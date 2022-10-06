#!/usr/bin/env python3

try:
    from socket import gethostbyname, gaierror
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

w = "\033[0;37m"
g = "\033[0;32m"
r = "\033[0;31m"
y = "\033[0;33m"

def error_message():
    print(f"{w}[{y}-{w}] You need to enter a value like{r}:{w} google.com in example{r}.\n{chr(0xa)}")
    input(f"{w}[{r}*{w}] Press enter key to continue")

class GetIPv4fromURL:
    def __init__(self, uniformresourcelocator: str):
        self.uniformresourcelocator = uniformresourcelocator

    def main(self):
        while True:
            if self.uniformresourcelocator == 'x' or self.uniformresourcelocator == 'exit': break

            try:
                print(
                    f"{r}{'=' * 70}\n{w}[{g}+{w}] IP Address from {self.uniformresourcelocator}"
                    f" {r}->{w} " + f"{gethostbyname(self.uniformresourcelocator)}\n{r}{'=' * 70}\n{chr(0xa)}")
                input(f"{w}[{r}*{w}] Press enter key to continue")
                break
            except (ValueError, gaierror):
                error_message()
                break
