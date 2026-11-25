import re


def starts_with_number(text):
    return bool(re.match(r"\d+", text))


def first_number(text):
    m = re.search(r"\d+", text)
    return int(m.group()) if m else None


def is_whole_number(text):
    return bool(re.fullmatch(r"\d+", text))


samples = ["42 apples", "apples 42", "42", "forty-two", ""]

for s in samples:
    m_res = starts_with_number(s)
    s_res = first_number(s)
    f_res = is_whole_number(s)
    print(f"{s!r:<12} match={str(m_res):<5} search={str(s_res):<5} fullmatch={f_res}")
