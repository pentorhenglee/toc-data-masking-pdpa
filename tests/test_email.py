# คนเขียนไฟล์นี้: คน 2 (กัน)
# เทส masker ของ: คน 5 (maskers/email.py)
#
# เทสเฉพาะรูปแบบตามโจทย์ใน PDF ของอาจารย์
# รันจาก root ด้วยคำสั่ง  python -m tests.test_email

try:
    from maskers.email import mask
except ImportError:
    # เผื่อกรณี maskers/email.py ยังใช้ชื่อ email_masking ตาม commit ก่อนหน้า
    try:
        from maskers.email import email_masking as mask
    except ImportError:
        mask = None

# เคสตามโจทย์ใน PDF อาจารย์:
# ซ่อนชื่อผู้ใช้ยกเว้นตัวอักษรตัวแรกและตัวสุดท้าย เปิดเผยโดเมน
# เช่น somchai.d@company.com => s*******d@company.com
cases = [
    # เคสมาตรฐานตาม PDF
    ("somchai.d@company.com", "s*******d@company.com"),
    ("Contact somchai.d@company.com now", "Contact s*******d@company.com now"),
    ("pentor.h@kmitl.ac.th", "p******h@kmitl.ac.th"),
    ("a1234@x.com, pentor.h@kmitl.ac.th", "a***4@x.com, p******h@kmitl.ac.th"),
    ("Somchai.D@Company.com", "S*******D@Company.com"),
    # กันจับผิด (ไม่ใช่เมล ห้ามแตะ)
    ("ประชุม @ห้อง 401", "ประชุม @ห้อง 401"),
    ("follow @pentor for news", "follow @pentor for news"),
]

passed = 0
total = len(cases)

print("=" * 60)
print("เริ่มการทดสอบ: หมวดอีเมล (ตามรูปแบบใน PDF อาจารย์)")
print("=" * 60)

for inp, expected in cases:
    if mask is None:
        print(f"[FAIL] input:    {inp}")
        print(f"       expected: {expected}")
        print("       got:      ไม่พบฟังก์ชัน 'mask' หรือ 'email_masking' ใน maskers/email.py")
        continue

    try:
        result = mask(inp)
        if result == expected:
            print(f"[PASS] {inp} -> {result}")
            passed += 1
        else:
            print(f"[FAIL] input:    {inp}")
            print(f"       expected: {expected}")
            print(f"       got:      {result}")
    except Exception as e:
        print(f"[ERROR] input:    {inp}")
        print(f"        expected: {expected}")
        print(f"        error:    {e}")

print("-" * 60)
print(f"สรุปผลการทดสอบ: ผ่าน {passed}/{total} เคส")
if passed == total:
    print("สถานะ: ผ่านทุกเคส (ALL PASS)")
else:
    print(f"สถานะ: ยังมีเคสที่ไม่ผ่านอีก {total - passed} เคส (FAIL)")
print("=" * 60)
