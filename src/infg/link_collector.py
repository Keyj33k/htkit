# !/usr/bin/env python3

try:
    from termcolor import colored as cld
    from pyfiglet import figlet_format
    from bs4 import BeautifulSoup
    from requests import get
    from requests.exceptions import MissingSchema
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
    def __init__(self, uniformresourcelocator: str):
        self.uniformresourcelocator = uniformresourcelocator

    def main(self):
        while True:
            if self.uniformresourcelocator == 'x' or self.uniformresourcelocator == 'exit':
                break

            print(f"\n{w}[{r}*{w}] Results:\n{r}{'=' * 70}")

            try:
                soup = BeautifulSoup(get(self.uniformresourcelocator).text, "html.parser")
                for collected_links in soup.find_all("a"):
                    print(f"{w}[{g}+{w}] Href found {r}->{w} ", collected_links.get('href'))

                print(f"{r}=" * 70)
                print(chr(0xa))
                input(f"{w}[{r}*{w}] Press enter key to continue")
                break
            except MissingSchema:
                soup = BeautifulSoup(get(f"http://{self.uniformresourcelocator}/").text, "html.parser")
                for collected_links in soup.find_all("a"):
                    print(f"{w}[{g}+{w}] Href found {r}->{w} ", collected_links.get('href'))

                print(f"{r}=" * 70)
                print(chr(0xa))
                input(f"{w}[{r}*{w}] Press enter key to continue")
                break
