import re
def email_masking(text):
    pattern = re.compile(r'(Email:\s*)([\w.%+-])([\w.%+-]+)([\w.%+-])(@[\w.-]+\.[A-Za-z]{2,})')

    text = pattern.sub(
        lambda m: m.group(1) + m.group(2) + '*' * len(m.group(3)) + m.group(4) + m.group(5),
        text
    )
    return text
