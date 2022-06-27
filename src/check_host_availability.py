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
#   Version :   1.1.5                     #
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

            ping_request = subprocess.check_output([
                "ping",
                "-c",
                "3",
                self.target_address
            ])

            if not ping_request:
                print(f"Host {self.target_address} seems to be dead ...")
            else:
                print(f"Host {self.target_address} is alive!")

            input("Press any key to continue")

            break
