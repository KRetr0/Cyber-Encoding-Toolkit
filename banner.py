import time
import os


def clear_screen():

    os.system(
        "cls" if os.name == "nt" else "clear"
    )



def show_banner(animated=True):

    banner = r"""
 ██████╗██╗   ██╗██████╗ ███████╗██████╗
██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗
██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝
██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗
╚██████╗   ██║   ██████╔╝███████╗██║  ██║
 ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝


        Cyber Encoding Toolkit v1.0.0
        Encoding & Detection Security Utility

"""


    if animated:

        clear_screen()


        for char in banner:

            print(
                char,
                end="",
                flush=True
            )

            time.sleep(0.002)


    else:

        print(banner)