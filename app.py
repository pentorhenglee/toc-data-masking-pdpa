"""
app.py (Flask) = ตัวกลางของระบบ

ข้อตกลงกับ index.html:
  - ช่องกรอก (<textarea>) ต้องมี name="user_text"
  - ปุ่มส่ง form มี name="action" ค่าเป็น "mask" หรือ "example"
  - template ได้ตัวแปร:
        original   ข้อความเดิมที่ผู้ใช้พิมพ์ ("" ตอนเปิดหน้าครั้งแรก)
        segments   ข้อความที่หั่นเป็นชิ้นแล้ว (None = ยังไม่ได้กด Mask)
        counts     จำนวนที่เจอแยกตามประเภท เช่น {"phone": 1, ...}
        types      รายชื่อประเภท [(ชื่อ, ชื่อที่โชว์), ...] ใช้ทำ checkbox
        github_url ลิงก์ GitHub ที่หน้าเว็บต้องมี (โจทย์บังคับ)

ข้อตกลงกับ maskers/*.py:
  - ทุกไฟล์มี PATTERN (regex ที่ compile แล้ว) และฟังก์ชัน mask(text)

Run:
    python app.py
แล้วเปิด http://127.0.0.1:5001
"""

import re
import shutil
from flask import request, jsonify
import io
from PIL import Image, ImageOps, UnidentifiedImageError
import pytesseract
import os

import pytesseract
import shutil

# กำหนด path ของ Tesseract ภายใน Docker (Linux)
pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

from flask import Flask, render_template, request

from maskers import credit_card, phone, dob, email, address


app = Flask(__name__)

INPUT_FIELD = "user_text"

GITHUB_URL = "https://github.com/pentorhenglee/toc-data-masking-pdpa"

# (ชื่อประเภท, ชื่อที่โชว์บนหน้าเว็บ, ไฟล์ masker)
MASKERS = [
    ("credit_card", "บัตรเครดิต", credit_card),
    ("phone", "เบอร์โทร", phone),
    ("dob", "วันเกิด", dob),
    ("email", "อีเมล", email),
    ("address", "ที่อยู่", address),
]

TYPES = [(name, label) for name, label, module in MASKERS]

# ข้อความตัวอย่างของปุ่ม Example = เคสรวมใน test_cases.md (มีครบ 5 ประเภท)
EXAMPLE_TEXT = (
    "Customer somchai.d@company.com called from 093-245-7894 "
    "regarding card 1234-5678-9012-3456. DOB:25/12/2549 "
    "Address: 689 ซอยลาดกระบัง 19 ถนนลาดกระบัง แขวงลาดกระบัง เขตลาดกระบัง กรุงเทพฯ"
)

# ส่วนที่ถูกเซ็นเซอร์ = X หรือ * ติดกัน ที่อาจมี - หรือ / คั่นตรงกลาง
# เช่น XXXX-XXXX-XXXX, XX/XX, *******
RED_PATTERN = re.compile(r"[X*]+(?:[-/][X*]+)*")

EXAMPLES_DIR = os.path.join(app.static_folder, "examples")
EXAMPLES = [
    ("all_types.txt", "รวมครบ 5 ประเภท", "ข้อความเดียวมีบัตรเครดิต เบอร์โทร วันเกิด อีเมล และที่อยู่"),
    ("credit_card.txt", "บัตรเครดิต", "เลขบัตรในประโยค หลายใบ และเบอร์โทรที่ต้องไม่โดนแตะ"),
    ("phone.txt", "เบอร์โทร", "เบอร์ในประโยค หลายเบอร์ และเลขบัตร/เลขบัญชีที่ต้องไม่โดนแตะ"),
    ("dob.txt", "วันเกิด", "DOB: ปกติ หลายอัน และวันที่ที่ไม่มี DOB: นำหน้า"),
    ("email.txt", "อีเมล", "อีเมลในประโยค โดเมนหลายชั้น และหลายอัน"),
    ("address.txt", "ที่อยู่", "มีซอย ไม่มีซอย เลขที่บ้านหลักเดียว และไม่มี Address: นำหน้า"),
    ("mixed.txt", "เคสปนกัน", "หลายประเภทอยู่ติดกัน และบรรทัดที่ไม่มีข้อมูลส่วนบุคคล"),
    ("ocr_sample.png", "รูปภาพสำหรับ OCR", "ใช้ทดสอบปุ่ม Import Image แล้วกด Extract Text"),
    ("OCR_CARD.png", "รูปบัตรสำหรับ OCR", "รูปบัตรเครดิตพื้นสี มีเลขบัตร ที่อยู่ วันเกิด อีเมล และเบอร์โทร"),
]


def split_red(masked):
    """หั่นข้อความที่เซ็นเซอร์แล้วเป็นชิ้น ๆ แต่ละชิ้นบอกว่าต้องเป็นสีแดงไหม

    "XXX-XXX-7894" -> [("XXX-XXX", True), ("-7894", False)]
    """
    parts = []
    pos = 0
    for m in RED_PATTERN.finditer(masked):
        if m.start() > pos:
            parts.append((masked[pos:m.start()], False))
        parts.append((m.group(), True))
        pos = m.end()
    if pos < len(masked):
        parts.append((masked[pos:], False))
    return parts


def find_pii(text):
    """ใช้ PATTERN ของทั้ง 5 ไฟล์หาทุกจุดในข้อความเดิม แล้วเรียงตามตำแหน่ง

    คืนค่าเป็น list ของ (ตำแหน่งเริ่ม, ตำแหน่งจบ, ชื่อประเภท, ไฟล์ masker)
    """
    found = []
    for name, label, module in MASKERS:
        for m in module.PATTERN.finditer(text):
            found.append((m.start(), m.end(), name, module))
    found.sort(key=lambda f: f[0])
    return found


def build_segments(text):
    """หั่นข้อความทั้งก้อนเป็นชิ้น ๆ ให้ template วนลูปแสดงผล

    ชิ้นธรรมดา      {"type": None, "text": "..."}
    ชิ้นที่ต้องปิด   {"type": "phone", "original": "093-245-7894",
                    "parts": [("XXX-XXX", True), ("-7894", False)]}
    """
    segments = []
    counts = {name: 0 for name, label, module in MASKERS}
    pos = 0

    for start, end, name, module in find_pii(text):
        # ทับกับจุดก่อนหน้า (เคสในโจทย์ไม่มี) ใช้อันที่เจอก่อน
        if start < pos:
            continue

        if start > pos:
            segments.append({"type": None, "text": text[pos:start]})

        original = text[start:end]
        segments.append({
            "type": name,
            "original": original,
            "parts": split_red(module.mask(original)),
        })
        counts[name] += 1
        pos = end

    if pos < len(text):
        segments.append({"type": None, "text": text[pos:]})

    return segments, counts


@app.route("/", methods=["GET", "POST"])
def index():
    original = ""
    segments = None
    counts = None

    if request.method == "POST":
        action = request.form.get("action", "mask")

        if action == "example":
            original = EXAMPLE_TEXT
        else:
            original = request.form.get(INPUT_FIELD, "")
            # เบราว์เซอร์ส่งการขึ้นบรรทัดใหม่มาเป็น \r\n แปลงเป็น \n ให้เหมือนกันหมด
            original = original.replace("\r\n", "\n")
            segments, counts = build_segments(original)

    return render_template(
        "index.html",
        original=original,
        segments=segments,
        counts=counts,
        types=TYPES,
        github_url=GITHUB_URL,
    )


@app.route("/ocr", methods=["POST"])
def ocr():
    uploaded_file = request.files.get("image")

    if not uploaded_file or not uploaded_file.filename:
        return jsonify({"error": "กรุณาเลือกไฟล์ภาพ"}), 400

    try:
        image_bytes = uploaded_file.read()

        # จำกัดขนาดไฟล์ไม่เกิน 5 MB
        if len(image_bytes) > 5 * 1024 * 1024:
            return jsonify({"error": "ไฟล์ภาพต้องมีขนาดไม่เกิน 5 MB"}), 413

        with Image.open(io.BytesIO(image_bytes)) as image:
            image = ImageOps.exif_transpose(image)
            image = image.convert("RGB")

            text = pytesseract.image_to_string(
                image,
                lang="tha+eng"
            ).strip()

        return jsonify({"text": text})

    except UnidentifiedImageError:
        return jsonify({"error": "ไฟล์ที่อัปโหลดไม่ใช่ภาพที่รองรับ"}), 400

    except pytesseract.TesseractNotFoundError:
        return jsonify({"error": "ไม่พบ Tesseract OCR ในระบบ"}), 500

    except pytesseract.TesseractError:
        return jsonify({"error": "เกิดข้อผิดพลาดระหว่าง OCR"}), 500

@app.route("/examples")
def examples():
    files = []
    for filename, title, description in EXAMPLES:
        preview = None
        if filename.endswith(".txt"):
            with open(os.path.join(EXAMPLES_DIR, filename), encoding="utf-8") as f:
                preview = f.read()
        files.append({
            "filename": filename,
            "title": title,
            "description": description,
            "preview": preview,
        })

    return render_template("examples.html", files=files, github_url=GITHUB_URL)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)