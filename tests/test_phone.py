# คนเขียนไฟล์นี้: คน 8
# เทส masker ของ: คน 3 (maskers/phone.py)
#
# อ่าน tests/README.md ก่อนเริ่ม แล้วเปิด test_cases.md ที่ root หมวด "เบอร์โทร"
# รันจาก root ด้วยคำสั่ง  python -m tests.test_phone

from maskers.phone import mask

cases = [
    ("093-245-7894", "XXX-XXX-7894"),
    ("Call 093-245-7894 today", "Call XXX-XXX-7894 today"),
    ("093-245-7894 / 081-222-3333", "XXX-XXX-7894 / XXX-XXX-3333"),
    ("1234-5678-9012-3456", "1234-5678-9012-3456"),
    ("123-456789-0", "123-456789-0"),
]

passed = 0
for text, expected in cases:
    got = mask(text)
    if got == expected:
        passed += 1
        print("PASS", text)
    else:
        print("FAIL", text)
        print("  expected:", expected)
        print("  got:     ", got)

print(f"{passed}/{len(cases)} passed")
