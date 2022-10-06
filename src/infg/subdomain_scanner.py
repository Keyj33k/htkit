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


def scanner(database: str, uniformresourcelocator: str):
    with open(database, "r") as file:
        print(f"\n{w}[{r}*{w}] Start scanning for subdomains from {uniformresourcelocator} {r}..."
              f"\n{w}[{r}*{w}] Be patient{r},{w} It may take some time {r}...\n{r}{'=' * 70}")

        for list_domains in file.read().splitlines():
            build_url = f"http://{list_domains}.{uniformresourcelocator}"
            sleep(0.75)

            try:
                print(f"{w}[{g}+{w}] {build_url}:\t{get(build_url).status_code}")
            except ConnectionError:
                pass


class SubdomainScanner:
    def __init__(self, url: str, wordlist: str):
        self.url = url
        self.wordlist = wordlist

    def main(self):
        while True:
            if self.wordlist == "exit" or self.wordlist == 'x': break

            try:
                scanner("subdomains.txt", self.url) if self.wordlist == "" else scanner(self.wordlist, self.url)
                input(f"{r}{'=' * 70}\n{chr(0xa)}\n{w}[{r}*{w}] Press enter key to continue")
                break
            except FileNotFoundError:
                print(f"{w}[{y}-{w}] You need the subdomain file in the current directory to run this tool{r}.")
                break
            except KeyboardInterrupt:
                print(f"{w}[{r}*{w}] You pressed Ctrl+C{r}.{w} Exit{r}.")
                break
