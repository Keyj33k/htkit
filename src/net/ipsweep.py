#!/usr/bin/env python3

try:
    from subprocess import CalledProcessError
    from subprocess import check_output
    from pyfiglet import figlet_format
    from datetime import datetime
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

W = "\033[0;37m"
G = "\033[0;32m"
R = "\033[0;31m"
Y = "\033[0;33m"


class IPv4Sweep:
    def __init__(self, ipv4_address: str, host_min: int, host_max: int, ping_count: str):
        self.host_min = host_min
        self.host_max = host_max
        self.ping_count = ping_count
        self.ipv4_address = ipv4_address

    def get_status(self):
        while True:
            if Conf.octets(self.ipv4_address, 3) is False or Conf.hosts(self.host_min, self.host_max) is False: break
            print(f"\n{W}[{R}*{W}] Started scanning at{R}:{W}\t{datetime.now()}\n{R}{'=' * 70}")
            start = datetime.now()

            for icmp_request in range(self.host_min, self.host_max + 1):
                ip_address = f"{self.ipv4_address}.{str(icmp_request)}"

                try:
                    check_output(["ping", "-c", self.ping_count, ip_address])
                    print(f"{W}[{G}+{W}] Host {ip_address} is reachable{R}!")
                except KeyboardInterrupt:
                    print(f"{W}[{Y}-{W}] You pressed Ctrl+C{R}.{W} Interrupted!")
                    break
                except CalledProcessError:
                    print(f"{W}[{Y}-{W}] Host {ip_address} is not reachable{R}!")

            print(f"{R}{'=' * 70}\n{W}[{R}*{W}] Scanner done in {datetime.now() - start}{R}!\n{chr(0xa)}")
            input(f"{W}[{R}*{W}] Press enter key to continue")
            break
