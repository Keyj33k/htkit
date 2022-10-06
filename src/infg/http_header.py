#!/usr/bin/env python3

try:
    from requests import get
    from requests.exceptions import ConnectionError
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


class HTTPHeader:
    def __init__(self, uniformresourcelocator: str):
        self.uniformresourcelocator = uniformresourcelocator

    def main(self):
        while True:
            if self.uniformresourcelocator == 'x' or self.uniformresourcelocator == 'exit':
                break

            print(f"\n{w}[{g}+{w}] Result{r}:\n{'=' * 70}{w}")

            try:
                for category, result in get(f"http://{self.uniformresourcelocator}").headers.items():
                    print(f"{category}: {result}")

                print(f"{r}{'=' * 70}\n{chr(0xa)}")
                input(f"{w}[{r}*{w}] Press enter key to continue")
                break
            except ConnectionError:
                print(f"{w}[{y}-{w}] Failed getting header from {self.uniformresourcelocator}{r}!\n{chr(0xa)}")
                input(f"{w}[{r}*{w}] Press enter key to continue")
                break
