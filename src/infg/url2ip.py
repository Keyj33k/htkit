#!/usr/bin/env python3

try:
    from socket import gethostbyname, gaierror, gethostbyaddr
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

def error_message():
    print(f"{W}[{Y}-{W}] You need to enter a value like{R}:{W} example.com{R}.")
    input(f"{W}[{R}*{W}] Press enter key to continue")

class GetIPv4fromURL:
    def __init__(self, uniformresourcelocator: str):
        self.uniformresourcelocator = uniformresourcelocator

    def main(self):
        while True:
            if self.uniformresourcelocator == 'x' or self.uniformresourcelocator == "exit": break

            try:
                print(f"{W}[{G}+{W}] IPv4{R}:{W} {gethostbyname(self.uniformresourcelocator)}\n"
                      f"{W}[{G}+{W}] IPv6{R}:{W} {''.join(gethostbyaddr(self.uniformresourcelocator)[2])}")
                input(f"{W}[{R}*{W}] Press enter key to continue")
                break
            except (ValueError, gaierror):
                error_message()
                break
