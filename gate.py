#!/usr/bin/env python3

try:
    from src.infg.whois_lookup_for_url import WhoisLookupForURL
    from src.infg.phonenumber_lookup import PhonenumberWhois
    from src.infg.status_code import RemoteServerStatusCode
    from src.infg.subdomain_scanner import SubdomainScanner
    from src.infg.email_extractor import EmailExtractor
    from src.infg.href_collector import HREFCollector
    from src.infg.banner_grabber import BannerGrabber
    from src.infg.ipv4_whois import IPv4Lookup
    from src.infg.url2ip import GetIPv4fromURL
    from src.infg.http_header import HTTPHeader

    from src.crypto.password_generator import PasswordGenerator
    from src.crypto.b64_crypt import Crypt

    from src.net.check_host_availability import CheckHostAvailability
    from src.net.witcher_portscanner import WitcherPortscanner
    from src.net.ipsweep import IPv4Sweep

    from src.system.system_inf import SystemInformations

    from termcolor import colored as cld
    from pyfiglet import figlet_format
    from subprocess import call
    from sys import exit
    from pwd import getpwuid
    from os import getuid
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
#   Contact :   K3yjeek@proton.me         #
#   Github  :   @Keyj33k                  #
#   Version :   1.1.13                    #
#                                         #
# # # # # # # # # # # # # # # # # # # # # #

Y = "\033[0;33m"
G = "\033[0;32m"
W = "\033[0;37m"
R = "\033[0;31m"

USERNAME = getpwuid(getuid())[0]

def exit_str_err(command: str, tool: str):
    if command == 'x' or command == "exit":
        print(f"{W}[{Y}-{W}] Error{R}:{W} {R}'{W}{command}{R}'{W} is"
              f" invalid{R}.{W} Please use Ctrl{R}+{W}C to exit {tool}{R}!{W}")

def exit_int_err(command: int, tool: str):
    if command == 0:
        print(f"{W}[{Y}-{W}] Error{R}:{W} {R}'{W}{command}{R}'{W} is "
              f"invalid{R}.{W} Please use Ctrl{R}+{W}C to exit {tool}{R}!{W}")

class HunterToolkit:
    def __init__(self, service: int):
        self.service = service

    @staticmethod
    def banner():
        print(cld(figlet_format("Hunter", font="poison"), "white"))
        print(f"\t{R}[{W} by{R}@{W}keyjeek {R}| {W}Toolkit{R} |{W} Ver{R}.:{W}1{R}.{W}1{R}.{W}13 {R}]\n")

    @staticmethod
    def menu():
        print(f" {R}[{W}0{R}]{W} Clear Screen\t\t{R}[{W}10{R}]{W} Password Generator\n" 
              f" {R}[{W}1{R}]{W} Port Scanner\t\t{R}[{W}11{R}]{W} Whois URL\n"
              f" {R}[{W}2{R}]{W} Whois IPv4\t\t\t{R}[{W}12{R}]{W} HTTP Header Grabber\n"
              f" {R}[{W}3{R}]{W} Banner Grabber\t\t{R}[{W}13{R}]{W} HREF Collector\n"
              f" {R}[{W}4{R}]{W} B64 En-/Decrypt\t\t{R}[{W}14{R}]{W} Ping\n"
              f" {R}[{W}5{R}]{W} Whois Phonenumber\t\t{R}[{W}15{R}]{W} IPSweep\n"
              f" {R}[{W}6{R}]{W} Subdomain Scanner\t\t{R}[{W}16{R}]{W} Status Code\n"
              f" {R}[{W}7{R}]{W} Whoami\t\t\t{R}[{W}17{R}]{W} Email Extractor\n"
              f" {R}[{W}8{R}]{W} System Overview\n"
              f" {R}[{W}9{R}]{W} IP Extractor\t\t{R}[{W}99{R}]{W} Exit\n")

    def hunter_gate(self):
        try:
            match self.service:
                case 0:
                    call(["clear"])
                case 1:
                    print(cld(figlet_format("port\nscanner", font="bulbhead"), "yellow"))
                    address = str(input(f"{W}[{R}*{W}] {W}{USERNAME}{R}@{W}Hunter{R},{W} Address{R} >>{Y} "))
                    exit_str_err(address, "Witcher")
                    start_port = int(input(f"{W}[{R}*{W}] {W}{USERNAME}{R}@{W}Hunter{R},{W} Min{R}.{W} Port{R} >>{Y} "))
                    exit_int_err(start_port, "Witcher")
                    last_port = int(input(f"{W}[{R}*{W}] {W}{USERNAME}{R}@{W}Hunter{R},{W} Max{R}.{W} Port{R} >>{Y} "))
                    exit_int_err(last_port, "Witcher")
                    port_scanner = WitcherPortscanner(address, start_port, last_port)
                    port_scanner.main()
                case 2:
                    print(cld(figlet_format("IPv4Whois", font="bulbhead"), "yellow"))
                    ipv4_address = str(input(f"{W}[{R}*{W}] {W}{USERNAME}{R}@{W}Hunter{R},{W} IPv4 {R}>>{Y} "))
                    exit_str_err(ipv4_address, "IPv4 Whois")
                    ip_lookup = IPv4Lookup(ipv4_address)
                    ip_lookup.main()
                case 3:
                    print(cld(figlet_format("Banner\nGrabber", font="bulbhead"), "yellow"))
                    ipv4_address = str(input(f"{W}[{R}*{W}] {W}{USERNAME}{R}@{W}Hunter{R},{W} Address{R} >>{Y} "))
                    exit_str_err(ipv4_address, "Banner Grabber")
                    target_port = int(input(f"{W}[{R}*{W}] {W}{USERNAME}{R}@{W}Hunter{R},{W} Port{R} >>{Y} "))
                    exit_int_err(target_port, "Banner Grabber")
                    banner_grabber = BannerGrabber(ipv4_address, target_port)
                    banner_grabber.main()
                case 4:
                    Crypt.main()
                case 5:
                    print(cld(figlet_format("Whois\nPhonenumber", font="bulbhead"), "yellow"))
                    target_phonenumber = str(input(f"{W}[{R}*{W}] {W}{USERNAME}{R}@{W}Hunter{R},{W} Phonenumber{R} >>{Y} "))
                    exit_str_err(target_phonenumber, "Phonenumber Whois")
                    phonenumber_whois = PhonenumberWhois(target_phonenumber)
                    phonenumber_whois.main()
                case 6:
                    print(cld(figlet_format("Subdomain\nScanner", font="bulbhead"), "yellow"))
                    url = str(input(f"{W}[{R}*{W}] {W}{USERNAME}{R}@{W}Hunter{R},{W} URL{R} >>{Y} "))
                    exit_str_err(url, "Subdomain Scanner")
                    wordlist = str(input(f"{W}[{R}*{W}] {W}{USERNAME}{R}@{W}Hunter{R},{W} "
                                      f"Wordlist{R}({W}empty for default wordlist{R}) >>{Y} "))
                    exit_str_err(wordlist, "Subdomain Scanner")
                    subdomain_scanner = SubdomainScanner(url, wordlist)
                    subdomain_scanner.main()
                case 7:
                    SystemInformations.details()
                case 8:
                    SystemInformations.overview()
                case 9:
                    print(cld(figlet_format("ipextract", font="bulbhead"), "yellow"))
                    url = str(input(f"{W}[{R}*{W}] {W}{USERNAME}{R}@{W}Hunter{R},{W} URL{R} >>{Y} "))
                    exit_str_err(url, "IP Extractor")
                    ip_extractor = GetIPv4fromURL(url)
                    ip_extractor.main()
                case 10:
                    print(cld(figlet_format("Password\nGenerator", font="bulbhead"), "yellow"))
                    password_length = int(input(f"{W}[{R}*{W}] {W}{USERNAME}{R}@{W}"
                                             f"Hunter{R},{W} Password length{R} >>{Y} "))
                    exit_int_err(password_length, "Password Generator")
                    password_generator = PasswordGenerator(password_length)
                    password_generator.main()
                case 11:
                    print(cld(figlet_format("URLWhois", font="bulbhead"), "yellow"))
                    url = str(input(f"{W}[{R}*{W}] {W}{USERNAME}{R}@{W}Hunter{R},{W} URL{R} >>{Y} "))
                    exit_str_err(url, "URL Whois")
                    url_lookup = WhoisLookupForURL(url)
                    url_lookup.main()
                case 12:
                    print(cld(figlet_format("Header\nGrabber", font="bulbhead"), "yellow"))
                    url = str(input(f"{W}[{R}*{W}] {W}{USERNAME}{R}@{W}Hunter{R},{W} URL{R} >>{Y} "))
                    exit_str_err(url, "Header Grabber")
                    header_grabber = HTTPHeader(url)
                    header_grabber.main()
                case 13:
                    print(cld(figlet_format("HREF\nCollector", font="bulbhead"), "yellow"))
                    url = str(input(f"{W}[{R}*{W}] {W}{USERNAME}{R}@{W}Hunter{R},{W} URL{R} >>{Y} "))
                    exit_str_err(url, "HREF Collector")
                    href_collector = HREFCollector(url)
                    href_collector.main()
                case 14:
                    print(cld(figlet_format("Ping", font="bulbhead"), "yellow"))
                    address = str(input(f"{W}[{R}*{W}] {W}{USERNAME}{R}@{W}Hunter{R},{W} Address{R} >>{Y} "))
                    exit_str_err(address, "Ping")
                    ping_count = str(input(f"{W}[{R}*{W}] {W}{USERNAME}{R}@{W}Hunter{R},{W}"
                                           f" Ping Count {R}({W} Enter for default {R}) >>{Y} "))
                    exit_str_err(ping_count, "Ping")
                    ping = CheckHostAvailability(address, ping_count)
                    ping.main()
                case 15:
                    print(cld(figlet_format("IPSweep", font="bulbhead"), "yellow"))
                    value_to_build = str(input(f"{W}[{R}*{W}] {W}{USERNAME}{R}@{W}Hunter{R},"
                                     f"{W} IPv4 Address {R}({W} First Three Octets Only {R}) >>{Y} "))
                    exit_str_err(value_to_build, "IPSweep")
                    start_range = int(input(f"{W}[{R}*{W}] {W}{USERNAME}{R}@{W}Hunter{R},{W} Start Range{R} >>{Y} "))
                    exit_int_err(start_range, "IPSweep")
                    last_range = int(input(f"{W}[{R}*{W}] {W}{USERNAME}{R}@{W}Hunter{R},{W} Last Range{R} >>{Y} "))
                    exit_int_err(last_range, "IPSweep")
                    ping_count = str(input(f"{W}[{R}*{W}] {W}{USERNAME}{R}@{W}Hunter{R},{W} Ping Count "
                                           f"{R}({W} Enter for default {R}) >>{Y} "))
                    exit_str_err(ping_count, "IPSweep")
                    ipsweep = IPv4Sweep(value_to_build, start_range, last_range, ping_count)
                    ipsweep.get_status()
                case 16:
                    print(cld(figlet_format("Code\nGrabber", font="bulbhead"), "yellow"))
                    url = str(input(f"{W}[{R}*{W}] {R}({W}{USERNAME}{R}@{W}Hunter{R},{W} Address {R}>>{Y} "))
                    exit_str_err(url, "Code Grabber")
                    status_code_grabber = RemoteServerStatusCode(url)
                    status_code_grabber.main()
                case 17:
                    print(cld(figlet_format("Email\nExtractor", font="bulbhead"), "yellow"))
                    url = str(input(f"{W}[{R}*{W}] {W}{USERNAME}{R}@{W}Hunter{R},{W} Full URL {R}>>{Y} "))
                    exit_str_err(url, "Email Extractor")
                    email_extractor = EmailExtractor(url)
                    email_extractor.main()
                case 99:
                    exit(f"\n{W}[{R}*{W}] Goodbye{R},{W} {USERNAME}{R}.{W} Follow the white rabbit {R}...\n")
                case _:
                    raise RuntimeError(f"\n{W}[{Y}-{W}] Invalid Input{R}!")
        except KeyboardInterrupt:
            print(f"\n{W}[{Y}-{W}] You pressed Ctrl{R}+{W}C{R}.{W} Exit{R}!")
        except Exception as exc:
            print(f"{W}[{Y}-{W}] Error{R}:{W} {exc}")


if __name__ == "__main__":
    while True:
        print(cld("""
 Welcome To The Hunter Toolkit!

 Before you can use this project, there are some things you need 
 to know:

 Disclaimer

 Please note that actions like port scanning etc. can be illegal. 
 If you want to use this toolkit, you need to accept the 
 following conditions:

 1) Respect the privacy of others.
 2) Always think before you type.
 3) Don't hack if you don't have any permissions to.

 Note

 - This tool is made for ethical purposes only 
 - I'm not responsible for your actions.
 - With great force follows great responsibility

 If you agree the conditions type 'y' and 'n' for decline.
        \n""", "red"))

        try:
            start = str(input(f"{W}[{R}*{W}] Accept{R}?{W} y{R}/{W}n{Y} "))
            if start == 'y' or start == 'Y': break
            elif start == 'n' or start == 'N':
                exit(f"\n{W}[{R}*{W}] You need to accept the terms to use the Hunter-Toolkit{R}.{W} Exit {R}...")
            else:
                print(f"\n{W}[{Y}-{W}] Only 'y{R}/{W}Y' or 'n{R}/{W}N' are allowed{R}!")
        except KeyboardInterrupt:
            exit(f"\n{W}[{Y}-{W}] You pressed Ctrl{R}+{W}C{R}.{W} Exit{R}!")

    while True:
        try:
            HunterToolkit.banner()
            HunterToolkit.menu()
            hunter_toolkit = HunterToolkit(int(input(f"{W}{USERNAME}{R}@{W}Hunter {R}>>{Y} ")))
            hunter_toolkit.hunter_gate()
        except KeyboardInterrupt:
            exit(f"\n{W}[{Y}-{W}] You pressed Ctrl{R}+{W}C{R}.{W} Exit{R}!")
        except ValueError:
            print(f"\n{W}[{Y}-{W}] You need to enter a integer value{R}!")
