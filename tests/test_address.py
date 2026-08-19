# คนเขียนไฟล์นี้: คน 3
# เทส masker ของ: คน 6 (maskers/address.py)
#
# อ่าน tests/README.md ก่อนเริ่ม แล้วเปิด test_cases.md ที่ root หมวด "ที่อยู่"
# รันจาก root ด้วยคำสั่ง  python -m tests.test_address

from maskers.address import mask

# TODO 1: ก๊อปเคสจาก test_cases.md หมวดที่อยู่ มาใส่ที่นี่
# แต่ละตัวเป็นคู่ (input, expected)
cases = [
    # ("Address: 689 ซอยลาดกระบัง 19", "Address: XXX ซอยลาดกระบัง 19"),
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
