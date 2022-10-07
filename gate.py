#!/usr/bin/env python3

try:
    from src.infg.whois_lookup_for_url import WhoisLookupForURL
    from src.infg.phonenumber_lookup import PhonenumberWhois
    from src.infg.status_code import RemoteServerStatusCode
    from src.infg.subdomain_scanner import SubdomainScanner
    from src.infg.email_extractor import EmailExtractor
    from src.infg.link_collector import LinkCollector
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
    from datetime import datetime as dtt
    from pyfiglet import figlet_format
    from subprocess import call
    import sys
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
#   Version :   1.1.12                    #
#                                         #
# # # # # # # # # # # # # # # # # # # # # #

Y = "\033[0;33m"
G = "\033[0;32m"
W = "\033[0;37m"
R = "\033[0;31m"

USERNAME = getpwuid(getuid())[0]

def exit_str_err(command: str, tool: str):
    if command == 'x' or command == 'exit':
        print(f"{W}[{Y}-{W}] Sorry{R},{W} But command '{command}' is"
              f" invalid{R}.{W} Please use Ctrl+C to exit {tool}{R}!{W}")

def exit_int_err(command: int, tool: str):
    if command == 0:
        print(
            f"{W}[{Y}-{W}] Sorry{R},{W} But command '{command}' is "
            f"invalid{R}.{W} Please use Ctrl+C to exit {tool}{R}!{W}")

class HunterToolkit:
    def __init__(self, menu_option_choice: int):
        self.menu_option_choice = menu_option_choice

    @staticmethod
    def banner():
        print(cld(figlet_format("Hunter", font="poison"), "white"))
        print(f" {R}<{W} by{R}@{W}keyjeek {R}> {Y}Happy Hunting! {R}< {W}Ver{R}.:{W}1{R}.{W}1{R}.{W}12 {R}>")
        print(f"\n {R}[{W}*{R}] {W}Hunter {R}-{W} Penetration Testing "
              f"Assistant{R},\n\t\t{W}Information Gathering And More{R}.")

    @staticmethod
    def menu():
        print(f"{R}{'=' * 70}\n{R}[{W}0{R}]{W} Clear Screen\t\t{R}[{W}10{R}]{W} Password Generator\n"
              f"{R}[{W}1{R}]{W} Port Scanner\t\t{R}[{W}11{R}]{W} Whois URL\n"
              f"{R}[{W}2{R}]{W} Whois IPv4\t\t\t{R}[{W}12{R}]{W} HTTP Header\n"
              f"{R}[{W}3{R}]{W} Banner Grabber\t\t{R}[{W}13{R}]{W} HREF Collector\n"
              f"{R}[{W}4{R}]{W} B64 En-/Decrypt\t\t{R}[{W}14{R}]{W} Ping\n"
              f"{R}[{W}5{R}]{W} Whois Phonenumber\t\t{R}[{W}15{R}]{W} IPSweep\n"
              f"{R}[{W}6{R}]{W} Subdomain Scanner\t\t{R}[{W}16{R}]{W} Status Code\n"
              f"{R}[{W}7{R}]{W} Whoami\t\t\t{R}[{W}17{R}]{W} Email Extractor\n"
              f"{R}[{W}8{R}]{W} System Overview\t\t{R}[{W}99{R}]{W} Exit\n"
              f"{R}[{W}9{R}]{W} IPv4 Extractor\n{R}{'=' * 70}\n")

    def hunter_gate(self):
        try:
            if self.menu_option_choice == 0: call(["clear"])
            elif self.menu_option_choice == 1:
                print(cld(figlet_format("Witcher", font="bulbhead"), "yellow"))
                ip_gipv4u = str(input(f"{W}[{R}*{W}] {R}({W}{USERNAME}{R}@{W}Hunter{R},{W} Address{R})>>{Y} "))
                exit_str_err(ip_gipv4u, "Witcher")
                sp_gipv4u = int(input(f"{W}[{R}*{W}] {R}({W}{USERNAME}{R}@{W}Hunter{R},{W} Min{R}.{W} Port{R})>>{Y} "))
                exit_int_err(sp_gipv4u, "Witcher")
                mp_gipv4u = int(input(f"{W}[{R}*{W}] {R}({W}{USERNAME}{R}@{W}Hunter{R},{W} Max{R}.{W} Port{R})>>{Y} "))
                exit_int_err(mp_gipv4u, "Witcher")
                extract_ipv4 = WitcherPortscanner(ip_gipv4u, sp_gipv4u, mp_gipv4u)
                extract_ipv4.main()
            elif self.menu_option_choice == 2:
                print(cld(figlet_format("IPv4Whois", font="bulbhead"), "yellow"))
                ipv4_address = str(input(f"{W}[{R}*{W}] {R}({W}{USERNAME}{R}@{W}Hunter{R},{W} IPv4{R})>>{Y} "))
                ipv4_lookup = IPv4Lookup(ipv4_address)
                ipv4_lookup.main()
            elif self.menu_option_choice == 3:
                print(cld(figlet_format("Banner\nGrabber", font="bulbhead"), "yellow"))
                ipv4_address = str(input(f"{W}[{R}*{W}] {R}({W}{USERNAME}{R}@{W}Hunter{R},{W} Address{R})>>{Y} "))
                exit_str_err(ipv4_address, "Banner Grabber")
                target_port = int(input(f"{W}[{R}*{W}] {R}({W}{USERNAME}{R}@{W}Hunter{R},{W} Port{R})>>{Y} "))
                exit_int_err(target_port, "Banner Grabber")
                get_service = BannerGrabber(ipv4_address, target_port)
                get_service.main()
            elif self.menu_option_choice == 4:
                Crypt.main()
            elif self.menu_option_choice == 5:
                print(cld(figlet_format("Whois\nPhonenumber", font="bulbhead"), "yellow"))
                url_ps = str(input(f"{W}[{R}*{W}] {R}({W}{USERNAME}{R}@{W}Hunter{R},{W} Phonenumber{R})>>{Y} "))
                phon_inf = PhonenumberWhois(url_ps)
                phon_inf.main()
            elif self.menu_option_choice == 6:
                print(cld(figlet_format("Subdomain\nScanner", font="bulbhead"), "yellow"))
                url_sds = str(input(f"{W}[{R}*{W}] {R}({W}{USERNAME}{R}@{W}Hunter{R},{W} URL{R})>>{Y} "))
                exit_str_err(url_sds, "Subdomain Scanner")
                wordl = str(input(f"{W}[{R}*{W}] {R}({W}{USERNAME}{R}@{W}Hunter{R},{W} "
                                  f"Wordlist{R}[{W}empty for default wordlist{R}])>>{Y} "))
                exit_str_err(wordl, "Subdomain Scanner")
                bruteforce_subdomains = SubdomainScanner(url_sds, wordl)
                bruteforce_subdomains.main()
            elif self.menu_option_choice == 7:
                SystemInformations.details()
            elif self.menu_option_choice == 8:
                SystemInformations.overview()
            elif self.menu_option_choice == 9:
                print(cld(figlet_format("URL2IPv4", font="bulbhead"), "yellow"))
                url_gipv4u = str(input(f"{W}[{R}*{W}] {R}({W}{USERNAME}{R}@{W}Hunter{R},{W} URL{R})>>{Y} "))
                extract_ipv4 = GetIPv4fromURL(url_gipv4u)
                extract_ipv4.main()
            elif self.menu_option_choice == 10:
                print(cld(figlet_format("Password\nGenerator", font="bulbhead"), "yellow"))
                passw_length = int(input(f"{W}[{R}*{W}] {R}({W}{USERNAME}{R}@{W}"
                                         f"Hunter{R},{W} Password length{R})>>{Y} "))
                extract_ipv4 = PasswordGenerator(passw_length)
                extract_ipv4.main()
            elif self.menu_option_choice == 11:
                print(cld(figlet_format("URLWhois", font="bulbhead"), "yellow"))
                url_whois = str(input(f"{W}[{R}*{W}] {R}({W}{USERNAME}{R}@{W}Hunter{R},{W} URL{R})>>{Y} "))
                get_lookup = WhoisLookupForURL(url_whois)
                get_lookup.main()
            elif self.menu_option_choice == 12:
                print(cld(figlet_format("HTTPHeader", font="bulbhead"), "yellow"))
                url_ghttph = str(input(f"{W}[{R}*{W}] {R}({W}{USERNAME}{R}@{W}Hunter{R},{W} URL{R})>>{Y} "))
                httpheader = HTTPHeader(url_ghttph)
                httpheader.main()
            elif self.menu_option_choice == 13:
                print(cld(figlet_format("Link\nCollector", font="bulbhead"), "yellow"))
                url_lc = str(input(f"{W}[{R}*{W}] {R}({W}{USERNAME}{R}@{W}Hunter{R},{W} URL{R})>>{Y} "))
                linkcollector = LinkCollector(url_lc)
                linkcollector.main()
            elif self.menu_option_choice == 14:
                print(cld(figlet_format("Ping", font="bulbhead"), "yellow"))
                addr = str(input(f"{W}[{R}*{W}] {R}({W}{USERNAME}{R}@{W}Hunter{R},{W} Address{R})>>{Y} "))
                check = CheckHostAvailability(addr)
                check.main()
            elif self.menu_option_choice == 15:
                print(cld(figlet_format("IPSweep", font="bulbhead"), "yellow"))
                ipv4 = str(input(f"{W}[{R}*{W}] {R}({W}{USERNAME}{R}@{W}Hunter{R},"
                                 f"{W} IPv4 Address(First Three Octets Only){R})>>{Y} "))
                exit_str_err(ipv4, "IPSweep")
                start_range = int(input(f"{W}[{R}*{W}] {R}({W}{USERNAME}{R}@{W}Hunter{R},{W} Start Range{R})>>{Y} "))
                exit_int_err(start_range, "IPSweep")
                last_range = int(input(f"{W}[{R}*{W}] {R}({W}{USERNAME}{R}@{W}Hunter{R},{W} Last Range{R})>>{Y} "))
                exit_int_err(last_range, "IPSweep")
                ping_count = str(input(f"{W}[{R}*{W}] {R}({W}{USERNAME}{R}@{W}Hunter{R},{W} Ping Count{R})>>{Y} "))
                exit_str_err(ping_count, "IPSweep")
                ipsweep = IPv4Sweep(ipv4, start_range, last_range, ping_count)
                ipsweep.get_status()
            elif self.menu_option_choice == 16:
                print(cld(figlet_format("GetStat", font="bulbhead"), "yellow"))
                gs_url = str(input(f"{W}[{R}*{W}] {R}({W}{USERNAME}{R}@{W}Hunter{R},{W} Address{R})>>{Y} "))
                status_code = RemoteServerStatusCode(gs_url)
                status_code.get_code()
            elif self.menu_option_choice == 17:
                print(cld(figlet_format("GetMail", font="bulbhead"), "yellow"))
                gm_url = str(input(f"{W}[{R}*{W}] {R}({W}{USERNAME}{R}@{W}Hunter{R},{W} Full URL{R})>>{Y} "))
                extract_mail_addr = EmailExtractor(gm_url)
                extract_mail_addr.extract_mail_address()
            elif self.menu_option_choice == 99:
                sys.exit(f"\n{W}[{R}*{W}] Goodbye{R},{W} {USERNAME}{R}.{W} Follow the white rabbit {R}...\n")
            else:
                print(f"\n{W}[{Y}-{W}] Invalid Input{R}!")
        except KeyboardInterrupt:
            print(f"\n{W}[{Y}-{W}] You pressed Ctrl{R}+{W}C{R}.{W} Exit{R}!")
        except Exception as exc:
            print(exc)


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
                sys.exit(f"\n{W}[{R}*{W}] You need to accept the terms to use the Hunter-Toolkit{R}.{W} Exit {R}...")
            else:
                print(f"\n{W}[{Y}-{W}] Only 'y/Y' or 'n/N' are allowed{R}!")
        except KeyboardInterrupt:
            sys.exit(f"\n{W}[{Y}-{W}] You pressed Ctrl{R}+{W}C{R}.{W} Exit{R}!")

    while True:
        try:
            HunterToolkit.banner()
            HunterToolkit.menu()
            hunter_toolkit = HunterToolkit(int(input(f"{R}({W}{USERNAME}{R}@{W}Hunter{R})>>{Y} ")))
            hunter_toolkit.hunter_gate()
        except KeyboardInterrupt:
            sys.exit(f"\n{W}[{Y}-{W}] You pressed Ctrl{R}+{W}C{R}.{W} Exit{R}!")
        except ValueError:
            print(f"\n{W}[{Y}-{W}] You need to enter a integer value{R}!")
