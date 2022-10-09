#!/usr/bin/env python3

try:
    from requests import get
    from requests.exceptions import ConnectionError
    from time import sleep
    from datetime import datetime
except ImportError:
    raise RuntimeError("""
    Oops,

    this tool uses important modules, which don't seem to be 
    installed at the moment.

    Use the requirements file and this command:
    "pip3 install -r requirements.txt" 

    You will find this file in the req directory.
    """)

W = "\033[0;37m"
G = "\033[0;32m"
R = "\033[0;31m"
Y = "\033[0;33m"


class HTTPHeader:
    def __init__(self, uniformresourcelocator: str):
        self.uniformresourcelocator = uniformresourcelocator

    def main(self):
        while True:
            if self.uniformresourcelocator == 'x' or self.uniformresourcelocator == "exit": break
            print(f"{W}[{R}*{W}] Sending GET request")
            start = datetime.now()
            try:
                for category, result in get(f"http://{self.uniformresourcelocator}").headers.items():
                    sleep(0.25)
                    print(f"{W}[{G}+{W}] {category}{R}:{W} {result}")
                print(f"{W}[{R}*{W}] Done, runtime{R}:{W} {datetime.now() - start}")
                input(f"{W}[{R}*{W}] Press enter key to continue")
                break
            except ConnectionError:
                print(f"{W}[{Y}-{W}] Failed getting header from {self.uniformresourcelocator}{R}!")

