#!/usr/bin/env python3

try:
    from datetime import datetime
    from phonenumbers import timezone
    from phonenumbers import geocoder
    from phonenumbers import carrier
    import phonenumbers
    from time import sleep
    from src.utils.coloring import W, R, Y, G
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
    def __init__(self, target_phonenumber: str):
        self.target_phonenumber = target_phonenumber

    def main(self):
        while True:
            time_start = datetime.now()
            print(f"{W}[{R}*{W}] Collecting values {R}...")

            try:
                phonenumber_val = phonenumbers.is_valid_number(phonenumbers.parse(self.target_phonenumber))
                national = phonenumbers.format_number(phonenumbers.parse(self.target_phonenumber),
                                                      phonenumbers.PhoneNumberFormat.NATIONAL)
                international = phonenumbers.format_number(phonenumbers.parse(self.target_phonenumber),
                                                           phonenumbers.PhoneNumberFormat.INTERNATIONAL)
                phonenumbers_ = phonenumbers.parse(self.target_phonenumber, None)
                final_timezone = timezone.time_zones_for_number(phonenumbers_)
                final_phonenumbers_location = geocoder.description_for_number(phonenumbers_, "en")
                final_phonenumbers_provider = carrier.name_for_number(phonenumbers_, "en")
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

                print(f"{W}[{R}*{W}] Done, runtime{R}:{W} {datetime.now() - time_start}")
                input(f"{W}[{R}*{W}] Press enter key to continue")
                break
            except Exception as error:
                print(f"{W}[{Y}-{W}] Error{R}:{W} {error}")
                break
