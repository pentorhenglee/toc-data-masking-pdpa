import re

PATTERN = re.compile(r"(?<![\d-])\d{3}-\d{3}-(\d{4})(?![\d-])")


def mask(text):
    return PATTERN.sub(r"XXX-XXX-\1", text)
