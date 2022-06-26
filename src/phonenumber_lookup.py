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
            print("Request\t\t\tResponse\n" + "=" * 55 + "\n")

            try:
                valid_check = pnmb.parse(self.target_phonenumber)
                finally_valid = pnmb.is_valid_number(valid_check)

                print(f"Validation:\t{finally_valid}")

                phonenumbers_timezone = pnmb.parse(
                    self.target_phonenumber,
                    "en"
                )
                final_timezone = tz.time_zones_for_number(phonenumbers_timezone)

                print(f"Timezone:\t{final_timezone}")

                phonenumbers_location = pnmb.parse(
                    self.target_phonenumber,
                    "CH"
                )
                final_phonenumbers_location = gc.description_for_number(
                    phonenumbers_location,
                    "en"
                )

                print(f"Location:\t{final_phonenumbers_location}")

                phonenumbers_provider = pnmb.parse(
                    self.target_phonenumber,
                    "RO"
                )
                final_phonenumbers_provider = cr.name_for_number(
                    phonenumbers_provider,
                    "en"
                )

                print(f"Provider:\t{final_phonenumbers_provider}")

                time_stop = dtt.now()
                time_result = time_stop - time_start

                print("\n" + "=" * 55)
                print(f"Job done in {time_result}")
                print("=" * 55)
                input("Press enter key to continue")

                break

            except Exception as error:
                print(cld(
                    "An error was defined!",
                    "red"
                ))

                print(error)
                input("Press enter key to continue")

            print(chr(0xa))
            input("Press enter key to continue")

            break
