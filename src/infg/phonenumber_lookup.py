#!/usr/bin/env python3

try:
    from datetime import datetime as dtt
    from phonenumbers import timezone as tz
    from phonenumbers import geocoder as gc
    from phonenumbers import carrier as cr
    import phonenumbers as pnmb
    from time import sleep
except ImportError:
    raise RuntimeError("""
    Oops,

    this tool uses important modules, which don't seem to be 
    installed at the moment.

    Use the requirements file and this command:
    "pip3 install -r requirements.txt" 

    You will find this file in the req directory.
    """)

W = "\033[0;37m"
G = "\033[0;32m"
R = "\033[0;31m"
Y = "\033[0;33m"


class PhonenumberWhois:
    def __init__(self, target_phonenumber: str):
        self.target_phonenumber = target_phonenumber

    def main(self):
        while True:
            time_start = dtt.now()
            print(f"{W}[{R}*{W}] Collecting values {R}...")

            try:
                phonenumber_val = pnmb.is_valid_number(pnmb.parse(self.target_phonenumber))
                national = pnmb.format_number(pnmb.parse(self.target_phonenumber), pnmb.PhoneNumberFormat.NATIONAL)
                international = pnmb.format_number(
                    pnmb.parse(self.target_phonenumber),
                    pnmb.PhoneNumberFormat.INTERNATIONAL
                )
                phonenumbers_ = pnmb.parse(self.target_phonenumber, None)
                final_timezone = tz.time_zones_for_number(phonenumbers_)
                final_phonenumbers_location = gc.description_for_number(phonenumbers_, "en")
                final_phonenumbers_provider = cr.name_for_number(phonenumbers_, "en")

                output = [
                    f"Validation{R}:{W} {phonenumber_val}",
                    f"National{R}:{W} {national}",
                    f"International{R}:{W} {international}",
                    f"Timezone{R}:{W} {final_timezone}",
                    f"Location{R}:{W} {final_phonenumbers_location}",
                    f"Provider{R}:{W} {final_phonenumbers_provider}"
                ]

                for results in output:
                    sleep(0.25)
                    print(f"{W}[{G}+{W}] {results}")

                print(f"{W}[{R}*{W}] Done, runtime{R}:{W} {dtt.now() - time_start}")
                input(f"{W}[{R}*{W}] Press enter key to continue")
                break
            except Exception as error:
                print(f"{W}[{Y}-{W}] Error{R}:{W} {error}")
                break
