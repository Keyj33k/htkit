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
    
# # # # # # # # # # # # # # # # # # # # # #
#                                         #
#   Author  :   Keyjeek                   #
#   Contact :   nomotikag33n@gmail.com    #
#   Github  :   @Keyj33k                  #
#   Version :   1.1.9                     #
#                                         #
# # # # # # # # # # # # # # # # # # # # # #

w = "\033[0;37m"
g = "\033[0;32m"
r = "\033[0;31m"
y = "\033[0;33m"


class SubdomainScanner:

    def __init__(
            self,
            uniformresourcelocator: str,
            wordlist: str
    ):
        self.wordlist = wordlist
        self.uniformresourcelocator = uniformresourcelocator

    def main(self):
        while True:
            found_subdomain = []
            if self.uniformresourcelocator == 'exit' or self.uniformresourcelocator == 'x':
                break

            try:
                if self.wordlist == "":
                    with open("subdomains.txt", "r") as FILE:
                        read_file = FILE.read()
                        subdomain = read_file.splitlines()

                        for list_domains in subdomain:
                            uniformresourcelocator = f"http://{list_domains}.{self.uniformresourcelocator}"
                            time.sleep(0.5)

                            try:
                                requests.get(uniformresourcelocator)
                            except requests.ConnectionError:
                                pass
                            else:
                                print(f"{w}[{g}+{w}] Discovered -> {uniformresourcelocator}")
                                found_subdomain.append(uniformresourcelocator)
                else:
                    with open(f"{self.wordlist}", "r") as FILE:
                        read_file = FILE.read()
                        subdomain = read_file.splitlines()

                        for list_domains in subdomain:
                            uniformresourcelocator = f"http://{list_domains}.{self.uniformresourcelocator}"
                            time.sleep(0.5)

                            try:
                                requests.get(uniformresourcelocator)
                            except requests.ConnectionError:
                                pass
                            else:
                                print(f"{w}[{g}+{w}] Discovered -> {uniformresourcelocator}")
                                found_subdomain.append(uniformresourcelocator)

                input(f"{w}[{r}*{w}] Press enter key to continue")
                break
            except FileNotFoundError:
                print(f"{w}[{y}-{w}] You need the subdomain file in the current directory to run this tool.")
                break
            except KeyboardInterrupt:
                print(f"{w}[{r}*{w}] You pressed Ctrl+C. Exit.")
                break


