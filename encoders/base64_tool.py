import base64

from core.errors import DecodeError, InvalidInputError



def encode(text):
    """
    Encode text to Base64
    """

    if not text:
        raise InvalidInputError(
            "Input cannot be empty"
        )


    data = text.encode("utf-8")

    result = base64.b64encode(
        data
    )

    return result.decode("utf-8")



def decode(text):
    """
    Decode Base64 to text
    """

    if not text:
        raise InvalidInputError(
            "Input cannot be empty"
        )


    try:

        data = text.encode("utf-8")

        result = base64.b64decode(
            data,
            validate=True
        )

        return result.decode("utf-8")


    except UnicodeDecodeError:

        raise DecodeError(
            "Decoded data is not valid UTF-8 text"
        )


    except Exception:

        raise DecodeError(
            "Invalid Base64 input"
        )