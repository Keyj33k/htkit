#!/usr/bin/env python3

try:
    from requests import get, ConnectionError
    from time import sleep
    from src.utils.coloring import W, R, Y, G
except ImportError:
    raise RuntimeError("""
    Oops,

    this tool uses important modules, which don't seem to be 
    installed at the moment.

    Use the requirements file and this command:
    "pip3 install -r requirements.txt" 

    You will find this file in the req directory.
    """)

def scanner(database: str, uniformresourcelocator: str):
    with open(database, 'r') as file:
        print(f"{W}[{R}*{W}] Sending GET requests {R}...\n"
              f"{W}[{Y}!{W}] Be patient{R},{W} It may take some time {R}...")
        for list_domains in file.read().splitlines():
            build_url = f"http://{list_domains}.{uniformresourcelocator}"
            sleep(0.75)
            try:
                print(f"{W}[{G}+{W}] {build_url}\t{R}[{W} {get(build_url).status_code} {R}]{W}")
            except ConnectionError:
                pass

class SubdomainScanner:
    def __init__(self, url: str, wordlist: str):
        self.url = url
        self.wordlist = wordlist

    def main(self):
        while True:
            try:
                scanner("htkit/subdomains.txt", self.url) if self.wordlist == "" else scanner(self.wordlist, self.url)
                input(f"{W}[{R}*{W}] Press enter key to continue")
                break
            except FileNotFoundError:
                print(f"{W}[{Y}-{W}] You need the subdomain file in the current directory to run this tool{R}.")
                break
            except KeyboardInterrupt:
                print(f"{W}[{R}*{W}] You pressed Ctrl{R}+{W}C{R}.{W} Exit{R}.")
                break
