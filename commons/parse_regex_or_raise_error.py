import re


def parse_regex_or_raise_error(regex, text):
    match = re.search(regex, text)
    if match is None:
        raise Exception(f"Regex {regex} not parsed")
    return match
