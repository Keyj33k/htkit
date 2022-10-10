#!/usr/bin/env python3

try:
    from whois import whois
    from termcolor import colored
except ImportError:
    raise RuntimeError("""
    Oops,

    this tool uses important modules, which don't seem to be 
    installed at the moment.

    Use the requirements file and this command:
    "pip3 install -r requirements.txt" 

    You will find this file in the req directory.
    """)

w = "\033[0;37m"
g = "\033[0;32m"
r = "\033[0;31m"
y = "\033[0;33m"


class WhoisLookupForURL:
    def __init__(self, uniformresourcelocator: str):
        self.uniformresourcelocator = uniformresourcelocator

    def main(self):
        while True:
            try:
                print(colored(whois(self.uniformresourcelocator).text, "white"))
                input(f"{w}[{r}*{w}] Press enter key to continue")
                break
            except Exception as excerr:
                print(f"{w}[{y}-{w}] Error{r}:{w} {excerr}")
                break
