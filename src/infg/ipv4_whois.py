#!/usr/bin/env python3

try:
    from datetime import datetime as dtt
    from termcolor import colored as cld
    from requests import post, RequestException
    from src.conf_checks.conf import Conf
except ImportError:
    raise RuntimeError("""
    Oops,

    this tool uses important modules, which don't seem to be 
    installed at the moment.

    Use the requirements file and this command:
    "pip3 install -r requirements.txt" 

    You will find this file in the req directory.
    """)

w = "\033[0;37m"
g = "\033[0;32m"
r = "\033[0;31m"
y = "\033[0;33m"

class IPv4Lookup:
    def __init__(self, ipv4_address: str):
        self.ipv4_address = ipv4_address

    def main(self):
        while True:
            if Conf.octets(self.ipv4_address, 4) is False: break
            time_start = dtt.now()
            print(f"\n{w}[{r}*{w}] Results{r}:\n{'=' * 70}")

            try:
                for lookup in post("http://ip-api.com/batch", json=[{"query": self.ipv4_address}]).json():
                    for category, result in lookup.items():
                        print(f"{w}[{g}+{w}] {category}: {result}")

                print(f"{r}{'=' * 70}\n{w}[{r}*{w}] Scanner done in {dtt.now() - time_start}!")
                input(f"{chr(0xa)}\n{w}[{r}*{w}] Press enter key to continue")
                break
            except RequestException as error:
                print(cld(str(error), "red"))
                input(f"{w}[{g}+{w}] Press enter key to continue")
                break
