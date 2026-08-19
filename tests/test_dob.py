# คนเขียนไฟล์นี้: คน 9
# เทส masker ของ: คน 4 (maskers/dob.py)
#
# อ่าน tests/README.md ก่อนเริ่ม แล้วเปิด test_cases.md ที่ root หมวด "วันเดือนปีเกิด"
# รันจาก root ด้วยคำสั่ง  python -m tests.test_dob

from maskers.dob import mask

# TODO 1: ก๊อปเคสจาก test_cases.md หมวดวันเดือนปีเกิด มาใส่ที่นี่
# แต่ละตัวเป็นคู่ (input, expected)
cases = [
    # ("DOB:25/12/2549", "DOB:XX/XX/25XX"),
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
