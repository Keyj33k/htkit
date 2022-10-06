#!/usr/bin/env python3

try:
    from datetime import datetime
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


class EmailExtractor:

    def __init__(self, uniformresourcelocator: str):
        self.uniformresourcelocator = uniformresourcelocator

    def extract_mail_address(self):
        email_address_regex = ("(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&"
                               "'*+/=?^_`{|}~-]+)*|(?:[\x01-\x08\x0b\x0c\x0e-"
                               "\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*"
                               ")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]"
                               "*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?"
                               "[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])"
                               "|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-"
                               "\x5a\x53-\x7f]|\\[\n\x01-\x09\x0b\x0c\x0e-\x7f])+)\])")

        while True:
            start_time = datetime.now()
            print(f"{'=' * 70}\n{w}[{r}*{w}] Started scanning at{r}:{w}\t{start_time}")

            try:
                sc_content = requests.get(self.uniformresourcelocator).content
                for url in re.finditer(email_address_regex, sc_content.decode()):
                    print(f"{w}[{g}+{w}] Email address found:\t{url.group()}")

                print(f"{r}{'=' * 70}\n{w}[{r}*{w}] Scanner done in {datetime.now() - start_time}!")
                input(f"{chr(0xa)}\n{w}[{r}*{w}] Press enter key to continue")
                break
            except requests.exceptions.MissingSchema:
                print(f"{w}[{y}-{w}] Invalid format{r}.{w} Did you mean 'http://{self.uniformresourcelocator}/'{r}?{w}")
                break
            except Exception as excerr:
                print(excerr)
                break
