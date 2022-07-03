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


class IPv4Sweep:

    def __init__(
            self,
            ipv4_address: str,
            min_range: int,
            max_range: int

    ):
        self.min_range = min_range
        self.max_range = max_range
        self.ipv4_address = ipv4_address

    def get_status(self):
        mod_ipv4_address = self.ipv4_address.split(".")
        remove_last_octet = mod_ipv4_address[0] + "." + \
                            mod_ipv4_address[1] + "." + \
                            mod_ipv4_address[2] + "."

        for icmp_request in range(
                self.min_range,
                self.max_range + 1
        ):
            try:
                check_output([
                    "ping", "-c", "2",
                    remove_last_octet + str(icmp_request)
                ])

                print(f"\033[0;37m[\033[0;32m+\033[0;37m] Host {remove_last_octet + str(icmp_request)} is reachable")

            except KeyboardInterrupt:
                print("\033[0;37m[\033[0;33m-\033[0;37m] You pressed Ctrl+C.INTERRUPTED!")

                break

            except CalledProcessError:
                print(
                    f"\033[0;37m[\033[0;33m-\033[0;37m] Host {remove_last_octet + str(icmp_request)} is not reachable"
                )

        print("\033[0;37m[\033[0;31m*\033[0;37m] Done")
        input("\nPress enter key to continue")


