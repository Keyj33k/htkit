#!/usr/bin/env python3

try:
    from whois import whois
    from termcolor import colored
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

class WhoisLookupForURL:
    def __init__(self, uniformresourcelocator: str):
        self.uniformresourcelocator = uniformresourcelocator

    def main(self):
        while True:
            try:
                print(colored(whois(self.uniformresourcelocator).text, "white"))
                input(f"{W}[{R}*{W}] Press enter key to continue")
                break
            except Exception as excerr:
                print(f"{W}[{Y}-{W}] Error{R}:{W} {excerr}")
                break
