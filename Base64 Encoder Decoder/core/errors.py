class EncodingError(Exception):
    """
    Base error class for Cyber Encoding Toolkit
    """
    pass



class InvalidInputError(EncodingError):
    """
    Empty or invalid user input
    """
    pass



class InvalidEncodingError(EncodingError):
    """
    Invalid encoding format
    """
    pass



class DecodeError(EncodingError):
    """
    Decode operation failed
    """
    pass



class UnsupportedOperationError(EncodingError):
    """
    Unsupported action
    """
    pass



def show_error(message):
    """
    Standard error output
    """

    print(
        f"[ERROR] {message}"
    )