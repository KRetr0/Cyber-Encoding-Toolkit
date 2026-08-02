import base64

from core.errors import DecodeError, InvalidInputError



def encode(text):
    """
    Encode text to Base32
    """

    if not text:
        raise InvalidInputError(
            "Input cannot be empty"
        )


    data = text.encode("utf-8")

    result = base64.b32encode(
        data
    )

    return result.decode("utf-8")



def decode(text):
    """
    Decode Base32 to text
    """

    if not text:
        raise InvalidInputError(
            "Input cannot be empty"
        )


    try:

        data = text.encode("utf-8")

        result = base64.b32decode(
            data
        )

        return result.decode("utf-8")


    except Exception:

        raise DecodeError(
            "Invalid Base32 input"
        )