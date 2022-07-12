#!/usr/bin/env python3

try:
    from datetime import datetime as dtt
    from termcolor import colored as cld
    import requests
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
#   Version :   1.1.6                     #
#                                         #
# # # # # # # # # # # # # # # # # # # # # #


class IPv4Lookup:

    def __init__(
            self,
            ipv4_address: str
    ):
        self.ipv4_address = ipv4_address

    def main(self):
        while True:
            if self.ipv4_address == 'x' or self.ipv4_address == 'exit':
                break

            time_start = dtt.now()
            print("\033[0;37m[\033[0;32m+\033[0;37m] Results:")

            try:
                response = requests.post(
                    "http://ip-api.com/batch",
                    json=[{"query": self.ipv4_address}]
                ).json()

                print("=" * 70)

                for lookup in response:
                    for k, j in lookup.items():
                        print("\033[0;37m[\033[0;32m+\033[0;37m] " + k, j)

                time_stop = dtt.now()
                time_result = time_stop - time_start

                print("=" * 70)
                print(f"\033[0;37m[\033[0;32m+\033[0;37m] Scanner done in {time_result}!")
                print(chr(0xa))
                input("\033[0;37m[\033[0;31m*\033[0;37m] Press enter key to continue")
                break
            except Exception as error:
                print(cld(
                    f"An error was defined! {error}",
                    "red"
                ))
                input("\033[0;37m[\033[0;31m*\033[0;37m] Press enter key to continue")
                break




