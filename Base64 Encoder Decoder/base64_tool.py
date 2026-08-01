import base64


def encode(text):
    data = text.encode()
    result = base64.b64encode(data)
    return result.decode()


def decode(text):
    data = text.encode()
    result = base64.b64decode(data)
    return result.decode()