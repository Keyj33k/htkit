#!/usr/bin/env python3

try:
    from datetime import datetime as dtt
    from termcolor import colored as cld
    from socket import error, AF_INET, SOCK_STREAM, socket, getservbyport
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

class WitcherPortscanner:
    def __init__(self, target_ipv4: str, start_port: int, maximum_port: int):
        self.start_port = start_port
        self.target_ipv4 = target_ipv4
        self.maximum_port = maximum_port

    @staticmethod
    def output(port: int, service: str):
        print(f"\tTCP\t\t{port}  \t\topen\t{service}")

    def main(self):
        while True:
            if Conf.ports(self.start_port, self.maximum_port) is False: break
            time_start = dtt.now()
            print(f"{W}[{R}*{W}] Start port scan {R}...\n\n"
                  f"\t{W}Protocol\tPort\t\tStatus\tService\n"
                  f"\t{'-' * 8}\t{'-' * 4}\t\t{'-' * 6}\t{'-' * 7}")
            open_ports = 0

            try:
                for target_port in range(self.start_port, self.maximum_port + 1):
                    with socket(AF_INET, SOCK_STREAM) as socket_sock:
                        socket_sock.settimeout(5)
                        if socket_sock.connect_ex((self.target_ipv4, target_port)) == 0:
                            open_ports += 1
                            try:
                                WitcherPortscanner.output(target_port, getservbyport(target_port))
                            except OSError:
                                WitcherPortscanner.output(target_port, "unknown")

                total = self.maximum_port - self.start_port
                closed_ports = total - open_ports
                print(f"\n{W}[{R}*{W}] Done, runtime{R}:{W} {dtt.now() - time_start}{R},{W} "
                      f"total{R}:{W} {total}{R},{W} open{R}:{W} {open_ports}{R},{W} closed{R}:{W} {closed_ports}")
                input(f"{W}[{R}*{W}] Press enter key to continue")
                break
            except error as socket_error:
                print(f"{W}[{Y}-{W}] Error{R}:{W} {socket_error}")
                break
            except KeyboardInterrupt:
                print(f"\n{W}[{Y}-{W}] Ctrl{R}+{W}C pressed{R}.{W} Exit{R}.")
                break
