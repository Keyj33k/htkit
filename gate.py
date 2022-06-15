#!/usr/bin/env python3

from phonenumbers import timezone as tz
from phonenumbers import geocoder as gc
from phonenumbers import carrier as cr
from termcolor import colored as cld
from datetime import datetime as dtt
from bs4 import BeautifulSoup
import phonenumbers as pnmb
import pyfiglet as pfgt
import subprocess
import requests
import hashlib
import socket
import base64
import psutil
import whois
import json
import time
import sys
import os

magenta = "\033[0;35m"
yellow = "\033[0;33m"
green = "\033[0;32m"
white = "\033[0;37m"
cyan = "\033[0;36m"
red = "\033[0;31m"

target_address_witcher = ""
target_port_witcher = ""
target_address = ""
hunter_choice = ""
passw_length = ""
passw_result = ""
target_port = ""
response = ""
new_url = ""
tarad = ""
sd_r = ""
res = ""


# # # # # # # # # # # # # # # # # # # # # #
#                                         #
#   Author  :   Keyjeek                   #
#   Contact :   nomotikag33n@gmail.com    #
#   Github  :   @Keyj33k                  #
#   Version :   1.1.4                     #
#                                         #
# # # # # # # # # # # # # # # # # # # # # #

def banner():
    print(cld("""
    █    █                 █
    █    █                 █
    █    █ █   █  █▒██▒  █████   ███    █▒██▒
    █    █ █   █  █▓ ▒█    █    ▓▓ ▒█   ██  █
    ██████ █   █  █   █    █    █   █   █
    █    █ █   █  █   █    █    █████   █
    █    █ █   █  █   █    █    █       █
    █    █ █▒ ▓█  █   █    █░   ▓▓  █   █
    █    █ ▒██▒█  █   █    ▒██   ███▒   █
    """, "cyan"))
    print(
        magenta + " <" + green + " by@keyjeek " + magenta + ">" +
        cyan + " | " + green + "Follow the white rabbit ..."
    )
    print(
        magenta + " <" + green + " contact:nomotikag33n@gmail.com " +
        magenta + ">" + yellow + " Ver" + magenta + ".:" + red + "1.1.4"
    )
    print(
        cyan + "\n[" + red + "i" + cyan + "] " + yellow +
        "Hunter is a small toolkit to perform information gathering."
    )


def menu():
    print(magenta + "=" * 70)
    print(
        green + "\n{" + red + "0" + green +
        "} " + green + " Clear Screen"
    )
    print(
        green + "{" + red + "1" + green + "} " +
        cyan + " Witcher " + magenta + ">> " + yellow + " A simple port scanner."
    )
    print(
        green + "{" + red + "2" + green + "} " +
        cyan + " MD5Crypt " + magenta + ">> " + yellow + " MD5 encryption."
    )
    print(
        green + "{" + red + "3" + green + "} " + cyan +
        " WhoisForIP " + magenta + ">> " + yellow + " Get informations about an ip address."
    )
    print(
        green + "{" + red + "4" + green + "} " + cyan +
        " BannerGrabber " + magenta + ">> " + yellow + " Get service behind a port."
    )
    print(
        green + "{" + red + "5" + green + "} " + cyan +
        " B64Crypt " + magenta + ">> " + yellow + " En- and Decryption used base64."
    )
    print(
        green + "{" + red + "6" + green + "} " + cyan +
        " PhoneStalk " + magenta + ">> " + yellow + " Get informations about a phonenumber"
    )
    print(
        green + "{" + red + "7" + green + "} " + cyan +
        " SubdomainScanner " + magenta + ">> " + yellow + " Get subdomains from any url."
    )
    print(
        green + "{" + red + "8" + green + "} " + cyan +
        " Whoami " + magenta + ">> " + yellow + " Get infos like current ip address etc."
    )
    print(
        green + "{" + red + "9" + green + "} " + cyan +
        " MySystem " + magenta + ">> " + yellow + " Get infos like cpu usage, disk usage etc."
    )
    print(
        green + "{" + red + "10" + green + "}" + cyan +
        " GetIPfromURL " + magenta + ">> " + yellow + " Get the ip address of any url."
    )
    print(
        green + "{" + red + "11" + green + "}" + cyan +
        " AutoInfoGathering " + magenta + ">> " + yellow + " Get infos like: open ports, location etc."
    )
    print(
        green + "{" + red + "12" + green + "}" + cyan +
        " PassGen " + magenta + ">> " + yellow + " Generate a random password."
    )
    print(
        green + "{" + red + "13" + green + "}" + cyan +
        " WhoisForURL " + magenta + ">> " + yellow + " Whois lookup for URL."
    )
    print(
        green + "{" + red + "14" + green + "}" + cyan +
        " GHeader " + magenta + ">> " + yellow + " Get header from url."
    )
    print(
        green + "{" + red + "15" + green + "}" + cyan +
        " GLinks " + magenta + ">> " + yellow + " Get links from any website."
    )
    print(
        green + "{" + red + "16" + green + "}" + cyan +
        " Ping " + magenta + ">> " + yellow + " Check host availability."
    )
    print(green + "{" + red + "99" + green + "}" + green + " Exit\n")
    
    print(magenta + "=" * 70)


def get_links():
    while True:
        passgen_banner = pfgt.figlet_format(
            "GLinks",
            font="slant"
        )
        print(
            cld(
                passgen_banner,
                "cyan"
            )
        )
        target = input(
            cyan + "(" + yellow +
            f"{os.getlogin()}@GLinks(URL, use 'x' to exit)" + cyan + ")>> "
        )
        if target == 'x' or target == 'exit':
            break

        try:
            resp = requests.get(target)
            soup = BeautifulSoup(
                resp.text,
                "html.parser"
            )

            for l in soup.find_all("a"):
                print(cyan + "[" + red + "+" + cyan + "]" + green + " Href found: ", l.get('href'))

        except requests.exceptions.MissingSchema:
            resp = requests.get(f"http://{target}/")
            soup = BeautifulSoup(
                resp.text,
                "html.parser"
            )

            for l in soup.find_all("a"):
                print(cyan + "[" + red + "+" + cyan + "]" + green + " Href found: ", l.get('href'))
                

def get_ip_from_url():
    while True:
        passgen_banner = pfgt.figlet_format(
            "url2ip",
            font="slant"
        )
        print(
            cld(
                passgen_banner,
                "cyan"
            )
        )

        try:
            target_url = str(
                input(
                    cyan + "(" + yellow +
                    f"{os.getlogin()}@WhoisURL(URL, use 'x' to exit)" +
                    cyan + ")>> "
                )
            )
            if target_url == 'x' or target_url == 'exit':
                break

            print(
                green + "\n[" + red + "*" + green + "]" + cyan +
                f" IP Address from {target_url}: " + green + socket.gethostbyname(target_url)
            )
            input(cyan + "\nPress any key to continue")
        except ValueError:
            print(red  + "\nYou need to enter a value like: google.com in example.")
            input(cyan + "Press any key to continue")
            get_ip_from_url()
        except socket.gaierror:
            print(red  + "\nYou need to enter a value like: google.com in example.")
            input(cyan + "Press any key to continue")
            get_ip_from_url()


def password_generator():
    import random
    global passw_length
    global passw_result

    while True:
        passgen_banner = pfgt.figlet_format(
            "passgen",
            font="slant"
        )
        
        print(
            cld(
                passgen_banner,
                "cyan"
            )
        )

        try:
            passw_length = int(
                input(
                    cyan + "(" + yellow + f"{os.getlogin()}@PassGen(Length, use '0' to exit)" + cyan + ")>> "
                )
            )
        except ValueError as ve:
            print(red + f"You need to enter a integer!\n{ve}")
            password_generator()

        if passw_length == 0:
            break
        elif passw_length <= 7:
            print(
                cld(
                    "Your password should be always bigger than eight characters.",
                    "red"
                )
            )

            input(cyan + "\nPress any key to continue")

            password_generator()

        numbers      = "1234567890"
        lowers       = "abcdefghijklmnopqrstuvwxyz"
        uppers       = "ABVDEFGHIJKLMNOPQRSTUVWXYZ"
        special      = "§$%&/()=}[{]?!_;:"
        mixer        = numbers + lowers + uppers + special
        passw_result = random.sample(
            mixer,
            passw_length
        )
        finalp = ''.join(passw_result)

        print(
            cyan + "\n[" + red + "+" + cyan + "] " + green +
            "Your generated password: " + cyan + f"{finalp}\n" + white
        )

        input(yellow + "Press any key to continue")


def whoami_():
    import uuid, re
    get_mac = ':'.join(
        re.findall(
            '..', '%012x' % uuid.getnode()
        )
    )
    get_hostname = socket.gethostname()
    get_host_ip  = socket.gethostbyname(get_hostname)
    get_username = os.getlogin()
    get_path     = os.path.abspath(os.getcwd())
    get_time     = dtt.now()

    def check_root():
        if "SUDO_UID" in os.environ.keys():
            print(cyan + "\tType         :" + yellow + "\tRoot User")
        else:
            print(cyan + "\tType         :" + yellow + "\tNormal User")

    print(cyan    + "\t\t\tWhoami")
    print(magenta + "< " + green + "=" * 66 + magenta + " >")
    print(cyan    + "\tDate         :" + yellow + f"\t{get_time}")
    print(cyan    + "\tUsername     :" + yellow + f"\t{get_username}")
    check_root()
    print(cyan    + "\tHostname     :" + yellow + f"\t{get_hostname}")
    print(cyan    + "\tIPAddress    :" + yellow + f"\t{get_host_ip}")
    print(cyan    + "\tMACAddress   :" + yellow + f"\t{get_mac}")
    print(cyan    + "\tCurrent Path :" + yellow + f"\t{get_path}")
    input(cyan    + "\nPress any key to continue")


def get_header():
    while True:
        passgen_banner = pfgt.figlet_format(
            "GHeader",
            font="slant"
        )
        print(
            cld(
                passgen_banner,
                "cyan"
            )
        )
        header_from = input(
            cyan + "(" + yellow + f"{os.getlogin()}@GHeader(Address, use 'x' to exit)"
            + cyan + ")>> "
        )
        if header_from == 'x' or header_from == 'exit':
            break

        try:
            subprocess.call(
                [
                    "curl",
                    "-I",
                    header_from
                ]
            )
        except subprocess.CalledProcessError:
            print(
                red +
                f"Failed getting header from {header_from}\n\n"
            )

        input(magenta + "\nPress any key to continue")


def witcher():
    global target_port_witcher, target_address_witcher

    while True:
        os.system("clear")
        witcher_banner = pfgt.figlet_format(
            "witcher",
            font="slant"
        )
        print(
            cld(
                witcher_banner,
                "cyan"
            )
        )

        try:
            target_address_witcher = input(
                    cyan + "(" + yellow +
                    f"{os.getlogin()}@Witcher(Address, use 'x' to exit)" +
                    cyan + ")>> "
            )
            if target_address_witcher == 'exit' or target_address_witcher == 'x':
                break
        except ValueError:
            print(
                cld(
                    "\nYou need to enter a string!",
                    "red"
                )
            )
            input(cyan + "Press any key to continue")
            witcher()

        try:
            target_port_witcher = int(
                input(
                    f"({os.getlogin()}@Witcher(Max. Port, use '0' to exit))>> "
                )
            )
            if target_port_witcher == 0:
                break
        except ValueError:
            print(
                cld(
                    "\nYou need to enter a integer!",
                    "red"
                )
            )
            input(cyan + "Press any key to continue")
            
            witcher()

        print(
            magenta + 
            "=" * 70
        )
        scan_start = dtt.now()
        print(
            green + 
            f"Started scanning at:\t\t\t{scan_start}"
        )
        print(
            magenta + 
            "=" * 70
        )
        time_start = dtt.now()
        print(
            green + 
            "Protocol\tPort\t\tStatus\t Service\n" + 
            magenta + 
            "-" * 70
        )

        try:
            for target in range(
                    1, target_port_witcher
            ):
                socket_sock = socket.socket(
                    socket.AF_INET,
                    socket.SOCK_STREAM
                )
                final_result = socket_sock.connect_ex((
                    target_address_witcher,
                    target
                ))
                socket_sock.settimeout(1)
                if final_result == 0:
                    try:
                        print(green + f"TCP\t\t\t{target}  \t\topen\t", socket.getservbyport(target))
                    except:
                        print(green + f"TCP\t\t\t{target}  \t\topen\t Unknown")
                socket_sock.close()
        except socket.error as socket_error:
            print(
                cld(
                    socket_error,
                    "red"
                )
            )
        except KeyboardInterrupt:
            print(
                cld(
                    "\nCtrl+C pressed. Exit.",
                    "red"
                )
            )
            break

        time_stop = dtt.now()
        needed_time = time_stop - time_start
        
        print(magenta + "=" * 70)
        print(
            cld(
                f"Scanner done in {needed_time}!",
                "green"
            )
        )
        print(magenta + "=" * 70)
        print(chr(0xa))
        
        input(cyan + "Press any key to continue")


def subdomain_scanner():
    import requests

    while True:
        sds_banner = pfgt.figlet_format(
            "Sub- domain- Scanner",
            font="slant"
        )
        
        print(magenta + sds_banner)
        
        found_subdomain    = []
        target_address_sds = input(
            cyan + "(" + yellow +
            f"{os.getlogin()}@SDS(URL, use 'x' to exit)"
            + cyan + ")>> "
        )
        if target_address_sds == 'exit' or target_address_sds == 'x':
            break

        with open("subdomains.txt") as FILE:
            read_file = FILE.read()
            subdomain = read_file.splitlines()
            for list_domains in subdomain:
                uniformresourcelocator = f"http://{list_domains}.{target_address_sds}"
                time.sleep(1)

                try:
                    requests.get(uniformresourcelocator)
                except requests.ConnectionError:
                    pass
                else:
                    print(
                        cyan + "[" + red + "+" + cyan + "] " + green + "Discovered:",
                        uniformresourcelocator
                    )
                    found_subdomain.append(
                        uniformresourcelocator
                    )

        input(cyan + "Press any key to continue")


def md5():
    while True:
        md5_banner = pfgt.figlet_format(
            "MD5C",
            font="slant"
        )
        print(
            cld(
                md5_banner,
                "cyan"
            )
        )
        print(
            cyan + "[" + red + "i" + cyan + "]" +
            yellow + " md5crypt is made to encrypt your string to an 128 bit hash value"
        )
        print(
            cyan + "[" + red + "i" + cyan + "]" +
            yellow + " Type 'exit' to exit md5crypt."
        )
        print(chr(0xa))

        hash_value = input(
            cyan + "(" + yellow +
            f"{os.getlogin()}@MD5(use 'x' to exit)" +
            cyan + ")>> "
        )
        if hash_value == 'exit' or hash_value == 'x':
            print(
                cld(
                    "Exit",
                    "red"
                )
            )
            break

        try:
            result = hashlib.md5(hash_value.encode())
            print(
                cyan + "[" + red + "+" + cyan + "]" + green +
                "\nResult: " + 
                green, 
                end=""
            )
            print(result.hexdigest())
            
            input(cyan + "\nPress any key to continue")
        except Exception as error:
            print(
                cld(
                    f"An error was defined! {error}", 
                    "red"
                )
            )
            
            input(cyan + "Press any key to continue")
            
            md5()  
            
            """
            
            https://www.md5online.org/md5-decrypt.html 
            This program is using a big database to bruteforce the hash for you
            
            """


def conditions():
    os.system("clear")
    
    print(cld("""
 \t\t\tWelcome To Hunter Toolkit!
 < =============================================================================== >
 
 \n Please note that actions like portscanning etc. can be illegal. 
 If you want to use this tool, follow the conditions:

  - This tool is made for ethical purposes only.
  - I'm not responsible for your actions.
  - With great force follows great responsibility.

 If you accept the conditions type 'y' and 'n' for decline.
 Thank you and have a nice day!

  ~ Keyjeek\n
    """, "red"))

    choice = input(
        cyan + "(" + yellow + f"{os.getlogin()}@" +
        red + "Hunter" + cyan + ")>> "
    )
    if choice == 'y' or choice == 'Y':
        pass
    elif choice == 'n' or choice == 'N':
        print(
            cld(
                "You need to accept the terms above to use Hunter. Exit.",
                "red"
            )
        )
        sys.exit(0)
    else:
        os.system("clear")
        print(
            cld(
                "Invalid Input!",
                "red"
            )
        )
        input(cyan + "Press any key to continue")
        
        os.system("clear")
        
        return conditions()


def eye_main():
    global response
    while True:
        ipe_banner = pfgt.figlet_format(
            "IPWhois",
            font="slant"
        )
        print(
            cld(
                ipe_banner,
                "yellow"
            )
        )
        print(red + "[" + cyan + "i" + red + "]" + yellow + "IPEye is a Tool to find out")
        print(red + "--" + magenta + "> " + yellow + "some information about an IP Address.")
        print(red + "[" + cyan + "i" + red + "]" + yellow + "Type 'exit' to exit ipeye.")
        
        print(chr(0xa))

        ipeye_scanner = input(
            cyan + "(" + yellow +
            f"{os.getlogin()}@IPWhois(IP, use 'x' to exit)" +
            cyan + ")>> "
        )
        if ipeye_scanner == 'exit' or ipeye_scanner == 'x':
            print(
                cld(
                    "Exiting ...",
                    "red"
                )
            )
            
            break
            
        time_start = dtt.now()
        print(cyan + "[" + red + "*" + cyan + "] " + green + "Results:")

        try:
            response = requests.post(
                "http://ip-api.com/batch",
                json=[{"query": ipeye_scanner}]
            ).json()
        except Exception as error:
            print(
                cld(
                    f"An error was defined! {error}",
                    "red"
                )
            )
            input(cyan + "Press any key to continue")
            
            os.system('clear')
            
            eye_main()

        print(magenta + "=" * 70 + "\n")

        for lookup in response:
            for k, j in lookup.items():
                print(cyan + "[" + red + "+" + cyan + "] " + green + k, j)

        time_stop = dtt.now()
        time_result = time_stop - time_start
        print("\n" + magenta + "=" * 70)

        print(chr(0xa))

        print(green + f"Scanner done in {time_result}!")
        input(cyan + "Press any key to continue")


def banner_grabber():
    tab2 = "\t" * 2
    tab3 = "\t" * 3
    line = magenta + "==" * 42

    info_array = [
        "@Keyj33k", 
        "1.0.1", 
        "06.04.22", 
        "Python3"
    ]

    links = [
        "https://github.com/Keyj33k", 
        "https://www.instagram.com/keyjeek/", 
        "nomotikag33n@gmail.com"
    ]

    author_name = info_array[0]
    version_num = info_array[1]
    written_on  = info_array[2]
    progr_lang  = info_array[3]
    instagram   = links[1]
    github      = links[0]
    email       = links[2]

    while True:
        target_host = input(
            cyan + "(" + yellow +
            f"{os.getlogin()}@GBanner(URL, use 'x' to exit)" +
            cyan + ")>> "
        )
        if target_host == 'exit' or target_host == 'x':
            os.system("clear")
            break

        target_p = input(
            red +
            "[" + cyan + "*" + red + "]" +
            cyan + " Port " + yellow +
            "(Exit with 'exit' or 'x'): " +
            red
        )

        if target_p == 'exit' or target_host == 'x':
            os.system("clear")
            break

        try:
            socket_sock = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )
            socket_sock.connect_ex((
                str(
                    target_host
                ),
                int(
                    target_port
                )
            ))
            
            socket_sock.settimeout(1)
            
            banner_result     = socket_sock.recv(1024).decode()
            time_start        = dtt.now()
            bannergrab_banner = pfgt.figlet_format(
                "Banner Grabber",
                font="slant"
            )
            
            print(
                cld(
                    bannergrab_banner,
                    "cyan"
                )
            )
            
            print(line)
            
            print(
                cyan + " Auth.:\t" + yellow + f"{author_name}{tab2}" + 
                cyan + "Github: " + yellow + f"{github}"
            )
            
            print(
                cyan + " Date :\t" + yellow + f"{written_on}{tab2}" + 
                cyan + "Instagram: " + yellow + f"{instagram}"
            )
            
            print(
                cyan + " Lang.:\t" + yellow + f"{progr_lang}{tab3}" + 
                cyan + "Email: " + yellow + f"{email}"
            )
            
            print(cyan + " Vers.:\t" + yellow + f"{version_num}")
            print(line)
            
            print(
                cld(
                    f" Started at:{tab3}{time_start}",
                    "yellow"
                )
            )
            
            print(line + "\n")
            
            print(
                cld(
                    f" Started at:{tab3}{time_start}",
                    "yellow"
                )
            )
            
            print(
                cld(
                    f" Target Host:{tab3}{target_host}",
                    "yellow"
                )
            )
            
            print(
                cld(
                    f" Target Port:{tab3}{target_port}",
                    "yellow"
                )
            )
            
            print(
                cld(
                    f"\n Result:{tab3}{banner_result}",
                    "green"
                )
            )
            
            print(line)
            
            time_end    = dtt.now()
            time_result = time_end - time_start
            
            print(
                cld(
                    f" Job done in:{tab3}{time_result}",
                    "green"
                )
            )
            
            print(line)
            print(chr(0xa))
            
            input(cyan + "Press any key to continue")
            
        except socket.error as sock_err:
            print(
                cld(
                    f"\nAn error was defined: {sock_err}",
                    "red"
                )
            )
            
            return banner_grabber()


def base64encode():
    while True:
        b64_banner = pfgt.figlet_format(
            "B64-  CRYPT",
            font="slant"
        )
        
        print(
            cld(
                b64_banner,
                "green"
            )
        )
        
        print(
            red + "[" + cyan + "i" + red + "] " +
            yellow + "This Tool encode and decode your text in base64."
        )
        
        print(
            red + "[" + cyan + "i" + red + "] " +
            yellow + "Type 'exit' to exit Base64crypt."
        )
        
        print(red + "\n\t[" + cyan + "1" + red + "] " + yellow + "Encoder")
        print(red + "\t[" + cyan + "2" + red + "] " + yellow + "Decoder")
        print(red + "\t[" + cyan + "x" + red + "] " + yellow + "Exit")

        choice = input(
            cyan + "\nChoice " +
            magenta + "~#$ " + green
        )

        if choice == "1":
            hash_value = input(f"({os.getlogin()}@B64C(Value, use 'x' to exit))>> ")
            if hash_value == 'exit' or hash_value == 'x':
                break

            try:
                m_bytes = hash_value.encode('ascii')
                b64_e = base64.b64encode(m_bytes)
                b64_hash = b64_e.decode('ascii')
                print(cyan + "[" + red + "+" + cyan + "]" + green + b64_hash)
                
                input(cyan + "Press any key to continue")
                
                return base64encode()
            
            except Exception as error:
                print(
                    cld(
                        f"An error was defined: {error}"
                    )
                )
                
                input(cyan + "Press any key to continue")

                return base64encode()

        elif choice == "2":
            decode_hash = input(
                cyan + "Hash: " +
                magenta + "~#$ " +
                red
            )
            if decode_hash == 'exit' or decode_hash == 'x':
                print(
                    cld(
                        "Exit",
                        "red"
                    )
                )
                
                break

            try:
                b64_d = decode_hash.encode('ascii')
                m_byte = base64.b64decode(b64_d)
                result = m_byte.decode('ascii')
                print(cyan + "[" + red + "+" + cyan + "]" + green + result)

                input(cyan + "Press any key to continue")

                return base64encode()
            except Exception as error:
                print(
                    cld(
                        f"An error was defined: {error}"
                    )
                )
                
                input(cyan + "Press any key to continue")

                return base64encode()

        elif choice == 'x' or choice == 'exit':
            break
        else:
            print(red + "Invalid Input!")


def number_tracker():
    pnsk_banner = pfgt.figlet_format(
        "Phone- Stalk",
        font="slant"
    )
    
    print(
        cld(
            pnsk_banner,
            "magenta"
        )
    )
    
    print(red + "[" + cyan + "*" + red + "]" + yellow
          + "This Tool helps to find out some informations\n about a phonenumber.")
    print(red + "[" + cyan + "*" + red + "]" + yellow + "Type 'exit' to exit PhoneStalk.")

    while True:
        print(chr(0xa))
        
        target_phonenumber = input(
            cyan + "(" + yellow + f"{os.getlogin()}@PhonenumberWhois(Phonenumber, use 'x' to exit)"
            + cyan + ")>> "
        )
        
        if target_phonenumber == 'exit' or target_phonenumber == 'x':
            print(
                cld(
                    "Exit",
                    "red"
                )
            )
            
            break
            
        elif target_phonenumber == "help" or target_phonenumber == 'h':
            print(cyan    + "\nHELP; " + yellow + "Phone-Stalk")
            print(magenta + "< " + green + "=" * 15 + magenta + " >")
            print(red     + "'exit'        " + yellow + "Return Menu / Exit PhoneStalk")
            print(red     + "'clear'       " + yellow + "Clear Screen")
            print(chr(0xa))
            input(cyan    + "Press any key to continue")

        time_start    = dtt.now()
        print(magenta + "=" * 55)
        print(yellow  + "Request\t\t\tResponse\n" + magenta + "=" * 55 + "\n")

        try:
            valid_check   = pnmb.parse(target_phonenumber)
            finally_valid = pnmb.is_valid_number(valid_check)
            print(cyan + "[" + red + "+" + cyan + "] " + green + f"Validation:\t{finally_valid}")
            
            phonenumbers_timezone = pnmb.parse(
                target_phonenumber, 
                "en"
            )
            
            final_timezone = tz.time_zones_for_number(phonenumbers_timezone)
            print(cyan + "[" + red + "+" + cyan + "] " + green + f"Timezone:\t{final_timezone}")
            
            phonenumbers_location = pnmb.parse(
                target_phonenumber, 
                "CH"
            )
            
            final_phonenumbers_location = gc.description_for_number(
                phonenumbers_location, 
                "en"
            )
            
            print(cyan + "[" + red + "+" + cyan + "] " + green + f"Location:\t{final_phonenumbers_location}")
            phonenumbers_provider = pnmb.parse(
                target_phonenumber, 
                "RO"
            )
            
            final_phonenumbers_provider = cr.name_for_number(
                phonenumbers_provider, 
                "en"
            )
            
            print(cyan + "[" + red + "+" + cyan + "] " + green + f"Provider:\t{final_phonenumbers_provider}")

            time_stop = dtt.now()
            time_result = time_stop - time_start
            
            print(
                "\n" + 
                magenta + 
                "=" * 55
            )
            
            print(
                green + 
                f"Job done in {time_result}"
            )
            
            print(
                magenta + 
                "=" * 55
            )
            
        except Exception as error:
            print(
                cld(
                    "[*] An error was defined!",
                    "red"
                )
            )
            
            print(error)
            input(red + "Press any key to continue")
            number_tracker()

        print(chr(0xa))
        
        input(cyan + "Press any key to continue")

        break


def my_system():
    import platform

    try:
        while True:
            print(
                cyan +
                pfgt.figlet_format(
                    "sysinf",
                    font="slant"
                )
            )

            continue_or_exit = input(
                yellow +
                "Press any key to continue, 'x' to exit "
            )

            start_time = dtt.now()
            if continue_or_exit == 'exit' or continue_or_exit == 'x':
                break

            os.system("clear")
            get_system = platform.uname()

            print(
                magenta +
                "=" * 45,
                "| Sys_Info |",
                "=" * 45
            )

            print(
                cyan + "\nSystem: " + yellow +
                f"{get_system.system}"
            )

            print(
                cyan + "Name: " + yellow +
                f"{get_system.node}"
            )

            print(
                cyan + "Release: " + yellow +
                f"{get_system.release}"
            )

            print(
                cyan + "Version: " + yellow +
                f"{get_system.version}"
            )

            print(
                cyan + "Machine: " + yellow +
                f"{get_system.machine}"
            )

            print(
                cyan + "Processor: " + yellow +
                f"{get_system.processor} \n"
            )

            def show_size(size):
                f = 1024
                for t in ["B", "KB", "MB", "GB", "TB"]:
                    if size > f:
                        size = size / f
                    else:
                        return f"{size:.3f}{t}"  # output formatted to 3 decimal places

            get_partitions = psutil.disk_partitions()

            print(
                magenta +
                "=" * 40,
                "| Disk_Information |",
                "=" * 42
            )

            for part in get_partitions:
                print(cyan + "\nDevice: " + yellow + f"{part.device}")
                print(cyan + "Mount At: " + yellow + f"{part.mountpoint}")
                print(cyan + "Type: " + yellow + f"{part.fstype}")

                try:
                    part_usage = psutil.disk_usage(part.mountpoint)
                except PermissionError:
                    continue

                print(
                    cyan + "Total Size: " + yellow +
                    f"{show_size(part_usage.total)}"
                )

                print(
                    cyan + "In Use: " + yellow +
                    f"{show_size(part_usage.used)}"
                )

                print(
                    cyan + "Free: " + yellow +
                    f"{show_size(part_usage.free)}"
                )

                print(
                    cyan + "Percentance: " + yellow +
                    f"{part_usage.percent}%"
                )

            disk_io = psutil.disk_io_counters()

            print(
                cyan + "Read Since Boot: " + yellow +
                f"{show_size(disk_io.read_bytes)}"
            )

            print(
                cyan + "Written Since Boot: " + yellow +
                f"{show_size(disk_io.write_bytes)} \n"
            )

            print(
                magenta +
                "=" * 40,
                "| CPU_Info |",
                "=" * 50
            )

            print(
                cyan + "\nCores: " + yellow +
                f"{psutil.cpu_count(logical=False)}"
            )

            print(
                cyan + "Logical Cores: " + yellow +
                f"{psutil.cpu_count(logical=True)}"
            )

            print(
                cyan + "Maximal Freq: " + yellow +
                f"{psutil.cpu_freq().max:.1f}Mhz"
            )

            print(
                cyan + "Current Freq: " + yellow +
                f"{psutil.cpu_freq().current:.1f}Mhz"
            )

            print(
                cyan + "CPU Usage: " + yellow +
                f"{psutil.cpu_percent()}%"
            )

            print(
                cyan +
                "\nCPU Core Usage: \n" +
                yellow
            )

            for core, percentance in enumerate(
                    psutil.cpu_percent(
                        percpu=True,
                        interval=1
                    )
            ):  # show percentence for all cores # 1
                print(f"Core {core}: {percentance}% ")

            virtual_mem = psutil.virtual_memory()
            swap = psutil.swap_memory()

            print(
                magenta +
                "=" * 40,
                "| Ram_Info |",
                "=" * 51
            )

            print(
                cyan + "\nTotal: " + yellow +
                f"{show_size(virtual_mem.total)}"
            )

            print(
                cyan + "\nAvailable: " + yellow +
                f"{show_size(virtual_mem.available)}"
            )

            print(
                cyan + "In Use: " + yellow +
                f"{show_size(virtual_mem.used)}"
            )

            print(
                cyan + "Percentence: " + yellow +
                f"{show_size(virtual_mem.percent)}% \n"
            )

            print(
                magenta +
                "=" * 45,
                "| SWAP |",
                "=" * 50,
                "\n"
            )

            print(
                cyan + "Total: " + yellow +
                f"{show_size(swap.total)} "
            )

            print(
                cyan + "Free: " + yellow +
                f"{show_size(swap.free)} "
            )

            print(
                cyan + "In Use: " + yellow +
                f"{show_size(swap.used)} "
            )

            print(
                cyan + "Percentence: " + yellow +
                f"{swap.percent}%\n"
            )

            print(
                magenta +
                "=" * 40,
                "| Network Information |",
                "=" * 40,
                "\n"
            )

            if_addrs = psutil.net_if_addrs()

            for interface_name, interface_addresses in if_addrs.items():
                for address in interface_addresses:
                    print(
                        cyan +
                        "Interface: " +
                        yellow +
                        f"{interface_name}"
                    )
                    if str(address.family) == 'AddressFamily.AF_INET':
                        print(
                            cyan + "IP: " + yellow +
                            f"{address.address}"
                        )

                        print(
                            cyan + "Netmask: " + yellow +
                            f"{address.netmask}"
                        )

                        print(
                            cyan + "Broadcast IP: " + yellow +
                            f"{address.broadcast}"
                        )

                    elif str(address.family) == 'AddressFamily.AF_PACKET':
                        print(
                            cyan + "MAC: " + yellow +
                            f"{address.address}"
                        )

                        print(
                            cyan + "Netmask: " + yellow +
                            f"{address.netmask}"
                        )

                        print(
                            cyan + "Broadcast MAC: " + yellow +
                            f"{address.broadcast}"
                        )

            net_io = psutil.net_io_counters()

            print(
                cyan + "Total Bytes Sent: " + yellow +
                f"{show_size(net_io.bytes_sent)}"
            )

            print(
                cyan + "Total Bytes Received: " + yellow +
                f"{show_size(net_io.bytes_recv)}\n"
            )

            boot_time_timestamp = psutil.boot_time()
            boot_time = dtt.fromtimestamp(boot_time_timestamp)

            print(
                magenta +
                "=" * 40,
                "| Boot |",
                "=" * 55
            )

            print(
                cyan +
                "\nLast Boot: " +
                yellow +
                f"{boot_time.day}.{boot_time.month}.{boot_time.year} " +
                f"{boot_time.hour}:{boot_time.minute}:{boot_time.second}\n"
            )

            end_time    = dtt.now()  # get end time
            needed_time = end_time - start_time

            print(
                cyan +
                "Job Done In " +
                green +
                f"{needed_time}"
            )
    except PermissionError:
        print(red + "Your device needs to be root for this function!\n")
        
    input(cyan + "Press Any Key To Continue")


def whois_url():
    global tarad

    while True:
        passgen_banner = pfgt.figlet_format(
            "who$url",
            font="slant"
        )
        
        print(
            cld(
                passgen_banner,
                "cyan"
            )
        )

        try:
            tarad = str(
                input(
                    red + "(" + cyan + "(URL, use 'x' to exit)" + red +
                    ")" + magenta + "$ " + yellow
                )
            )
            if tarad == 'x' or tarad == 'exit':
                break
        except ValueError:
            print(red + "You need to enter a address like: example.com!")
            input(cyan + "Press any key to continue")

        whs = whois.whois(tarad)
        print(green + whs.text)
        
        input(cyan + "Press any key to continue")


def check_host_availability():
    while True:
        try:
            paddr = input(
                red + "(" + cyan + "Address, use 'x' to exit" +
                red + ")>> " + yellow
            )

            if paddr == 'x' or paddr == 'exit':
                break

            ping = subprocess.check_output(
                [
                    "ping",
                    "-c",
                    "3",
                    paddr
                ]
            )

            if not ping:
                print(
                    red + "\n[" + cyan + "*" + red +
                    "]" + red + f" Host {paddr} seems to be dead!\n"
                )
            else:
                print(
                    red + "\n[" + cyan + "*" + red +
                    "]" + green + f" Host {paddr} is alive!\n"
                )

            input(cyan + "Press any key to continue ...")
        except subprocess.CalledProcessError as scpe:
            print(f"\n{scpe}")


def information_gathering():
    try:
        while True:
            # os.system('clear')
            global target_address, target_port
            global new_url
            global sd_r
            global res

            try:
                target_address = input(
                        cyan + "(" + yellow + f"{os.getlogin()}@AIG(URL, use 'x' to exit)"
                        + cyan + ")>> "
                )
                if target_address == 'x' or target_address == 'exit':
                    break
            except ValueError:
                print(red + "You need to enter a string!")
                input(cyan + "Press any key to continue")

            try:
                target_port = int(
                    input(
                        cyan + "Max. Port: " +
                        yellow
                    )
                )
                if target_port == 0:
                    break
            except ValueError:
                print(red + "You need to enter a integer!")
                input(cyan + "Press any key to continue")
                
                information_gathering()

            os.system('clear')
            print(yellow + "Time for a coffee break!")
            time.sleep(0.5)
            print(yellow + "(...)")
            time.sleep(1.25)
            
            date_n = dtt.now()

            with open("results.txt", "w") as resf:
                try:
                    resf.write(
                        f"Results from {target_address}/{socket.gethostbyname(target_address)} at {date_n}\n" +
                        "=" * 75 + "\n"
                    )
                except socket.gaierror:
                    print("Results:")

            def locate():
                try:
                    target_addr = socket.gethostbyname(target_address)
                    resp        = requests.get(
                        f'https://ipapi.co/{target_address}/json/'
                    ).json()
                    d = {
                        "IP Address": target_addr,
                        "Country": resp.get("country_name"),
                        "Region": resp.get("region"),
                        "City": resp.get("city"),
                    }
                    con_to_str = json.dumps(d)
                    return con_to_str
                except socket.timeout:
                    pass

            try:
                for target in range(1, target_port):
                    try:
                        socket_sock = socket.socket(
                            socket.AF_INET,
                            socket.SOCK_STREAM
                        )
                        final_result = socket_sock.connect_ex((
                            target_address,
                            target
                        ))
                        socket_sock.settimeout(1)
                        if final_result == 0:
                            res = f"\nPort\t{target}\t\t\t\t\t   open\n"  # , socket_sock.recv(1024).decode())
                        socket_sock.close()
                    except socket.timeout:
                        continue
            except socket.error as socket_error:
                print(
                    cld(
                        socket_error,
                        "red"
                    )
                )
                information_gathering()
            except KeyboardInterrupt:
                pass

            with open("subdomains.txt") as subd_list_file:
                file_content      = subd_list_file.read()
                sub_sp_subdomains = file_content.splitlines()
                found_subdomains  = []

            for subdomain in sub_sp_subdomains:
                url = f"http://{subdomain}.{target_address}"
                time.sleep(1)
                try:
                    requests.get(url)
                except requests.ConnectionError:
                    pass
                else:
                    found_subdomains.append(url)

            with open("result_subdomains.txt", "w") as f:
                for subdomain in found_subdomains:
                    print(
                        subdomain,
                        file=f
                    )

            with open("results.txt", "a") as final_output:
                try:
                    final_output.write(locate())
                except Exception as error:
                    print(
                        cld(
                            f"An error was defined! {error}",
                            "red"
                        )
                    )
                    
                    information_gathering()

                try:
                    final_output.write(res)
                except Exception as error:
                    print(
                        cld(
                            f"An error was defined! {error}",
                            "red"
                        )
                    )
                    
                    information_gathering()

            date_e      = dtt.now()
            needed_time = date_e - date_n
            print(green + f"\nJob done in {needed_time}!")

    except KeyboardInterrupt:
        print(red  + "Ctrl+C pressed. Exit.")
        input(cyan + "Press any key to continue")


if __name__ == "__main__":
    conditions()


    def start():
        os.system("clear")
        time_now = dtt.now()
        username = os.getlogin()
        print(cld(f"Welcome {username}. Today is the {time_now}", "yellow"))
        
        time.sleep(0.75)
        
        start_hunter = input(
            yellow + "Do you want to start hunter? (" + green +
            "y" + yellow + "/" + red + "n" + yellow + ") " + cyan
        )
        if start_hunter == 'y' or start_hunter == 'Y':
            pass
        elif start_hunter == 'n' or start_hunter == 'N':
            sys.exit(0)
        else:
            print(cld("Invalid Input!", "red"))
            input(cyan + "Press any key to continue")
            return start()


    start()


    def hunter_main():
        while True:
            banner()
            menu()
            global hunter_choice

            try:
                hunter_choice = int(
                    input(
                        cyan + "(" + yellow + f"{os.getlogin()}@" +
                        red + "Hunter" + cyan + ")>> " + magenta
                    )
                )
            except KeyboardInterrupt:
                print(red + "\nCtrl+C pressed. Exit")
                sys.exit(0)
            except ValueError:
                print(
                    cld(
                        "You need to enter an integer!",
                        "red"
                    )
                )
                
                input(cyan + "Press any key to continue")
                
                return hunter_main()

            if hunter_choice == 1:
                witcher()
            elif hunter_choice == 2:
                md5()
            elif hunter_choice == 3:
                eye_main()
            elif hunter_choice == 4:
                banner_grabber()
            elif hunter_choice == 5:
                base64encode()
            elif hunter_choice == 6:
                number_tracker()
            elif hunter_choice == 7:

                try:
                    subdomain_scanner()
                except KeyboardInterrupt:
                    print(
                        cld(
                            "\nCtrl+C pressed, Exiting ...",
                            "red"
                        )
                    )
                    
                    input(cyan + "Press any key to continue")
                    
                    return hunter_main()

            elif hunter_choice == 8:
                whoami_()
            elif hunter_choice == 9:
                my_system()
            elif hunter_choice == 10:
                get_ip_from_url()
            elif hunter_choice == 11:
                information_gathering()
            elif hunter_choice == 12:
                password_generator()
            elif hunter_choice == 13:
                whois_url()
            elif hunter_choice == 14:
                get_header()
            elif hunter_choice == 15:
                get_links()
            elif hunter_choice == 16:
                check_host_availability()
            elif hunter_choice == 99:
                ex_banner = pfgt.figlet_format(
                    "Exit",
                    font="digital"
                )
                
                print(
                    cld(
                        ex_banner,
                        "red"
                    )
                )
                
                sys.exit(0)
                
            elif hunter_choice == 0:
                os.system("clear")
                return hunter_main()
            else:
                print(
                    cld(
                        "Invalid Input!",
                        "red"
                    )
                )
                
                input(cyan + "Press any key to continue")
                
                return hunter_main()


    hunter_main()
