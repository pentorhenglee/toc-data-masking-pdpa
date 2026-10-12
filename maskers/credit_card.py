import re

# รูปแบบเลขบัตรเครดิตตามโจทย์ใน PDF:
# มีรูปแบบ XXXX-XXXX-XXXX-XXXX ให้เซ็นเซอร์เหลือแค่ 4 ตัวท้าย
# เช่น 1234-5678-9012-3456 => XXXX-XXXX-XXXX-3456
#
# คำอธิบาย Regular Expression:
# (?<![\d-]) : Negative lookbehind - ข้างหน้าต้องไม่ใช่ตัวเลขหรือขีด เพื่อไม่ให้จับส่วนท้ายของเลขที่ยาวกว่า
# (?:\d{4}-){3} : เลข 4 หลักคั่นด้วยขีด ซ้ำ 3 กลุ่ม (Non-capturing group)
# (\d{4})    : กลุ่ม 4 หลักสุดท้าย (Group 1) เพื่อเก็บไว้เป็นเลขจริง
# (?![\d-])  : Negative lookahead - ข้างหลังต้องไม่ใช่ตัวเลขหรือขีด

PATTERN = re.compile(r'(?<![\d-])(?:\d{4}-){3}(\d{4})(?![\d-])')


def mask(text: str) -> str:
    """
    เซ็นเซอร์เลขบัตรเครดิตรูปแบบ XXXX-XXXX-XXXX-XXXX
    เหลือเฉพาะ 4 ตัวท้ายตามข้อกำหนดใน PDF ของอาจารย์
    """
    if not text:
        return text

    return PATTERN.sub(r'XXXX-XXXX-XXXX-\1', text)
