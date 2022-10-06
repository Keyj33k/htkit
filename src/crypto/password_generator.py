#!/usr/bin/env python3

try:
    from random import sample
    from string import digits, ascii_uppercase, ascii_lowercase
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


class PasswordGenerator:
    def __init__(self, password_length: int):
        self.password_length = password_length

    def main(self):
        while True:
            if self.password_length == 0: break
            elif self.password_length < 8:
                print(f"{w}[{y}-{w}] Your password should be always bigger than eight characters{r}.")
                break

            special_chars = "!$%&/()?{}][-_"
            mixer = digits + ascii_lowercase + ascii_uppercase + special_chars
            final_password = ''.join(sample(mixer, self.password_length))

            print(f"{r}{'=' * 70}\n{w}[{g}+{w}] Your generated password{r}:"
                  f"{w} {final_password}\n{r}{'=' * 70}{chr(0xa)}")
            input(f"\n{w}[{r}*{w}] Press enter key to continue")
            break
