#!/usr/bin/env python3

try:
    from requests import get, ConnectionError
    from time import sleep
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


class SubdomainScanner:
    def __init__(self, uniformresourcelocator: str, wordlist: str):
        self.wordlist = wordlist
        self.uniformresourcelocator = uniformresourcelocator

    def main(self):
        def scanner(database):
            with open(database, "r") as file:
                print(f"\n{w}[{r}*{w}] Start scanning for subdomains from {self.uniformresourcelocator} {r}...")
                print(f"\n{w}[{r}*{w}] Be patient{r},{w} It may take some time {r}...")
                print(f"{r}=" * 70)

                for list_domains in file.read().splitlines():
                    uniformresourcelocator = f"http://{list_domains}.{self.uniformresourcelocator}"
                    sleep(0.5)

                    try:
                        get(uniformresourcelocator)
                        print(f"{w}[{g}+{w}] Discovered {r}->{w} {uniformresourcelocator}")
                    except ConnectionError:
                        pass

        while True:
            if self.wordlist == "exit" or self.wordlist == 'x':
                break

            try:
                if self.wordlist == "":
                    scanner("subdomains.txt")
                else:
                    scanner(self.wordlist)

                print(f"{r}{'=' * 70}\n{chr(0xa)}")
                input(f"{w}[{r}*{w}] Press enter key to continue")
                break
            except FileNotFoundError:
                print(f"{w}[{y}-{w}] You need the subdomain file in the current directory to run this tool{r}.")
                break
            except KeyboardInterrupt:
                print(f"{w}[{r}*{w}] You pressed Ctrl+C{r}.{w} Exit{r}.")
                break
