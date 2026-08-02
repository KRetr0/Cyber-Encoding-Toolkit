import re
import base64


def check_url(data):
    """
    URL Encoding detection
    """

    if re.search(r"%[0-9A-Fa-f]{2}", data):
        return 95

    return 0



def check_hex(data):
    """
    Hexadecimal detection
    """

    cleaned = data.replace(" ", "").replace(":", "")

    # Hex minimum uzunluk kontrolü
    if len(cleaned) < 4:
        return 0

    # Çift karakter olmalı
    if len(cleaned) % 2 != 0:
        return 0

    if re.fullmatch(r"[0-9A-Fa-f]+", cleaned):

        return 90

    return 0



def check_base32(data):
    """
    Base32 detection
    """

    if len(data) < 8:
        return 0

    if re.fullmatch(r"[A-Z2-7]+=*", data):

        try:
            base64.b32decode(data)
            return 85

        except Exception:
            return 0

    return 0



def check_base64(data):
    """
    Base64 detection
    """

    if len(data) < 8:
        return 0


    if not re.fullmatch(r"[A-Za-z0-9+/]+=*", data):
        return 0


    try:

        decoded = base64.b64decode(
            data,
            validate=True
        )

        # Decode edilen veri varsa
        if decoded:
            return 85


    except Exception:

        return 0


    return 0



def detect(data):
    """
    Main detection engine
    Returns sorted results
    """

    results = []


    detectors = {

        "URL Encoding": check_url,

        "Hexadecimal": check_hex,

        "Base32": check_base32,

        "Base64": check_base64

    }


    for name, detector in detectors.items():

        score = detector(data)

        if score:

            results.append(
                (
                    name,
                    score
                )
            )


    # En yüksek confidence ilk sırada
    results.sort(
        key=lambda x: x[1],
        reverse=True
    )


    return results