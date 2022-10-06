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

w = "\033[0;37m"
g = "\033[0;32m"
r = "\033[0;31m"
y = "\033[0;33m"

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
        print(f"{w}[{g}+{w}] Email address found:\t{url.group()}")

class EmailExtractor:
    def __init__(self, uniformresourcelocator: str):
        self.uniformresourcelocator = uniformresourcelocator

    def extract_mail_address(self):
        while True:
            print(f"\n{w}[{r}*{w}] Results\n{r}{'=' * 70}")

            try:
                extractor(self.uniformresourcelocator)
            except requests.exceptions.MissingSchema:
                extractor(f"http://{self.uniformresourcelocator}/")
            except Exception as excerr:
                print(excerr)
                break

            input(f"{r}{'=' * 70}\n{chr(0xa)}\n{w}[{r}*{w}] Press enter key to continue")
            break
