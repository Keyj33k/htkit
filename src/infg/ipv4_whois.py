#!/usr/bin/env python3

try:
    from datetime import datetime as dtt
    from requests import post, RequestException
    from src.utils.conf import Conf
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

class IPv4Lookup:
    def __init__(self, ipv4_address: str):
        self.ipv4_address = ipv4_address

    def main(self):
        while True:
            if Conf.octets(self.ipv4_address, 4) is False: break
            time_start = dtt.now()
            print(f"{W}[{R}*{W}] Sending api request{R} ...")

            try:
                for lookup in post("http://ip-api.com/batch", json=[{"query": self.ipv4_address}]).json():
                    for category, result in lookup.items():
                        sleep(0.25)
                        print(f"{W}[{G}+{W}] {category}{R}:{W} {result}")
                print(f"{W}[{R}*{W}] Done{R},{W} runtime{R}:{W} {dtt.now() - time_start}")
                input(f"{W}[{R}*{W}] Press enter key to continue")
                break
            except RequestException as error:
                print(f"{W}[{Y}-{W}] Error{R}:{W} {error}")
                break
