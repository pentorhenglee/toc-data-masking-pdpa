"""
app.py (Flask) = ตัวกลางของระบบ


ไอพวกงาน 8 (index.html) งาน 9 (แสดงผล/CSS):
  - ช่องกรอก (<textarea>) ต้องมี name="user_text"
  - template ได้ตัวแปร 3 ตัว:
        original   ข้อความเดิมที่ผู้ใช้พิมพ์ ("" ตอนเปิดหน้าครั้งแรก)
        result     ข้อความที่เซ็นเซอร์แล้ว (None ตอนเปิดหน้าครั้งแรก)
        github_url ลิงก์ GitHub ที่หน้าเว็บต้องมี (โจทย์บังคับ)
    ใช้ {% if result is not none %} เช็กว่าเพิ่งกดส่งหรือยัง
    (อย่าใช้ {% if result %} เพราะข้อความว่างที่เซ็นเซอร์แล้วก็ต้องแสดงผลได้)

Run:
    python app.py
แล้วเปิด http://127.0.0.1:5000
"""

from flask import Flask, render_template, request

from maskers import credit_card, phone, dob, email, address

app = Flask(__name__)

# ชื่อ name ของ <textarea> ใน index.html ต้องตรงกับค่านี้ (งาน 8 มาอ่านดิ๊)
INPUT_FIELD = "user_text"

# ลิงก์ GitHub ของพรี่เป็นต่อ ที่โจทย์บังคับให้มีบนหน้าเว็บ ส่งไปให้ template ใช้
GITHUB_URL = "https://github.com/pentorhenglee/toc-data-masking-pdpa"

# ลำดับการเรียก mask ตามขั้นตอนในชีตงาน
MASKERS = [
    ("credit_card", credit_card),
    ("phone", phone),
    ("dob", dob),
    ("email", email),
    ("address", address),
]


def mask_all(text):
    """ส่งข้อความผ่าน mask() ของทั้ง 5 ไฟล์ต่อกัน แล้วคืนข้อความที่ปิดครบแล้ว"""
    for name, module in MASKERS:
        mask_fn = getattr(module, "mask", None)
        if mask_fn is None:
            print(f"[app.py] maskers/{name}.py ยังไม่มีฟังก์ชัน mask() -> ข้าม")
            continue
        text = mask_fn(text)
    return text


# route เดียวรับทั้ง GET (เปิดหน้า) และ POST (กดปุ่ม)
@app.route("/", methods=["GET", "POST"])
def index():
    original = ""
    result = None

    if request.method == "POST":
        # ดึงข้อความที่ผู้ใช้พิมพ์ ใช้ .get พร้อมค่า default
        original = request.form.get(INPUT_FIELD, "")

        # เบราว์เซอร์ส่งการขึ้นบรรทัดใหม่ใน <textarea> มาเป็น \r\n
        # แปลงเป็น \n เพื่อให้ masker ทุกตัวเจอรูปแบบเดียวกัน
        original = original.replace("\r\n", "\n")

        print("[app.py] รับข้อความ:", repr(original))  # debug: ดูใน terminal

        result = mask_all(original)

    return render_template(
        "index.html",
        original=original,
        result=result,
        github_url=GITHUB_URL,
    )


if __name__ == "__main__":
    app.run(debug=True)