#!/usr/bin/env python3

try:
    from datetime import datetime
    from requests import get
    from requests.exceptions import MissingSchema
    from re import finditer
    from bs4 import BeautifulSoup
    from requests.exceptions import MissingSchema, InvalidSchema, ConnectionError
    from time import sleep
    from src.utils.coloring import W, R, Y, G
except ImportError:
    raise RuntimeError("""
    Oops,
    
    this tool uses important modules, which don't seem to be 
    installed at the moment.
    
    Use the requirements file and this command:
    "pip3 install -r requirements.txt" 
    
    You will find this file in the req directory.
    """)

def runtime(start_time):
    print(f"{W}[{R}*{W}] Done{R},{W} runtime{R}:{W} {datetime.now() - start_time}")

def extractor(target_url: str):
    email_address_regex = ("(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&"
                           "'*+/=?^_`{|}~-]+)*|(?:[\x01-\x08\x0b\x0c\x0e-"
                           "\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*"
                           ")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]"
                           "*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?"
                           "[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])"
                           "|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-"
                           "\x5a\x53-\x7f]|\\[\n\x01-\x09\x0b\x0c\x0e-\x7f])+)\])")

    print(f"{W}[{R}*{W}] Scanning {target_url} for addresses {R}...")
    for address in finditer(email_address_regex, get(target_url).content.decode()):
        print(f"{W}[{G}+{W}] Email address found{R}:{W} {address.group()}")
    else:
        print(f"{W}[{R}*{W}] Finished")

def request(target_url: str):
    for collected_links in BeautifulSoup(get(target_url).text, "html.parser").find_all('a'):
        href = collected_links.get("href")
        sleep(0.5)
        
        try:
            if get(href).status_code == 200:
                extractor(href)
        except MissingSchema:
            pass

class EmailExtractor:
    def __init__(self, uniformresourcelocator: str):
        self.uniformresourcelocator = uniformresourcelocator

    def main(self):
        while True:
            start = datetime.now()
            try:
                request(self.uniformresourcelocator)
                runtime(start)
            except (MissingSchema, InvalidSchema):
                request(f"http://{self.uniformresourcelocator}/")
                runtime(start)
            except Exception as excerr:
                print(excerr)
                break
                
            input(f"{W}[{R}*{W}] Press enter key to continue")
            break
