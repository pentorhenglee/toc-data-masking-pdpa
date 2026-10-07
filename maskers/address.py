import re

PATTERN = re.compile(r'(Address:\s*)(\S+)')


def mask(text):
    return PATTERN.sub(
        lambda m: m.group(1) + 'X' * len(m.group(2)),
        text
    )
