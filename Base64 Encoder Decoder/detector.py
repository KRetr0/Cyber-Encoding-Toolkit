import re


def detect(data):

    results = []


    # URL kontrolü
    if re.search(r"%[0-9A-Fa-f]{2}", data):
        results.append(
            ("URL Encoding", 95)
        )


    # Hex kontrolü
    if re.fullmatch(r"[0-9A-Fa-f]+", data):
        results.append(
            ("Hexadecimal", 90)
        )


    # Base32 kontrolü
    if re.fullmatch(r"[A-Z2-7]+=*", data):
        results.append(
            ("Base32", 80)
        )


    # Base64 kontrolü
    if re.fullmatch(r"[A-Za-z0-9+/]+=*", data):
        results.append(
            ("Base64", 85)
        )


    return results