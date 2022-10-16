#!/usr/bin/env python3

try:
    from subprocess import call, CalledProcessError
    from termcolor import colored as cld
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

class CheckHostAvailability:
    def __init__(self, target_address: str, ping_count: int):
        self.ping_count = ping_count
        self.target_address = target_address

    def main(self):
        while True:
            try:
                if self.ping_count >= 20:
                    print(f"{W}[{Y}-{W}] Error{R}:{W} ping "
                          f"count of size {self.ping_count} is not supported")
                    break
                print(W)
                if self.ping_count == "":
                    call(["ping", "-c", str(2), self.target_address])
                else:
                    call(["ping", "-c", str(self.ping_count), self.target_address])
                input(f"\n{W}[{R}*{W}] Press enter key to continue")
                break
            except CalledProcessError as cpe:
                print(f"{W}[{Y}-{W}] Error: {cpe}")
                break
