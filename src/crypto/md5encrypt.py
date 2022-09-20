#!/usr/bin/env python3

try:
    from termcolor import colored as cld
    import hashlib
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


class MD5Encrypt:
    def __init__(self, input_data: str):
        self.input_data = input_data

    def main(self):
        while True:
            if self.input_data == 'x' or self.input_data == 'exit':
                break

            try:
                print(f"{r}=" * 70)
                print(f"{w}[{g}+{w}] {self.input_data} {r}->{w} {hashlib.md5(self.input_data.encode()).hexdigest()}")
                input(f"{r}{'=' * 70}\n{w}[{r}*{w}] Press enter key to continue")
                break
            except Exception as excerr:
                print(cld(f"{excerr}", "red"))
                input(f"{chr(0xa)}\n{w}[{r}*{w}] Press enter key to continue")
                break

                # https://www.md5online.org/md5-decrypt.html
                # This program is using a big database to bruteforce the hash for you
                
                
