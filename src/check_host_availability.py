#!/usr/bin/env python3

try:
    import subprocess
    
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


class CheckHostAvailability:

    def __init__(
            self,
            target_address: str
    ):
        self.target_address = target_address

    def main(self):
        while True:
            if self.target_address == 'x' or self.target_address == 'exit':
                break

            print("\033[0;37m[\033[0;32m+\033[0;37m] Result:")
            print("=" * 70)

            ping_request = subprocess.check_output([
                "ping", "-c", "3",
                self.target_address
            ])

            if not ping_request:
                print(f"\033[0;37m[\033[0;33m-\033[0;37m] Host {self.target_address} seems to be dead ...")
                
            else:
                print(f"\033[0;37m[\033[0;32m+\033[0;37m] Host {self.target_address} is alive!")

            print("=" * 70)

            print(chr(0xa))
            input("\033[0;37m[\033[0;31m*\033[0;37m] Press enter key to continue")

            break
