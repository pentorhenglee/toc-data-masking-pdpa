# เคสรวม: ข้อความเดียวมีหลายประเภทปนกัน ส่งผ่าน mask ครบทั้ง 5 ไฟล์
# รันจาก root ด้วยคำสั่ง  python -m tests.test_combined

from maskers import credit_card, phone, dob, email, address

maskers = [credit_card, phone, dob, email, address]

cases = [
    ("Customer somchai.d@company.com called from 093-245-7894 regarding card 1234-5678-9012-3456. DOB:25/12/2549 Address: 689 ซอยลาดกระบัง 19 ถนนลาดกระบัง แขวงลาดกระบัง เขตลาดกระบัง กรุงเทพฯ",
     "Customer s*******d@company.com called from XXX-XXX-7894 regarding card XXXX-XXXX-XXXX-3456. DOB:XX/XX/25XX Address: XXX ซอยลาดกระบัง 19 ถนนลาดกระบัง แขวงลาดกระบัง เขตลาดกระบัง กรุงเทพฯ"),
    ("093-245-7894 1234-5678-9012-3456", "XXX-XXX-7894 XXXX-XXXX-XXXX-3456"),
    ("DOB:25/12/2549 Address: 25 ถนนสุขุมวิท แขวงคลองเตย เขตคลองเตย กรุงเทพฯ",
     "DOB:XX/XX/25XX Address: XX ถนนสุขุมวิท แขวงคลองเตย เขตคลองเตย กรุงเทพฯ"),
    ("ไม่มีข้อมูลส่วนบุคคลในบรรทัดนี้", "ไม่มีข้อมูลส่วนบุคคลในบรรทัดนี้"),
    ("", ""),
]

passed = 0
for text, expected in cases:
    got = text
    for m in maskers:
        got = m.mask(got)
    if got == expected:
        passed += 1
        print("PASS", text)
    else:
        print("FAIL", text)
        print("  expected:", expected)
        print("  got:     ", got)

print(f"{passed}/{len(cases)} passed")
