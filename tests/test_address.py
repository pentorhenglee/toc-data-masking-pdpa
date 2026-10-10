# คนรีวิวไฟล์นี้: คน 3
# เทส masker ของ: คน 6 (maskers/address.py)
#
# อ่าน tests/README.md ก่อนเริ่ม แล้วเปิด test_cases.md ที่ root หมวด "ที่อยู่"
# รันจาก root ด้วยคำสั่ง  python -m tests.test_address

from maskers.address import mask

cases = [
    ("Address: 689 ซอยลาดกระบัง 19 ถนนลาดกระบัง แขวงลาดกระบัง เขตลาดกระบัง กรุงเทพฯ", "Address: XXX ซอยลาดกระบัง 19 ถนนลาดกระบัง แขวงลาดกระบัง เขตลาดกระบัง กรุงเทพฯ"),
    ("Address: 45 ถนนพระราม 4 แขวงคลองเตย เขตคลองเตย กรุงเทพฯ", "Address: XX ถนนพระราม 4 แขวงคลองเตย เขตคลองเตย กรุงเทพฯ"),
    ("Address: 7 ถนนสุขุมวิท แขวงคลองเตย เขตคลองเตย กรุงเทพฯ", "Address: X ถนนสุขุมวิท แขวงคลองเตย เขตคลองเตย กรุงเทพฯ"),
    ("689 ซอยลาดกระบัง 19 ถนนลาดกระบัง", "689 ซอยลาดกระบัง 19 ถนนลาดกระบัง"),
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
