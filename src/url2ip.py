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
#   Version :   1.1.5                     #
#                                         #
# # # # # # # # # # # # # # # # # # # # # #


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
                print(f"IP Address from {self.uniformresourcelocator}: " + socket.gethostbyname(self.uniformresourcelocator))
                input("\nPress enter key to continue")

                break

            except ValueError:
                print("\nYou need to enter a value like: google.com in example.")
                input("Press any key to continue")

            except socket.gaierror:
                print("\nYou need to enter a value like: google.com in example.")
                input("Press any key to continue")

