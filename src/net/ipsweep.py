#!/usr/bin/env python3

try:
    from subprocess import CalledProcessError
    from subprocess import check_output
    from pyfiglet import figlet_format
    from datetime import datetime
    from src.conf_checks.conf import Conf
    from src.colors.coloring import W, R, Y, G
except ImportError:
    raise RuntimeError("""
    Oops,

    this tool uses important modules, which don't seem to be 
    installed at the moment.

    Use the requirements file and this command:
    "pip3 install -r requirements.txt" 

    You will find this file in the req directory.
    """)

def count_config(ip_address: str, ping_count: str):
    check_output(["ping", "-c", ping_count, ip_address])

class IPv4Sweep:
    def __init__(self, ipv4_address: str, host_min: int, host_max: int, ping_count: str):
        self.host_min = host_min
        self.host_max = host_max
        self.ping_count = ping_count
        self.ipv4_address = ipv4_address

    def get_status(self):
        while True:
            if Conf.octets(self.ipv4_address, 3) is False or Conf.hosts(self.host_min, self.host_max) is False: break
            print(f"{W}[{R}*{W}] Scanning host range {R}...{W}")
            start = datetime.now()
            active_hosts, host_count, inactive_hosts = 0, 0, 0
            for icmp_request in range(self.host_min, self.host_max + 1):
                ip_address = f"{self.ipv4_address}.{str(icmp_request)}"
                host_count += 1
                try:
                    if self.ping_count == "":
                        count_config(ip_address, "2")
                    else:
                        count_config(ip_address, str(self.ping_count))

                    print(f"{W}[{G}+{W}] Host {ip_address} is reachable{R}!")
                    active_hosts += 1
                except CalledProcessError:
                    inactive_hosts += 1
                except KeyboardInterrupt:
                    print(f"{W}[{Y}-{W}] You pressed Ctrl{R}+{W}C{R}.{W} Interrupted!")
                    break
            print(f"{W}[{R}*{W}] Done{R},{W} runtime{R}:{W} {datetime.now() - start}{R},{W} total{R}:{W} "
                  f"{host_count}{R},{W} active{R}:{W} {active_hosts}{R},{W} inactive{R}:{W} {inactive_hosts}")
            input(f"{W}[{R}*{W}] Press enter key to continue")
            break
