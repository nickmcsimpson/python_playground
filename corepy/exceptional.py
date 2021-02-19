import sys
from math import log

DIGIT_MAP = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
}


def convert(s):
    """converts strings into numbers"""
    x = -1
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        return int(number)
    except (KeyError, TypeError) as e:
        print(f"Conversion Error {e!r}", file=sys.stderr)
        raise


def string_log(s):
    v = convert(s)
    return log(v)
