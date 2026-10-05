import re

def mask(text):

    pattern = r'(DOB:\s*)(?:0?[1-9]|[12]\d|3[01])([/\-.])(?:0?[1-9]|1[0-2])\2(\d{2})\d{2}(?!\d)'

    return re.sub(pattern,
                  lambda m: f"{m.group(1)}XX{m.group(2)}XX{m.group(2)}{m.group(3)}XX",
                  text, flags=re.IGNORECASE)
