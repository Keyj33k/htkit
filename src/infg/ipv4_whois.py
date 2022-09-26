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


class IPv4Lookup:
    def __init__(self, ipv4_address: str):
        self.ipv4_address = ipv4_address

    def main(self):
        while True:
            split_address = self.ipv4_address.split(".")
            if len(split_address) != 4:
                print(f"\n{w}[{y}-{w}] You need to enter a valid 32 bit address{r}!")
                break
            elif int(split_address[0]) <= 0 or int(split_address[0]) >= 253:
                print(f"\n{w}[{y}-{w}] Octet 1 ( {split_address[0]} ) is invalid{r}!")
                break
            elif int(split_address[1]) <= 0 or int(split_address[1]) >= 253:
                print(f"\n{w}[{y}-{w}] Octet 2 ( {split_address[1]} ) is invalid{r}!")
                break
            elif int(split_address[2]) <= 0 or int(split_address[2]) >= 253:
                print(f"\n{w}[{y}-{w}] Octet 3 ( {split_address[2]} ) is invalid{r}!")
                break
            elif int(split_address[3]) <= 0 or int(split_address[3]) >= 253:
                print(f"\n{w}[{y}-{w}] Octet 4 ( {split_address[3]} ) is invalid{r}!")
                break

            time_start = dtt.now()
            print(f"\n{w}[{r}*{w}] Results{r}:\n{'=' * 70}")

            try:
                for lookup in post("http://ip-api.com/batch", json=[{"query": self.ipv4_address}]).json():
                    for k, j in lookup.items():
                        print(f"{w}[{g}+{w}] " + k, j)

                time_stop = dtt.now()
                time_result = time_stop - time_start

                print(f"{r}=" * 70)
                print(f"{w}[{r}*{w}] Scanner done in {time_result}!")
                print(chr(0xa))
                input(f"{w}[{r}*{w}] Press enter key to continue")
                break
            except RequestException as error:
                print(cld(str(error), "red"))
                input(f"{w}[{g}+{w}] Press enter key to continue")
                break

