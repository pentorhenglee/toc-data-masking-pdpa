
import numpy as np
import cv2
import pytesseract

from PIL import Image, ImageOps
from pathlib import Path

ALLOWED_EXTENSIONS = {
    ".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff"
}

CUSTOM_WORDS = Path(__file__).resolve().parent / "custom_words.txt"


def extract_text(image_path):
    path = Path(image_path)

    if path.suffix.lower() not in ALLOWED_EXTENSIONS:
        raise ValueError("Unsupported image format")

    with Image.open(path) as image:
        # แก้ภาพที่ถ่ายกลับหัวจากข้อมูล EXIF
        image = ImageOps.exif_transpose(image)

        # แปลง PIL Image เป็น NumPy array แบบ RGB
        image = np.array(image.convert("RGB"))

    # RGB -> Grayscale
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    # ขยายภาพ 2 เท่า
    image = cv2.resize(
        image,
        None,
        fx=3,
        fy=3,
        interpolation=cv2.INTER_CUBIC
    )

    # ลด noise โดยรักษาขอบตัวอักษร
    image = cv2.bilateralFilter(image, 9, 75, 75)

    # ปรับพื้นหลังและตัวอักษรให้แยกกันชัดขึ้น
    image = cv2.adaptiveThreshold(cv2.bilateralFilter(image, 9, 75, 75), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    config = (
        "--oem 3 --psm 6 "
        f'--user-words "{CUSTOM_WORDS}"'
    )

    text = pytesseract.image_to_string(
        image,
        lang="tha+eng",
        config=config
    )

    return text.strip()