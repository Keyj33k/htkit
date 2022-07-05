#!/usr/bin/env python3

try:
    from termcolor import colored as cld
    import random
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


class PasswordGenerator:

    def __init__(
            self,
            password_length: int
    ):
        self.password_length = password_length

    def main(self):
        while True:
            if self.password_length == 0:
                break
                
            elif self.password_length <= 7:
                print(cld(
                    "Your password should be always bigger than eight characters.",
                    "red"
                ))

                break

            numbers = "1234567890"
            lowers = "abcdefghijklmnopqrstuvwxyz"
            uppers = "ABVDEFGHIJKLMNOPQRSTUVWXYZ"
            special = "§$%&/()=}[{]?!_;:"
            mixer = numbers + lowers + uppers + special
            passw_result = random.sample(
                mixer,
                self.password_length
            )
            finalpassword = ''.join(passw_result)

            print("=" * 70)
            print(f"\033[0;37m[\033[0;32m+\033[0;37m] Your generated password: {finalpassword}")
            print("=" * 70)

            print(chr(0xa))
            input("\033[0;37m[\033[0;31m*\033[0;37m] Press enter key to continue")

            break




