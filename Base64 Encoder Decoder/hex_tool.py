def encode(text, style="normal"):
    hex_data = text.encode().hex()

    if style == "space":
        return " ".join(
            hex_data[i:i+2]
            for i in range(0, len(hex_data), 2)
        )

    elif style == "colon":
        return ":".join(
            hex_data[i:i+2]
            for i in range(0, len(hex_data), 2)
        )

    return hex_data


def decode(hex_data):
    hex_data = hex_data.replace(" ", "")
    hex_data = hex_data.replace(":", "")

    return bytes.fromhex(hex_data).decode() 