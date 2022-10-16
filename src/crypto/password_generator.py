#!/usr/bin/env python3

try:
    from random import sample
    from string import digits, ascii_uppercase, ascii_lowercase
    from src.utils.coloring import R, W, Y, G
except ImportError:
    raise RuntimeError("""
    Oops,

    this tool uses important modules, which don't seem to be 
    installed at the moment.

    Use the requirements file and this command:
    "pip3 install -r requirements.txt" 

    You will find this file in the req directory.
    """)

class PasswordGenerator:
    def __init__(self, password_length: int):
        self.password_length = password_length

    def main(self):
        while True:
            if self.password_length < 8:
                print(f"{W}[{Y}-{W}] Your password should be always bigger than eight characters{R}.")
                break

            special_chars = "!$%&/()?{}][-_"
            mixer = digits + ascii_lowercase + ascii_uppercase + special_chars
            final_password = ''.join(sample(mixer, self.password_length))

            print(f"{W}[{G}+{W}] Generated {self.password_length} digits value{R}:{W} {final_password}")
            input(f"{W}[{R}*{W}] Press enter key to continue")
            break
