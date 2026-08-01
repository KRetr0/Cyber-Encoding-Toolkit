import argparse

from base64_tool import encode as b64_encode, decode as b64_decode
from base32_tool import encode as b32_encode, decode as b32_decode
from hex_tool import encode as hex_encode, decode as hex_decode
from url_tool import encode as url_encode, decode as url_decode
from detector import detect



parser = argparse.ArgumentParser(
    description="Cyber Encoding Toolkit"
)


parser.add_argument(
    "--type",
    choices=[
        "base64",
        "base32",
        "hex",
        "url"
    ]
)


parser.add_argument(
    "--encode",
    help="Encode data"
)


parser.add_argument(
    "--decode",
    help="Decode data"
)


parser.add_argument(
    "--detect",
    help="Detect encoding format"
)


args = parser.parse_args()



if args.detect:

    results = detect(args.detect)

    for name, score in results:
        print(
            f"{name}: %{score}"
        )


elif args.type == "base64":

    if args.encode:
        print(
            b64_encode(args.encode)
        )

    elif args.decode:
        print(
            b64_decode(args.decode)
        )


elif args.type == "base32":

    if args.encode:
        print(
            b32_encode(args.encode)
        )

    elif args.decode:
        print(
            b32_decode(args.decode)
        )


elif args.type == "hex":

    if args.encode:
        print(
            hex_encode(args.encode)
        )

    elif args.decode:
        print(
            hex_decode(args.decode)
        )


elif args.type == "url":

    if args.encode:
        print(
            url_encode(args.encode)
        )

    elif args.decode:
        print(
            url_decode(args.decode)
        )   