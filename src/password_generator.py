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
#   Version :   1.1.5                     #
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

            print(f"Your generated password: {finalpassword}\n")
            input("Press enter key to continue")

            break




