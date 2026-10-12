import re

PATTERN = re.compile(r'(?<![\d-])(\d{4}-){3}(\d{4})(?![\d-])')

def mask(text: str) -> str:
    if not text:
        return text

    return PATTERN.sub(r'XXXX-XXXX-XXXX-\2', text)
