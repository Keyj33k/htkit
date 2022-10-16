#!/usr/bin/env python3

try:
    import urllib3
    from time import sleep
    from pwd import getpwuid
    from os import getuid
    from datetime import datetime
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

class RemoteServerStatusCode:
    def __init__(self, url: str):
        self.url = url

    def main(self):
        while True:
            try:
                start = datetime.now()
                print(f"{W}[{R}*{W}] Sending GET request {R}...")
                sleep(0.25)
                print(f"{W}[{G}+{W}] {self.url}{R}:{W} {urllib3.PoolManager().request('GET', self.url).status}\n"
                      f"{W}[{R}*{W}] Done{R},{W} runtime{R}:{W} {datetime.now() - start}")
                input(f"{W}[{R}*{W}] Press enter key to continue")
                break
            except Exception as excerr:
                print(f"{W}[{Y}-{W}] Error{R}:{W} {excerr}")
                break
            except KeyboardInterrupt:
                print(f"\n{W}[{R}*{W}] You pressed Ctrl{R}+{W}C{R}.{W} Exit{R}.")
                break
