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
    
# # # # # # # # # # # # # # # # # # # # # #
#                                         #
#   Author  :   Keyjeek                   #
#   Contact :   nomotikag33n@gmail.com    #
#   Github  :   @Keyj33k                  #
#   Version :   1.1.9                     #
#                                         #
# # # # # # # # # # # # # # # # # # # # # #

w = "\033[0;37m"
g = "\033[0;32m"
r = "\033[0;31m"
y = "\033[0;33m"


class IPv4Sweep:

    def __init__(
            self,
            ipv4_address: str,
            min_range: int,
            max_range: int,
            ping_count: str

    ):
        self.ping_count = ping_count
        self.min_range = min_range
        self.max_range = max_range
        self.ipv4_address = ipv4_address

    def get_status(self):
        mod_ipv4_address = self.ipv4_address.split(".")
        remove_last_octet = mod_ipv4_address[0] + "." + \
                            mod_ipv4_address[1] + "." + \
                            mod_ipv4_address[2] + "."

        print(f"\n{w}[{g}+{w}] Started scanning at:\t{datetime.now()}")
        print("=" * 70)

        start = datetime.now()

        for icmp_request in range(
                self.min_range,
                self.max_range + 1
        ):
            try:
                check_output([
                    "ping", "-c", self.ping_count,
                    remove_last_octet + str(icmp_request)
                ])

                print(f"{w}[{g}+{w}] Host {remove_last_octet + str(icmp_request)} is reachable")
            except KeyboardInterrupt:
                print(f"{w}[{y}-{w}] You pressed Ctrl+C.INTERRUPTED!")
                break
            except CalledProcessError:
                print(f"{w}[{y}-{w}] Host {remove_last_octet + str(icmp_request)} is not reachable")

        end = datetime.now()

        print("=" * 70)
        print(f"{w}[{g}+{w}] Scanner done in {end - start}!")
        print("\033[0;37m=" * 70)
        print(chr(0xa))
        input(f"{w}[{r}*{w}] Press enter key to continue")


