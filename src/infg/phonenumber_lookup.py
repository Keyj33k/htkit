#!/usr/bin/env python3

try:
    from datetime import datetime as dtt
    from phonenumbers import timezone as tz
    from phonenumbers import geocoder as gc
    from phonenumbers import carrier as cr
    import phonenumbers as pnmb
    from termcolor import colored as cld
    
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


class PhonenumberWhois:

    def __init__(
            self,
            target_phonenumber: str
    ):
        self.target_phonenumber = target_phonenumber

    def main(self):
        while True:
            if self.target_phonenumber == 'x' or self.target_phonenumber == 'exit':
                break

            time_start = dtt.now()

            print("=" * 55)
            print(f"{w}[{g}+{w}] Request\t\tResponse\n" + "=" * 55)

            try:
                phonenumber_val = pnmb.is_valid_number(pnmb.parse(self.target_phonenumber))
                national = pnmb.format_number(pnmb.parse(
                    self.target_phonenumber),
                    pnmb.PhoneNumberFormat.NATIONAL
                )
                international = pnmb.format_number(
                    pnmb.parse(self.target_phonenumber),
                    pnmb.PhoneNumberFormat.INTERNATIONAL
                )
                phonenumbers_ = pnmb.parse(
                    self.target_phonenumber,
                    None
                )
                final_timezone = tz.time_zones_for_number(phonenumbers_)
                final_phonenumbers_location = gc.description_for_number(
                    phonenumbers_,
                    "en"
                )
                final_phonenumbers_provider = cr.name_for_number(
                    phonenumbers_,
                    "en"
                )

                print(f"{w}[{g}+{w}] Validation:\t\t{phonenumber_val}")
                print(f"{w}[{g}+{w}] National:\t\t{national}")
                print(f"{w}[{g}+{w}] International:\t{international}")
                print(f"{w}[{g}+{w}] Timezone:\t\t{final_timezone}")
                print(f"{w}[{g}+{w}] Location:\t\t{final_phonenumbers_location}")
                print(f"{w}[{g}+{w}] Provider:\t\t{final_phonenumbers_provider}")
                
                time_stop = dtt.now()
                time_result = time_stop - time_start

                print("=" * 55)
                print(f"{w}[{g}+{w}] Job done in {time_result}")
                print("=" * 55)
                print(chr(0xa))
                input(f"{w}[{r}*{w}] Press enter key to continue")
                break
            except Exception as error:
                print(cld(
                    "An error was defined!",
                    "red"
                ))
                print(error)
                input(f"{w}[{r}*{w}] Press enter key to continue")
                break
