#!/usr/bin/env python3

try:
    import time
    from datetime import datetime
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

W = "\033[0;37m"
G = "\033[0;32m"
R = "\033[0;31m"
Y = "\033[0;33m"


class BannerGrabber:
    def __init__(self, target_address: str, target_port: int):
        self.target_address = target_address
        self.target_port = target_port

    def main(self):
        while True:
            if self.target_address == 'x' or self.target_address == "exit": break
            if self.target_port == 0: break

            try:
                start = datetime.now()
                with socket(AF_INET, SOCK_STREAM) as socket_sock:
                    socket_sock.connect_ex((self.target_address, self.target_port))
                    socket_sock.settimeout(2)
                    banner = socket_sock.recv(1024).decode().replace("\n", "")
                    
                print(f"{W}[{R}*{W}] Sending TCP request {R}...")
                time.sleep(0.25)
                print(f"{W}[{G}+{W}] Port {self.target_port}{R}:{W} {banner}\n{W}[{R}*{W}] "
                      f"Done{R},{W} runtime{R}:{W} {datetime.now() - start}")
                input(f"{W}[{R}*{W}] Press enter key to continue")
                break
            except error as sockerr:
                print(f"{W}[{Y}-{W}] Error{R}:{W} {sockerr}")
                break
            except KeyboardInterrupt:
                print(f"{W}[{R}*{W}] You pressed Ctrl{R}+{W}C{R}.{W} Exit{R}.")
                break
