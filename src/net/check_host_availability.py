#!/usr/bin/env python3

try:
    from subprocess import call, CalledProcessError
    from termcolor import colored as cld
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


class CheckHostAvailability:
    def __init__(self, target_address: str, ping_count: str):
        self.ping_count = ping_count
        self.target_address = target_address

    def main(self):
        while True:
            try:
                print(W)
                if self.ping_count == "":
                    call(["ping", "-c", "2", self.target_address])
                else:
                    call(["ping", "-c", self.ping_count, self.target_address])
                input(f"\n{W}[{R}*{W}] Press enter key to continue")
                break
            except CalledProcessError as cpe:
                print(f"{W}[{Y}-{W}] Error: {cpe}")
