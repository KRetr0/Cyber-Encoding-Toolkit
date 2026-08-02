from urllib.parse import (
    quote,
    unquote,
    quote_plus,
    unquote_plus
)

from core.errors import (
    InvalidInputError,
    DecodeError
)



def encode(text, mode="standard"):
    """
    Encode text using URL encoding

    Modes:
    standard -> Hello World -> Hello%20World
    form     -> Hello World -> Hello+World
    """

    if not text:
        raise InvalidInputError(
            "Input cannot be empty"
        )


    try:

        if mode == "form":

            return quote_plus(
                text
            )


        return quote(
            text
        )


    except Exception:

        raise DecodeError(
            "URL encoding failed"
        )



def decode(text, mode="standard"):
    """
    Decode URL encoded data

    Modes:
    standard -> Hello%20World -> Hello World
    form     -> Hello+World -> Hello World
    """

    if not text:
        raise InvalidInputError(
            "Input cannot be empty"
        )


    try:

        if mode == "form":

            return unquote_plus(
                text
            )


        return unquote(
            text
        )


    except Exception:

        raise DecodeError(
            "Invalid URL encoded data"
        )