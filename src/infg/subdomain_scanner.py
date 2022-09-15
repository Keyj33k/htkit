#!/usr/bin/env python3

try:
    import requests
    import time
    import os
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
        while True:
            found_subdomain = []

            if self.wordlist == 'exit' or self.wordlist == 'x':
                break

            try:
                if self.wordlist == "":
                    with open("subdomains.txt", "r") as FILE:
                        read_file = FILE.read()
                        subdomain = read_file.splitlines()

                        print(f"\n{w}[{r}*{w}] Start scanning for subdomains from {self.uniformresourcelocator} {r}...")
                        print(f"{w}[{r}*{w}] Be patient{r},{w} It may take some time {r}...")
                        print(f"{r}=" * 70)

                        for list_domains in subdomain:
                            uniformresourcelocator = f"http://{list_domains}.{self.uniformresourcelocator}"
                            time.sleep(0.5)

                            try:
                                requests.get(uniformresourcelocator)
                            except requests.ConnectionError:
                                pass
                            else:
                                print(f"{w}[{g}+{w}] Discovered {r}->{w} {uniformresourcelocator}")
                                found_subdomain.append(uniformresourcelocator)
                else:
                    with open(f"{self.wordlist}", "r") as FILE:
                        read_file = FILE.read()
                        subdomain = read_file.splitlines()

                        print(f"\n{w}[{r}*{w}] Start scanning for subdomains from {self.uniformresourcelocator} {r}...")
                        print(f"{w}[{r}*{w}] Be patient, It may take some time {r}...")
                        print(f"{r}=" * 70)

                        for list_domains in subdomain:
                            uniformresourcelocator = f"http://{list_domains}.{self.uniformresourcelocator}"
                            time.sleep(0.5)

                            try:
                                requests.get(uniformresourcelocator)
                            except requests.ConnectionError:
                                pass
                            else:
                                print(f"{w}[{g}+{w}] Discovered {r}->{w} {uniformresourcelocator}")
                                found_subdomain.append(uniformresourcelocator)

                print(f"{r}=" * 70, f"\n{chr(0xa)}")
                input(f"{w}[{r}*{w}] Press enter key to continue")

                break
            except FileNotFoundError:
                print(f"{w}[{y}-{w}] You need the subdomain file in the current directory to run this tool{r}.")

                break
            except KeyboardInterrupt:
                print(f"{w}[{r}*{w}] You pressed Ctrl+C{r}.{w} Exit{r}.")

                break

