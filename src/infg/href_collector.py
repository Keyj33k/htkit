# !/usr/bin/env python3

try:
    from termcolor import colored as cld
    from pyfiglet import figlet_format
    from bs4 import BeautifulSoup
    from requests import get
    from requests.exceptions import MissingSchema, ConnectionError, InvalidSchema
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

W = "\033[0;37m"
G = "\033[0;32m"
R = "\033[0;31m"
Y = "\033[0;33m"

class HREFCollector:
    def __init__(self, url: str):
        self.url = url

    def main(self):
        while True:
            if self.url == 'x' or self.url == 'exit': break
            print(f"{W}[{R}*{W}] Sending GET requests {R}...")
            start = datetime.now()
            for collected_links in BeautifulSoup(get(f"http://{self.url}/").text, "html.parser").find_all("a"):
                try:

                    print(f"{W}[{G}+{W}] Href found{R}:{W} {collected_links.get('href')} "
                          f"{R}[{W} {get(collected_links.get('href')).status_code} {R}]{W}")
                except (InvalidSchema, MissingSchema):
                    print(f"{W}[{G}+{W}] Href found{R}:{W} {collected_links.get('href')}")
            print(f"{W}[{R}*{W}] Done{R},{W} runtime{R}:{W} {datetime.now() - start}")
            input(f"{W}[{R}*{W}] Press enter key to continue")
            break
