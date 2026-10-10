# คนรีวิวไฟล์นี้: คน 4
# เทส masker ของ: คน 2 (maskers/credit_card.py)
#
# อ่าน tests/README.md ก่อนเริ่ม แล้วเปิด test_cases.md ที่ root หมวด "เลขบัตรเครดิต"
# รันจาก root ด้วยคำสั่ง  python -m tests.test_credit_card

from maskers.credit_card import mask

cases = [
    ("1234-5678-9012-3456", "XXXX-XXXX-XXXX-3456"),
    ("Card 1234-5678-9012-3456 was used.", "Card XXXX-XXXX-XXXX-3456 was used."),
    ("1234-5678-9012-3456 and 9876-5432-1098-7654", "XXXX-XXXX-XXXX-3456 and XXXX-XXXX-XXXX-7654"),
    ("093-245-7894", "093-245-7894"),
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
