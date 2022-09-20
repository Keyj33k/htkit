#!/usr/bin/env python3

try:
    from datetime import datetime as dtt
    from termcolor import colored as cld
    import time
    from socket import socket, AF_INET, SOCK_STREAM, error
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


class BannerGrabber:
    def __init__(self, target_address: str, target_port: int):
        self.target_address = target_address
        self.target_port = target_port

    def main(self):
        while True:
            if self.target_address == 'x' or self.target_address == 'exit':
                break
            elif self.target_port == 0:
                break

            try:
                with socket(AF_INET, SOCK_STREAM) as socket_sock:
                    socket_sock.connect_ex((self.target_address, self.target_port))
                    socket_sock.settimeout(5)
                    service = socket_sock.recv(1024).decode()
                    
                    print(f"\n{w}[{r}*{w}] Start scanning {self.target_address} at {dtt.now()}")
                    time.sleep(1.5)
                    print(f"{r}=" * 70)
                    print(f"{w}[{g}+{w}] Port {self.target_port} {r}->{w} {service}" + f"{r}=" * 70)
                    print(chr(0xa))
                    input(f"{w}[{r}*{w}] Press enter key to continue")
                break
            except error as sockerr:
                print(cld(sockerr, "red"))
                break

