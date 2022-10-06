#!/usr/bin/env python3

try:
    from datetime import datetime as dtt
    from termcolor import colored as cld
    from socket import error, AF_INET, SOCK_STREAM, socket, getservbyport
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

def output(port: int, service: str):
    print(f"TCP\t\t{port}  \t\topen\t{service}")

class WitcherPortscanner:
    def __init__(self, target_ipv4: str, start_port: int, maximum_port: int):
        self.start_port = start_port
        self.target_ipv4 = target_ipv4
        self.maximum_port = maximum_port

    def main(self):
        while True:
            if self.start_port <= 0 or self.start_port >= 65534:
                print(f"\n{w}[{y}-{w}] Port {self.start_port} is invalid{r}!")
                break
            elif self.maximum_port <= 1 or self.maximum_port >= 65535:
                print(f"\n{w}[{y}-{w}] Port {self.maximum_port} is invalid{r}!")
                break

            time_start = dtt.now()
            print(f"\n{w}[{r}*{w}] Started scanning at{r}:{w}\t{time_start}\n{r}{'=' * 70}")
            print(f"{w}Protocol\tPort\t\tStatus\t Service\n{'-' * 70}")

            try:
                for target_port in range(self.start_port, self.maximum_port + 1):
                    with socket(AF_INET, SOCK_STREAM) as socket_sock:
                        socket_sock.settimeout(5)
                        if socket_sock.connect_ex((self.target_ipv4, target_port)) == 0:
                            try:
                                output(target_port, getservbyport(target_port))
                            except OSError:
                                output(target_port, "unknown")
                print(f"{r}{'=' * 70}\n{w}[{r}*{w}] Scanner done in {dtt.now() - time_start}!\n{chr(0xa)}")
                input(f"{w}[{r}*{w}] Press enter key to continue")
                break
            except error as socket_error:
                print(cld(socket_error, "red"))
                break
            except KeyboardInterrupt:
                print(f"\n{w}[{y}-{w}] Ctrl+C pressed{r}.{w} Exit{r}.")
                break
