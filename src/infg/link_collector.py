# !/usr/bin/env python3

try:
    from termcolor import colored as cld
    from pyfiglet import figlet_format
    from bs4 import BeautifulSoup
    from requests import get
    from requests.exceptions import MissingSchema, ConnectionError, InvalidSchema
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

class LinkCollector:
    def __init__(self, url: str):
        self.url = url

    def main(self):
        while True:
            if self.url == 'x' or self.url == 'exit': break
            print(f"\n{w}[{r}*{w}] Results:\n{r}{'=' * 70}")
            for collected_links in BeautifulSoup(get(f"http://{self.url}/").text, "html.parser").find_all("a"):
                try:
                    print(f"{w}[{g}+{w}] Href found {r}->{w} {collected_links.get('href')} "
                          f"{r}[{w} {get(collected_links.get('href')).status_code} {r}]{w}")
                except (InvalidSchema, MissingSchema):
                    print(f"{w}[{g}+{w}] Href found {r}->{w} {collected_links.get('href')}")

            print(f"{r}{'=' * 70}\n{chr(0xa)}")
            input(f"{w}[{r}*{w}] Press enter key to continue")
            break
