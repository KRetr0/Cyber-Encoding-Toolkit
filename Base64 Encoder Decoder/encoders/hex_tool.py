from core.errors import DecodeError, InvalidInputError



def encode(text, style="normal"):
    """
    Encode text to hexadecimal format

    Styles:
    normal -> 48656c6c6f
    space  -> 48 65 6c 6c 6f
    colon  -> 48:65:6c:6c:6f
    """

    if not text:
        raise InvalidInputError(
            "Input cannot be empty"
        )


    hex_data = text.encode("utf-8").hex()


    if style == "space":

        return " ".join(
            hex_data[i:i+2]
            for i in range(
                0,
                len(hex_data),
                2
            )
        )


    elif style == "colon":

        return ":".join(
            hex_data[i:i+2]
            for i in range(
                0,
                len(hex_data),
                2
            )
        )


    return hex_data



def decode(hex_data):
    """
    Decode hexadecimal data to text
    """

    if not hex_data:
        raise InvalidInputError(
            "Input cannot be empty"
        )


    try:

        cleaned = (
            hex_data
            .replace(" ", "")
            .replace(":", "")
        )


        if len(cleaned) % 2 != 0:
            raise DecodeError(
                "Invalid hexadecimal length"
            )


        data = bytes.fromhex(
            cleaned
        )


        return data.decode(
            "utf-8"
        )


    except UnicodeDecodeError:

        raise DecodeError(
            "Hex data is not valid UTF-8 text"
        )


    except ValueError:

        raise DecodeError(
            "Invalid hexadecimal input"
        )


    except DecodeError:

        raise


    except Exception:

        raise DecodeError(
            "Hex decoding failed"
        )