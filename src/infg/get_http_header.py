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


class GetHTTPHeader:

    def __init__(
            self,
            uniformresourcelocator: str
    ):
        self.uniformresourcelocator = uniformresourcelocator

    def main(self):
        while True:
            if self.uniformresourcelocator == 'x' or self.uniformresourcelocator == 'exit':
                break

            print("\033[0;37m[\033[0;32m+\033[0;37m] Result:")
            print("\033[0;37m=" * 70)

            try:
                subprocess.call([
                    "curl", "-I",
                    self.uniformresourcelocator
                ])

                print("\033[0;37m=" * 70)
                print(chr(0xa))
                input("\033[0;37m[\033[0;31m*\033[0;37m] Press enter key to continue")

                break
                
            except subprocess.CalledProcessError:
                print(f"\033[0;37m[\033[0;31m*\033[0;37m] Failed getting header from {self.uniformresourcelocator}")

                print(chr(0xa))
                input("\033[0;37m[\033[0;31m*\033[0;37m] Press enter key to continue")

                break


