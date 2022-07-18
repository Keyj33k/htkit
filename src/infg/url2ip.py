#!/usr/bin/env python3
import sys

try:
    import socket
    from termcolor import colored as cld
    from pyfiglet import figlet_format
    
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


class GetIPv4fromURL:

    def __init__(
            self,
            uniformresourcelocator: str
    ):
        self.uniformresourcelocator = uniformresourcelocator

    def main(self):
        while True:
            if self.uniformresourcelocator == 'x' or self.uniformresourcelocator == 'exit':
                break

            try:
                print(f"{w}=" * 70)
                print(f"{w}[{g}+{w}] IP Address from {self.uniformresourcelocator} -> " + socket.gethostbyname(self.uniformresourcelocator))
                print(f"{w}=" * 70)
                print(chr(0xa))
                input(f"{w}[{r}*{w}] Press enter key to continue")
                break
            except ValueError:
                print(f"{w}[{y}-{w}] You need to enter a value like: google.com in example.")
                print(chr(0xa))
                input(f"{w}[{r}*{w}] Press enter key to continue")
            except socket.gaierror:
                print(f"\n{w}[{y}-{w}] You need to enter a value like: google.com in example.")
                print(chr(0xa))
                input(f"{w}[{r}*{w}] Press any key to continue")

