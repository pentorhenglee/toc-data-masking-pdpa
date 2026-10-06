import re

EMAIL_PATTERN = re.compile(r'([\w.%+-])([\w.%+-]+)([\w.%+-])(@[\w.-]+\.[A-Za-z]{2,})')


def mask(text):
    return EMAIL_PATTERN.sub(
        lambda m: m.group(1) + '*' * len(m.group(2)) + m.group(3) + m.group(4),
        text
    )
