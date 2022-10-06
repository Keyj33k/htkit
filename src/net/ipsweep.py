#!/usr/bin/env python3

try:
    from subprocess import CalledProcessError
    from subprocess import check_output
    from pyfiglet import figlet_format
    from datetime import datetime
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


def conf_check(addr: str, min_host: int, max_host: int):
    address_split = addr.split(".")
    if len(address_split) != 3:
        print(f"\n{w}[{y}-{w}] Only the first three octets are allowed{r}!")
        return False
    elif min_host <= 0 or min_host >= 252 or max_host <= 0 or max_host >= 253:
        print(f"\n{w}[{y}-{w}] Invalid host config!")
        return False

    for octet in range(3):
        if int(address_split[octet]) <= 0 or int(address_split[octet]) >= 253:
            print(f"\n{w}[{y}-{w}] Octet {address_split[octet]} is invalid{r}!")
            return False


class IPv4Sweep:
    def __init__(self, ipv4_address: str, host_min: int, host_max: int, ping_count: str):
        self.host_min = host_min
        self.host_max = host_max
        self.ping_count = ping_count
        self.ipv4_address = ipv4_address

    def get_status(self):
        while True:
            if conf_check(self.ipv4_address, self.host_min, self.host_max) is False: break
            print(f"\n{w}[{r}*{w}] Started scanning at{r}:{w}\t{datetime.now()}\n{r}{'=' * 70}")
            start = datetime.now()

            for icmp_request in range(self.host_min, self.host_max + 1):
                ip_address = f"{self.ipv4_address}.{str(icmp_request)}"

                try:
                    check_output(["ping", "-c", self.ping_count, ip_address])
                    print(f"{w}[{g}+{w}] Host {ip_address} is reachable{r}!")
                except KeyboardInterrupt:
                    print(f"{w}[{y}-{w}] You pressed Ctrl+C{r}.{w} Interrupted!")
                    break
                except CalledProcessError:
                    print(f"{w}[{y}-{w}] Host {ip_address} is not reachable{r}!")

            print(f"{r}{'=' * 70}\n{w}[{r}*{w}] Scanner done in {datetime.now() - start}{r}!\n{chr(0xa)}")
            input(f"{w}[{r}*{w}] Press enter key to continue")
            break
