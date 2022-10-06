#!/usr/bin/env python3

try:
    from datetime import datetime as dtt
    from termcolor import colored as cld
    from requests import post, RequestException
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

def config_check(ip_addr: str):
    split_address = ip_addr.split(".")
    if len(split_address) != 4:
        print(f"\n{w}[{y}-{w}] You need to enter a valid 32 bit address{r}!")
        return False

    for octet in range(4):
        if int(split_address[octet]) <= 0 or int(split_address[octet]) >= 253:
            print(f"\n{w}[{y}-{w}] Octet {octet + 1} ( {split_address[octet]} ) is invalid{r}!")
            return False

class IPv4Lookup:
    def __init__(self, ipv4_address: str):
        self.ipv4_address = ipv4_address

    def main(self):
        while True:
            if config_check(self.ipv4_address) is False: break
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
