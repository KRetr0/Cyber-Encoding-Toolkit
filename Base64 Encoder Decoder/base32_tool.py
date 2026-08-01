import base64


def encode(text):
    data = text.encode()
    result = base64.b32encode(data)
    return result.decode()


def decode(text):
    data = text.encode()
    result = base64.b32decode(data)
    return result.decode()