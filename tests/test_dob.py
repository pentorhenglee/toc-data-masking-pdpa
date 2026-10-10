# คนเขียนไฟล์นี้: คน 9
# เทส masker ของ: คน 4 (maskers/dob.py)
#
# อ่าน tests/README.md ก่อนเริ่ม แล้วเปิด test_cases.md ที่ root หมวด "วันเดือนปีเกิด"
# รันจาก root ด้วยคำสั่ง  python -m tests.test_dob

from maskers.dob import mask

cases = [
    ("DOB:25/12/2549", "DOB:XX/XX/25XX"),
    ("Customer DOB:25/12/2549 verified", "Customer DOB:XX/XX/25XX verified"),
    ("DOB:25/12/2549 DOB:01/01/2540", "DOB:XX/XX/25XX DOB:XX/XX/25XX"),
    ("25/12/2549", "25/12/2549"),
    ("Transaction date 25/12/2549", "Transaction date 25/12/2549"),
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
