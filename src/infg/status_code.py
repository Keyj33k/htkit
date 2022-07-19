#!/usr/bin/env python3

try:
    from datetime import datetime
    import requests
    import urllib3
    import socket
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


class RemoteServerStatusCode:

    def __init__(
            self,
            uniformresourcelocator: str
    ):
        self.uniformresourcelocator = uniformresourcelocator

    def get_code(self):
        while True:
            try:
                request_ = urllib3.PoolManager().request("GET", self.uniformresourcelocator)
                print(f"\n{w}[{r}*{w}] Getting the status code from {self.uniformresourcelocator} ...\n" + "=" * 70)

                time.sleep(1.25)

                print(f"{w}[{g}+{w}] Status Code From {self.uniformresourcelocator} -> {request_.status}")
                print("=" * 70)
                input(f"\n{w}[{r}*{w}] Press enter key to continue")
                break
            except KeyboardInterrupt:
                print(f"\n{w}[{r}*{w}] You pressed Ctrl+C. Exit.")
                break
            except Exception as excerr:
                print(excerr)
                break

