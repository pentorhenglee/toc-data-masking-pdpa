import re

def address_masking(text):
    pattern = re.compile(r'(Address:\s*)(\S+)')

    text = pattern.sub(
        lambda m: m.group(1)+ 'X' * len(m.group(2)) ,
        text
    )
    return text
