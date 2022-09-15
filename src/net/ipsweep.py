#!/usr/bin/env python3

try:
    from subprocess import CalledProcessError
    from subprocess import check_output
    from pyfiglet import figlet_format
    from datetime import datetime
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

w = "\033[0;37m"
g = "\033[0;32m"
r = "\033[0;31m"
y = "\033[0;33m"


class IPv4Sweep:

    def __init__(self, ipv4_address: str, min_range: int, max_range: int, ping_count: str):
        self.ping_count = ping_count
        self.min_range = min_range
        self.max_range = max_range
        self.ipv4_address = ipv4_address

    def get_status(self):
        print(f"\n{w}[{r}*{w}] Started scanning at{r}:{w}\t{datetime.now()}")
        print(f"{r}=" * 70)

        start = datetime.now()

        for icmp_request in range(self.min_range, self.max_range + 1):
            ip_address = f"{self.ipv4_address}.{str(icmp_request)}"
            try:
                check_output(["ping", "-c", self.ping_count, ip_address])
                print(f"{w}[{g}+{w}] Host {ip_address} is reachable{r}!")
            except KeyboardInterrupt:
                print(f"{w}[{y}-{w}] You pressed Ctrl+C{r}.{w} Interrupted!")
                break
            except CalledProcessError:
                print(f"{w}[{y}-{w}] Host {ip_address} is not reachable{r}!")

        end = datetime.now()

        print(f"{r}=" * 70)
        print(f"{w}[{r}*{w}] Scanner done in {end - start}{r}!")
        print(chr(0xa))
        input(f"{w}[{r}*{w}] Press enter key to continue")



