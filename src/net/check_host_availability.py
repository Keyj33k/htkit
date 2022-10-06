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

w = "\033[0;37m"
g = "\033[0;32m"
r = "\033[0;31m"


class CheckHostAvailability:
    def __init__(self, target_address: str):
        self.target_address = target_address

    def main(self):
        while True:
            if self.target_address == 'x' or self.target_address == 'exit':
                break

            print(f"\n{w}[{g}+{w}] Result{r}:{w}\n{r}{'=' * 70}{w}")

            try:
                call(["ping", "-c", "2", self.target_address])
            except CalledProcessError as cpe:
                print(cld(str(cpe), "red"))

            print(f"{r}{'=' * 70}\n{chr(0xa)}")
            input(f"{w}[{r}*{w}] Press enter key to continue")
            break
