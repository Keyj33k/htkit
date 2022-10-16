#!/usr/bin/env python3

try:
    from requests import get
    from requests.exceptions import ConnectionError
    from time import sleep
    from datetime import datetime
    from src.colors.coloring import W, R, Y, G
except ImportError:
    raise RuntimeError("""
    Oops,

    this tool uses important modules, which don't seem to be 
    installed at the moment.

    Use the requirements file and this command:
    "pip3 install -r requirements.txt" 

    You will find this file in the req directory.
    """)

class HTTPHeader:
    def __init__(self, uniformresourcelocator: str):
        self.uniformresourcelocator = uniformresourcelocator

    def main(self):
        while True:
            print(f"{W}[{R}*{W}] Sending GET request")
            start = datetime.now()
            try:
                for category, result in get(f"http://{self.uniformresourcelocator}").headers.items():
                    sleep(0.25)
                    print(f"{W}[{G}+{W}] {category}{R}:{W} {result}")
                print(f"{W}[{R}*{W}] Done, runtime{R}:{W} {datetime.now() - start}")
                input(f"{W}[{R}*{W}] Press enter key to continue")
                break
            except ConnectionError as conn_err:
                print(f"{W}[{Y}-{W}] Error{R}:{W} {conn_err}")
                break

