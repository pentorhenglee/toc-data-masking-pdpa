import re

def mask(text):
    text = re.sub(r"(?<![\d-])\d{3}-\d{3}-(\d{4})(?![\d-])", r"XXX-XXX-\1", text)
    return text