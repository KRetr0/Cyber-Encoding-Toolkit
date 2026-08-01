from urllib.parse import quote, unquote, quote_plus, unquote_plus


def encode(text, mode="standard"):

    if mode == "form":
        return quote_plus(text)

    return quote(text)


def decode(text, mode="standard"):

    if mode == "form":
        return unquote_plus(text)

    return unquote(text)    