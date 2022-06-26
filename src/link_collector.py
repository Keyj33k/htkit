#!/usr/bin/env python3

try:
    from termcolor import colored as cld
    from pyfiglet import figlet_format
    from bs4 import BeautifulSoup
    import requests
except ImportError:
    raise RuntimeError("""
    Oops,
    
    this tool uses important modules, which don't seem to be 
    installed at the moment.
     
    Use the requirements file and this command:
    "pip3 install -r requirements.txt" 
    
    You will find this file in the req directory.
    
    
    """)
    
# # # # # # # # # # # # # # # # # # # # # #
#                                         #
#   Author  :   Keyjeek                   #
#   Contact :   nomotikag33n@gmail.com    #
#   Github  :   @Keyj33k                  #
#   Version :   1.1.5                     #
#                                         #
# # # # # # # # # # # # # # # # # # # # # #

class LinkCollector:

    def __init__(
            self,
            uniformresourcelocator: str
    ):
        self.uniformresourcelocator = uniformresourcelocator

    def main(self):
        while True:
            if self.uniformresourcelocator == 'x' or self.uniformresourcelocator == 'exit':
                break

            try:
                request = requests.get(self.uniformresourcelocator)
                soup = BeautifulSoup(
                    request.text,
                    "html.parser"
                )

                for collected_links in soup.find_all("a"):
                    print(
                        " Href found: ",
                        collected_links.get('href')
                    )

                input("Press any key to continue")

            except requests.exceptions.MissingSchema:
                request = requests.get(f"http://{self.uniformresourcelocator}/")
                soup = BeautifulSoup(
                    request.text,
                    "html.parser"
                )

                for collected_links in soup.find_all("a"):
                    print(
                        " Href found: ",
                        collected_links.get('href')
                    )

                input("Press any key to continue")

            break
