#!/usr/bin/env python3

try:
    from requests.exceptions import MissingSchema
    import requests
    import re
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

def extractor(url: str):
    email_address_regex = ("(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&"
                           "'*+/=?^_`{|}~-]+)*|(?:[\x01-\x08\x0b\x0c\x0e-"
                           "\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*"
                           ")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]"
                           "*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?"
                           "[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])"
                           "|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-"
                           "\x5a\x53-\x7f]|\\[\n\x01-\x09\x0b\x0c\x0e-\x7f])+)\])")

    for url in re.finditer(email_address_regex, requests.get(url).content.decode()):
        print(f"{W}[{G}+{W}] Email address found: {url.group()}")

class EmailExtractor:
    def __init__(self, uniformresourcelocator: str):
        self.uniformresourcelocator = uniformresourcelocator

    def main(self):
        while True:
            print(f"{W}[{R}*{W}] Sending GET request and extract all addresses {R}...")
            try:
                extractor(self.uniformresourcelocator)
            except MissingSchema:
                extractor(f"http://{self.uniformresourcelocator}/")
            except Exception as excerr:
                print(excerr)
                break
            input(f"{W}[{R}*{W}] Press enter key to continue")
            break
