# ToC Assignment — Data Masking for PDPA

A web app that takes bank-log text containing leaked personal data and **censors it
using Python regex (`re` module only)**.

Live: https://toc-data-masking-pdpa.vercel.app

## Team & Roles

| Role | หน้าที่ | รหัสนักศึกษา |
|------|--------|-------------|
| Coordinator | วางระบบ แบ่งงาน รวมโค้ดทุกส่วน และ deploy เว็บ | 67010585 |
| Maskers and Test | 5 คน คนละประเภท เขียน regex ในไฟล์ของตัวเองใน `maskers/` และรีวิวไฟล์เทส | 67010686, 67010522, 67011569, 67010207, 67010500 |
| Backend + Frontend | `app.py` เชื่อม masker ทั้ง 5 กับหน้าเว็บ ด้วย HTML/CSS | 67010465, 67010493, 67010500 |
| UX/UI | ดีไซน์ สไลด์ และตัดคลิป | 67010482 |

---

## Setup (do this after you clone)

```bash
# 1. go into the project
cd your folder workspace for this project

# 2. create a virtual environment (once)
python3 -m venv venv

# 3. activate it (EVERY new terminal)
source venv/bin/activate        # Mac / Linux
# venv\Scripts\activate         # Windows

# 4. install Flask (once)
pip install -r requirements.txt

# 5. run
python app.py
```

Open **http://127.0.0.1:5000** in your browser to see the app.
Stop the server with `Ctrl + C`. If you get "No module named flask", you forgot step 3.

---

## What we have to build (from the assignment)

Input: text typed by the user. Output: the same text with 5 data types censored.

| Data type | Rule | Example |
|-----------|------|---------|
| Credit card `XXXX-XXXX-XXXX-XXXX` | keep last 4 | `1234-5678-9012-3456` → `XXXX-XXXX-XXXX-3456` |
| Email | hide username except first & last char, keep domain | `somchai.d@company.com` → `s*******d@company.com` |
| Phone `XXX-XXX-XXXX` | keep last 4 | `093-245-7894` → `XXX-XXX-7894` |
| DOB (starts `DOB:`) | censor all but first 2 digits of year | `DOB:25/12/2549` → `DOB:XX/XX/25XX` |
| Address (starts `Address:`) | censor house number only | `Address: 689 ซอย...` → `Address: XXX ซอย...` |

**Constraint:** masking must use Python's `re` module only.

## Deliverables (due Wed 14 Oct 2569, before 09:00)
1. YouTube clip (≤ 10 min) focused on the regex application.
2. Live web app link — the page **must** link to this GitHub repo.

## Graded on
1. Regex coverage across many cases
2. Web app creativity + design
3. Presentation quality (must be cohesive across the whole group)
