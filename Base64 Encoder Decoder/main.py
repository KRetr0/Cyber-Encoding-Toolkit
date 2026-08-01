from base64_tool import encode as b64_encode, decode as b64_decode
from base32_tool import encode as b32_encode, decode as b32_decode
from hex_tool import encode as hex_encode, decode as hex_decode
from url_tool import encode as url_encode, decode as url_decode
from detector import detect


print("=== Cyber Encoding Toolkit ===")
print()

print("1 - Base64 Encode")
print("2 - Base64 Decode")
print("3 - Base32 Encode")
print("4 - Base32 Decode")
print("5 - Hex Encode")
print("6 - Hex Decode")
print("7 - URL Encode")
print("8 - URL Decode")
print("9 - Auto Detect")

print()


choice = input("Selection: ").strip()


if choice == "1":

    text = input("Data: ")

    print(
        "Result:",
        b64_encode(text)
    )


elif choice == "2":

    text = input("Data: ")

    print(
        "Result:",
        b64_decode(text)
    )


elif choice == "3":

    text = input("Data: ")

    print(
        "Result:",
        b32_encode(text)
    )


elif choice == "4":

    text = input("Data: ")

    print(
        "Result:",
        b32_decode(text)
    )


elif choice == "5":

    text = input("Data: ")

    style = input(
        "Format (normal/space/colon): "
    ).strip()


    print(
        "Result:",
        hex_encode(text, style)
    )


elif choice == "6":

    text = input("Data: ")

    print(
        "Result:",
        hex_decode(text)
    )


elif choice == "7":

    text = input("Data: ")

    mode = input(
        "Mode (standard/form): "
    ).strip()


    print(
        "Result:",
        url_encode(text, mode)
    )


elif choice == "8":

    text = input("Data: ")

    mode = input(
        "Mode (standard/form): "
    ).strip()


    print(
        "Result:",
        url_decode(text, mode)
    )


elif choice == "9":

    text = input("Data: ")


    results = detect(text)


    if results:

        print("\nDetection Results:")

        for name, score in results:

            print(
                f"{name}: {score}%"
            )

    else:

        print("Unknown format")


else:

    print("Invalid selection")