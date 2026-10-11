
import pytesseract
from PIL import Image, ImageOps, ImageFilter
from pathlib import Path

ALLOWED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff"}

def extract_text(image_path):
    path = Path(image_path)

    if path.suffix.lower() not in ALLOWED_EXTENSIONS:
        raise ValueError("Unsupported image format")

    with Image.open(path) as image:
        image = ImageOps.exif_transpose(image)
        image = ImageOps.grayscale(image)

        # ขยายภาพเพื่อช่วยอ่านข้อความขนาดเล็ก
        image = image.resize(
            (image.width * 2, image.height * 2)
        )

        # เพิ่มความคมชัดเล็กน้อย
        image = image.filter(ImageFilter.SHARPEN)

        # ทดลอง OCR ด้วยทั้งภาษาไทยและอังกฤษ
        text = pytesseract.image_to_string(
            image,
            lang="tha+eng",
            config="--psm 6"
        )

    return text.strip()