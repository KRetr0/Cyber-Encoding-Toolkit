from banner import show_banner, clear_screen

from encoders.base64_tool import (
    encode as b64_encode,
    decode as b64_decode
)

from encoders.base32_tool import (
    encode as b32_encode,
    decode as b32_decode
)

from encoders.hex_tool import (
    encode as hex_encode,
    decode as hex_decode
)

from encoders.url_tool import (
    encode as url_encode,
    decode as url_decode
)

from core.detector import detect

from core.errors import (
    EncodingError,
    show_error
)


def show_menu():

    print("""
====================================
 Cyber Encoding Toolkit v1.0.0
====================================

1 - Base64 Encode
2 - Base64 Decode

3 - Base32 Encode
4 - Base32 Decode

5 - Hex Encode
6 - Hex Decode

7 - URL Encode
8 - URL Decode

9 - Automatic Detection

0 - Exit

====================================
""")



def detection_menu():

    text = input(
        "\nData: "
    )


    results = detect(text)


    if not results:

        print(
            "\n[!] Unknown format"
        )

        return


    print(
        "\nDetection Results:\n"
    )


    print(
        f"Most Possible Format: {results[0][0]}"
    )

    print(
        f"Confidence: {results[0][1]}%"
    )


    if len(results) > 1:

        print(
            "\nOther Results:"
        )


        for name, score in results[1:]:

            print(
                f"{name}: {score}%"
            )



def main():

    # İlk açılış banner animasyonu
    show_banner(animated=True)


    while True:


        show_menu()


        choice = input(
            "Selection: "
        ).strip()



        try:


            if choice == "1":

                text = input(
                    "Data: "
                )

                print(
                    "\nResult:",
                    b64_encode(text)
                )



            elif choice == "2":

                text = input(
                    "Data: "
                )

                print(
                    "\nResult:",
                    b64_decode(text)
                )



            elif choice == "3":

                text = input(
                    "Data: "
                )

                print(
                    "\nResult:",
                    b32_encode(text)
                )



            elif choice == "4":

                text = input(
                    "Data: "
                )

                print(
                    "\nResult:",
                    b32_decode(text)
                )



            elif choice == "5":

                text = input(
                    "Data: "
                )


                style = input(
                    "Format (normal/space/colon): "
                ).strip()


                print(
                    "\nResult:",
                    hex_encode(
                        text,
                        style
                    )
                )



            elif choice == "6":

                text = input(
                    "Data: "
                )

                print(
                    "\nResult:",
                    hex_decode(text)
                )



            elif choice == "7":

                text = input(
                    "Data: "
                )


                mode = input(
                    "Mode (standard/form): "
                ).strip()


                print(
                    "\nResult:",
                    url_encode(
                        text,
                        mode
                    )
                )



            elif choice == "8":

                text = input(
                    "Data: "
                )


                mode = input(
                    "Mode (standard/form): "
                ).strip()


                print(
                    "\nResult:",
                    url_decode(
                        text,
                        mode
                    )
                )



            elif choice == "9":

                detection_menu()



            elif choice == "0":

                print(
                    "\nClosing Cyber Encoding Toolkit..."
                )

                break



            else:

                print(
                    "\n[!] Invalid selection"
                )



        except EncodingError as error:

            show_error(error)



        except Exception as error:

            show_error(
                f"Unexpected error: {error}"
            )



        input(
            "\nPress Enter to continue..."
        )


        # Ekranı temizle ve bannerı geri getir
        clear_screen()

        show_banner(animated=False)



if __name__ == "__main__":

    main()