# คนเขียนไฟล์นี้: คน 4
# เทส masker ของ: คน 2 (maskers/credit_card.py)
#
# อ่าน tests/README.md ก่อนเริ่ม แล้วเปิด test_cases.md ที่ root หมวด "เลขบัตรเครดิต"
# รันจาก root ด้วยคำสั่ง  python -m tests.test_credit_card

from maskers.credit_card import mask

# TODO 1: ก๊อปเคสจาก test_cases.md หมวดเลขบัตรเครดิต มาใส่ที่นี่
# แต่ละตัวเป็นคู่ (input, expected)
cases = [
    # ("1234-5678-9012-3456", "XXXX-XXXX-XXXX-3456"),
]

# TODO 2: เขียนลูปวนทุกเคสใน cases
#   - เรียก mask(input) เก็บผลที่ได้ไว้
#   - ถ้าตรงกับ expected พิมพ์ PASS
#   - ถ้าไม่ตรง พิมพ์ FAIL พร้อมบอกว่า input คืออะไร ได้อะไรมา และควรได้อะไร
#   - จบด้วยสรุปว่าผ่านกี่เคสจากทั้งหมดกี่เคส
#
# ใช้ print ธรรมดา ห้ามใช้ pytest
#
# ตอนรันครั้งแรกจะ FAIL หมดหรือ error เพราะยังไม่มีใครเขียน regex นั่นถูกแล้ว
