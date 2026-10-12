import re

PATTERN = re.compile(r'(?<![\d-])\d{4}-\d{4}-\d{4}-(\d{4})(?![\d-])')


def mask(text: str) -> str:
    """
    เซ็นเซอร์เลขบัตรเครดิตรูปแบบ XXXX-XXXX-XXXX-XXXX
    เหลือเฉพาะ 4 ตัวท้ายตามข้อกำหนดใน PDF ของอาจารย์
    """
    if not text:
        return text

    return PATTERN.sub(r'XXXX-XXXX-XXXX-\1', text)
