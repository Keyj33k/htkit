#!/usr/bin/env python3

try:
    from src.net.check_host_availability import CheckHostAvailability
    from src.crypto.password_generator import PasswordGenerator
    from src.infg.whois_lookup_for_url import WhoisLookupForURL
    from src.net.witcher_portscanner import WitcherPortscanner
    from src.infg.phonenumber_lookup import PhonenumberWhois
    from src.infg.status_code import RemoteServerStatusCode
    from src.infg.subdomain_scanner import SubdomainScanner
    from src.infg.email_extractor import EmailExtractor
    from src.infg.link_collector import LinkCollector
    from src.infg.banner_grabber import BannerGrabber
    from src.infg.ipv4_whois import IPv4Lookup
    from src.infg.url2ip import GetIPv4fromURL
    from src.infg.http_header import HTTPHeader
    from src.net.ipsweep import IPv4Sweep

    from termcolor import colored as cld
    from datetime import datetime as dtt
    from pyfiglet import figlet_format
    from subprocess import call
    from requests import get
    import pyfiglet as pfgt
    import base64 as b64
    import platform
    import psutil
    import socket
    import time
    import uuid
    import sys
    import pwd
    import re
    import os
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

m = "\033[0;35m"
y = "\033[0;33m"
g = "\033[0;32m"
w = "\033[0;37m"
c = "\033[0;36m"
r = "\033[0;31m"
o = "\033[0;93m"

USERNAME = pwd.getpwuid(os.getuid())[0]

def exit_str_err(command: str, tool: str):
    if command == 'x' or command == 'exit':
        print(f"{w}[{o}-{w}] Sorry{r},{w} But command '{command}' is"
              f" invalid{r}.{w} Please use Ctrl+C to exit {tool}{r}!{w}")

def exit_int_err(command: int, tool: str):
    if command == 0:
        print(
            f"{w}[{o}-{w}] Sorry{r},{w} But command '{command}' is "
            f"invalid{r}.{w} Please use Ctrl+C to exit {tool}{r}!{w}")

class HunterToolkit:
    def __init__(self, menu_option_choice: int):
        self.menu_option_choice = menu_option_choice

    @staticmethod
    def banner():
        print(cld(pfgt.figlet_format("Hunter", font="poison"), "white"))
        print(f" {r}<{w} by{r}@{w}keyjeek {r}> {o}Happy Hunting! {r}< {w}Ver{r}.:{w}1{r}.{w}1{r}.{w}12 {r}>")
        print(f"\n {r}[{w}*{r}] {w}Hunter {r}-{w} Penetration Testing "
              f"Assistant{r},\n\t\t{w}Information Gathering And More{r}.")

    @staticmethod
    def menu():
        print(f"{r}{'=' * 70}\n{r}[{w}0{r}]{w} Clear Screen\t\t{r}[{w}10{r}]{w} Password Generator\n"
              f"{r}[{w}1{r}]{w} Port Scanner\t\t{r}[{w}11{r}]{w} Whois URL\n"
              f"{r}[{w}2{r}]{w} Whois IPv4\t\t\t{r}[{w}12{r}]{w} HTTP Header\n"
              f"{r}[{w}3{r}]{w} Banner Grabber\t\t{r}[{w}13{r}]{w} HREF Collector\n"
              f"{r}[{w}4{r}]{w} B64 En-/Decrypt\t\t{r}[{w}14{r}]{w} Ping\n"
              f"{r}[{w}5{r}]{w} Whois Phonenumber\t\t{r}[{w}15{r}]{w} IPSweep\n"
              f"{r}[{w}6{r}]{w} Subdomain Scanner\t\t{r}[{w}16{r}]{w} Status Code\n"
              f"{r}[{w}7{r}]{w} Whoami\t\t\t{r}[{w}17{r}]{w} Email Extractor\n"
              f"{r}[{w}8{r}]{w} System Overview\t\t{r}[{w}99{r}]{w} Exit\n"
              f"{r}[{w}9{r}]{w} IPv4 Extractor Exit\n{r}{'=' * 70}\n")

    @staticmethod
    def my_system():
        try:
            while True:
                print(cld(figlet_format("MySystem", font="bulbhead"), "yellow"))
                continue_or_exit = str(input(f"{w}[{r}*{w}] {r}({w}{USERNAME}{r}@{w}Hunter{r},"
                                             f"{w} Enter to continue{r},{w} {r}'{w}x{r}'{w} to exit{r})>>{o} "))
                if continue_or_exit == 'exit' or continue_or_exit == 'x': break
                start_time = dtt.now()
                get_system = platform.uname()

                print(f"{w}{'=' * 24} {r}|{w} Sys_Info {r}|{w}{'=' * 24}\n"
                      f"{w}System {r}->{w} {get_system.system}\n"
                      f"{w}Name {r}->{w} {get_system.node}\n"
                      f"{w}Release {r}->{w} {get_system.release}\n"
                      f"{w}Version {r}->{w} {get_system.version}\n"
                      f"{w}Machine {r}->{w} {get_system.machine}\n"
                      f"{w}Processor {r}->{w} {get_system.processor}\n")

                def show_size(size):
                    for unit in ["B", "KB", "MB", "GB", "TB"]:
                        if size > 1024:
                            size = size / 1024
                        else:
                            return f"{size:.3f}{unit}"

                get_partitions = psutil.disk_partitions()
                print(f"{w}{'=' * 20} {r}|{w} Disk Information {r}|{w}{'=' * 20}")

                for part in get_partitions:
                    print(f"\n{w}Device {r}->{w} {part.device}\n"
                          f"{w}Mounted At {r}->{w} {part.mountpoint}\n"
                          f"{w}Type {r}->{w} {part.fstype}\n")

                    try:
                        part_usage = psutil.disk_usage(part.mountpoint)
                    except PermissionError:
                        continue

                    print(f"{w}Total Size {r}->{w} {show_size(part_usage.total)}\n"
                          f"{w}In Use {r}->{w} {show_size(part_usage.used)}\n"
                          f"{w}Free {r}->{w} {show_size(part_usage.free)}\n"
                          f"{w}Percentance {r}->{w} {part_usage.percent}%")

                disk_io = psutil.disk_io_counters()
                print(f"{w}Read Since Boot {r}->{w} {show_size(disk_io.read_bytes)}\n"
                      f"{w}Written Since Boot {r}->{w} {show_size(disk_io.write_bytes)}\n")

                print(f"{w}{'=' * 22} {r}|{w} CPU Info {r}|{w}{'=' * 26}\n"
                      f"{w}Cores {r}->{w} {psutil.cpu_count(logical=False)}\n"
                      f"{w}Logical Cores {r}->{w} {psutil.cpu_count(logical=True)}\n"
                      f"{w}Maximal Freq {r}->{w} {psutil.cpu_freq().max:.1f}Mhz\n"
                      f"{w}Current Freq {r}->{w} {psutil.cpu_freq().current:.1f}Mhz\n"
                      f"{w}CPU Usage {r}->{w} {psutil.cpu_percent()}%\n"
                      f"\n{w}CPU Core Usage:\n{y}")

                for core, percentance in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
                    print(f"{w}Core {core} {r}->{w} {percentance}%")

                virtual_mem = psutil.virtual_memory()
                swap = psutil.swap_memory()

                print(f"{w}{'=' * 23} {r}|{w} Ram Info {r}|{w}{'=' * 25}\n"
                      f"\n{w}Total {r}->{w} {show_size(virtual_mem.total)}\n"
                      f"\n{w}Available {r}->{w} {show_size(virtual_mem.available)}\n"
                      f"{w}In Use {r}->{w} {show_size(virtual_mem.used)}\n"
                      f"{w}Percentence {r}->{w} {show_size(virtual_mem.percent)}%\n")

                print(f"{w}{'=' * 26} {r}|{w} SWAP {r}|{w}{'=' * 26}\n"
                      f"\n{w}Total {r}->{w} {show_size(swap.total)}\n"
                      f"{w}Free {r}->{w} {show_size(swap.free)}\n"
                      f"{w}In Use {r}->{w} {show_size(swap.used)}\n"
                      f"{w}Percentence {r}->{w} {swap.percent}%\n")

                print(f"{w}{'=' * 22} {r}|{w} Network Info {r}|{w}{'=' * 22}")
                if_addrs = psutil.net_if_addrs()

                for interface_name, interface_addresses in if_addrs.items():
                    for address in interface_addresses:
                        print(f"{w}Interface {r}->{w} {interface_name}")
                        if str(address.family) == 'AddressFamily.AF_INET':
                            print(f"{w}IP {r}->{w} {address.address}\n"
                                  f"{w}Netmask {r}->{w} {address.netmask}\n"
                                  f"{w}Broadcast IP {r}->{w} {address.broadcast}\n")
                        elif str(address.family) == 'AddressFamily.AF_PACKET':
                            print(f"{w}MAC {r}->{w} {address.address}\n"
                                  f"{w}Netmask {r}->{w} {address.netmask}\n"
                                  f"{w}Broadcast MAC {r}->{w} {address.broadcast}")

                net_io = psutil.net_io_counters()
                boot_time_timestamp = psutil.boot_time()
                boot_time = dtt.fromtimestamp(boot_time_timestamp)

                print(f"{w}Total Bytes Sent {r}->{w} {show_size(net_io.bytes_sent)}\n"
                      f"{w}Total Bytes Received {r}->{w} {show_size(net_io.bytes_recv)}\n")

                print(f"{w}{'=' * 27} {r}|{w} Boot {r}|{w}{'=' * 25}\n"
                      f"{w}Last Boot {r}->{w} {boot_time.day}.{boot_time.month}.{boot_time.year} "
                      f"{boot_time.hour}:{boot_time.minute}:{boot_time.second}\n")

                print(f"{w}Job done in {dtt.now() - start_time}")
        except PermissionError as permerr:
            print(permerr)

    def hunter_gate(self):
        try:
            if self.menu_option_choice == 0:
                call(["clear"])
            elif self.menu_option_choice == 1:
                print(cld(figlet_format("Witcher", font="bulbhead"), "yellow"))
                ip_gipv4u = str(input(f"{w}[{r}*{w}] {r}({w}{USERNAME}{r}@{w}Hunter{r},{w} Address{r})>>{o} "))
                exit_str_err(ip_gipv4u, "Witcher")
                sp_gipv4u = int(input(f"{w}[{r}*{w}] {r}({w}{USERNAME}{r}@{w}Hunter{r},{w} Min{r}.{w} Port{r})>>{o} "))
                exit_int_err(sp_gipv4u, "Witcher")
                mp_gipv4u = int(input(f"{w}[{r}*{w}] {r}({w}{USERNAME}{r}@{w}Hunter{r},{w} Max{r}.{w} Port{r})>>{o} "))
                exit_int_err(mp_gipv4u, "Witcher")
                extract_ipv4 = WitcherPortscanner(ip_gipv4u, sp_gipv4u, mp_gipv4u)
                extract_ipv4.main()
            elif self.menu_option_choice == 2:
                print(cld(figlet_format("IPv4Whois", font="bulbhead"), "yellow"))
                ipv4_address = str(input(f"{w}[{r}*{w}] {r}({w}{USERNAME}{r}@{w}Hunter{r},{w} IPv4{r})>>{o} "))
                ipv4_lookup = IPv4Lookup(ipv4_address)
                ipv4_lookup.main()
            elif self.menu_option_choice == 3:
                print(cld(figlet_format("Banner\nGrabber", font="bulbhead"), "yellow"))
                ipv4_address = str(input(f"{w}[{r}*{w}] {r}({w}{USERNAME}{r}@{w}Hunter{r},{w} Address{r})>>{o} "))
                exit_str_err(ipv4_address, "Banner Grabber")
                target_port = int(input(f"{w}[{r}*{w}] {r}({w}{USERNAME}{r}@{w}Hunter{r},{w} Port{r})>>{o} "))
                exit_int_err(target_port, "Banner Grabber")
                get_service = BannerGrabber(ipv4_address, target_port)
                get_service.main()
            elif self.menu_option_choice == 4:
                while True:
                    print(cld(figlet_format("B64Crypt", font="bulbhead"), "yellow"))
                    print(f"\n\t{w}[{r}1{w}] Encoder\n"
                          f"\t{w}[{r}2{w}] Decoder\n"
                          f"\t{w}[{r}x{w}] Exit")
                    b64_choice = input(f"\n{w}[{r}*{w}] Choice {r}>>{o} ")
                    if b64_choice == "1":
                        hash_value = str(input(f"{w}[{r}*{w}] {r}({w}{USERNAME}{r}@{w}Hunter{r},{w} Value{r})>>{o} "))
                        if hash_value == 'exit' or hash_value == 'x': break

                        try:
                            print(f"{r}{'=' * 70}\n{w}[{g}+{w}] {hash_value} {r}->{w} "
                                  f"{b64.b64encode(hash_value.encode('ascii')).decode('ascii')}\n"
                                  f"{r}{'=' * 70}\n{chr(0xa)}")
                            input(f"{w}[{r}*{w}] Press enter key to continue")
                        except Exception as error:
                            print(cld(f"An error was defined: {error}", "red"))
                            input(f"{w}[{r}*{w}] Press enter key to continue")
                    elif b64_choice == "2":
                        decode_hash = str(input(f"{w}[{r}*{w}] {r}({w}{USERNAME}{r}@{w}Hunter{r},{w} Value{r})>>{o} "))
                        if decode_hash == 'exit' or decode_hash == 'x': break

                        try:
                            print(f"{r}{'=' * 70}\n{w}[{g}+{w}] {decode_hash} {r}->{w} "
                                  f"{b64.b64decode(decode_hash.encode('ascii')).decode('ascii')}\n"
                                  f"{r}{'=' * 70}\n{chr(0xa)}")
                            input(f"{w}[{r}*{w}] Press enter key to continue")
                        except Exception as error:
                            print(cld(f"An error was defined:\n{error}", "red"))
                            input(f"{w}[{r}*{w}] Press enter key to continue")
                    elif b64_choice == 'x' or b64_choice == 'exit':
                        break
                    else:
                        print(cld("Invalid Input!", "red"))
            elif self.menu_option_choice == 5:
                print(cld(figlet_format("Whois\nPhonenumber", font="bulbhead"), "yellow"))
                url_ps = str(input(f"{w}[{r}*{w}] {r}({w}{USERNAME}{r}@{w}Hunter{r},{w} Phonenumber{r})>>{o} "))
                phon_inf = PhonenumberWhois(url_ps)
                phon_inf.main()
            elif self.menu_option_choice == 6:
                print(cld(figlet_format("Subdomain\nScanner", font="bulbhead"), "yellow"))
                url_sds = str(input(f"{w}[{r}*{w}] {r}({w}{USERNAME}{r}@{w}Hunter{r},{w} URL{r})>>{o} "))
                exit_str_err(url_sds, "Subdomain Scanner")
                wordl = str(input(f"{w}[{r}*{w}] {r}({w}{USERNAME}{r}@{w}Hunter{r},{w} "
                                  f"Wordlist{r}[{w}empty for default wordlist{r}])>>{o} "))
                exit_str_err(wordl, "Subdomain Scanner")
                bruteforce_subdomains = SubdomainScanner(url_sds, wordl)
                bruteforce_subdomains.main()
            elif self.menu_option_choice == 7:
                def check_root():
                    if "SUDO_UID" in os.environ.keys():
                        return f"{w}[{g}+{w}] Type         {r}:{w}\tRoot"
                    else:
                        return f"{w}[{g}+{w}] Type         {r}:{w}\tUser"

                print(f"\n{w}\t\tWhoami\n"
                      f"{r}{'=' * 70}\n{w}[{g}+{w}] Date         {r}:{w}\t{dtt.now()}\n"
                      f"{w}[{g}+{w}] Username     {r}:{w}\t{USERNAME}\n"
                      f"{check_root()}\n"
                      f"{w}[{g}+{w}] Hostname     {r}:{w}\t{socket.gethostname()}\n"
                      f"{w}[{g}+{w}] IPAddress    {r}:{w}\t{socket.gethostbyname(socket.gethostname())}\n"
                      f"{w}[{g}+{w}] Public IPv4  {r}:{w}\t{get('https://api.ipify.org').text}\n"
                      f"{w}[{g}+{w}] MACAddress   {r}:{w}\t{':'.join(re.findall('..', '%012x' % uuid.getnode()))}\n"
                      f"{w}[{g}+{w}] Current Path {r}:{w}\t{os.path.abspath(os.getcwd())}\n{r}{'=' * 70}\n{chr(0xa)}")

                input(f"{w}[{r}*{w}] Press enter key to continue")
            elif self.menu_option_choice == 8:
                HunterToolkit.my_system()
            elif self.menu_option_choice == 9:
                print(cld(figlet_format("URL2IPv4", font="bulbhead"), "yellow"))
                url_gipv4u = str(input(f"{w}[{r}*{w}] {r}({w}{USERNAME}{r}@{w}Hunter{r},{w} URL{r})>>{o} "))
                extract_ipv4 = GetIPv4fromURL(url_gipv4u)
                extract_ipv4.main()
            elif self.menu_option_choice == 10:
                print(cld(figlet_format("Password\nGenerator", font="bulbhead"), "yellow"))
                passw_length = int(input(f"{w}[{r}*{w}] {r}({w}{USERNAME}{r}@{w}"
                                         f"Hunter{r},{w} Password length{r})>>{o} "))
                extract_ipv4 = PasswordGenerator(passw_length)
                extract_ipv4.main()
            elif self.menu_option_choice == 11:
                print(cld(figlet_format("URLWhois", font="bulbhead"), "yellow"))
                url_whois = str(input(f"{w}[{r}*{w}] {r}({w}{USERNAME}{r}@{w}Hunter{r},{w} URL{r})>>{o} "))
                get_lookup = WhoisLookupForURL(url_whois)
                get_lookup.main()
            elif self.menu_option_choice == 12:
                print(cld(figlet_format("HTTPHeader", font="bulbhead"), "yellow"))
                url_ghttph = str(input(f"{w}[{r}*{w}] {r}({w}{USERNAME}{r}@{w}Hunter{r},{w} URL{r})>>{o} "))
                httpheader = HTTPHeader(url_ghttph)
                httpheader.main()
            elif self.menu_option_choice == 13:
                print(cld(figlet_format("Link\nCollector", font="bulbhead"), "yellow"))
                url_lc = str(input(f"{w}[{r}*{w}] {r}({w}{USERNAME}{r}@{w}Hunter{r},{w} URL{r})>>{o} "))
                linkcollector = LinkCollector(url_lc)
                linkcollector.main()
            elif self.menu_option_choice == 14:
                print(cld(figlet_format("Ping", font="bulbhead"), "yellow"))
                addr = str(input(f"{w}[{r}*{w}] {r}({w}{USERNAME}{r}@{w}Hunter{r},{w} Address{r})>>{o} "))
                check = CheckHostAvailability(addr)
                check.main()
            elif self.menu_option_choice == 15:
                print(cld(figlet_format("IPSweep", font="bulbhead"), "yellow"))
                ipv4 = str(input(f"{w}[{r}*{w}] {r}({w}{USERNAME}{r}@{w}Hunter{r},"
                                 f"{w} IPv4 Address(First Three Octets Only){r})>>{o} "))
                exit_str_err(ipv4, "IPSweep")
                start_range = int(input(f"{w}[{r}*{w}] {r}({w}{USERNAME}{r}@{w}Hunter{r},{w} Start Range{r})>>{o} "))
                exit_int_err(start_range, "IPSweep")
                last_range = int(input(f"{w}[{r}*{w}] {r}({w}{USERNAME}{r}@{w}Hunter{r},{w} Last Range{r})>>{o} "))
                exit_int_err(last_range, "IPSweep")
                ping_count = str(input(f"{w}[{r}*{w}] {r}({w}{USERNAME}{r}@{w}Hunter{r},{w} Ping Count{r})>>{o} "))
                exit_str_err(ping_count, "IPSweep")
                ipsweep = IPv4Sweep(ipv4, start_range, last_range, ping_count)
                ipsweep.get_status()
            elif self.menu_option_choice == 16:
                print(cld(figlet_format("GetStat", font="bulbhead"), "yellow"))
                gs_url = str(input(f"{w}[{r}*{w}] {r}({w}{USERNAME}{r}@{w}Hunter{r},{w} Address{r})>>{o} "))
                status_code = RemoteServerStatusCode(gs_url)
                status_code.get_code()
            elif self.menu_option_choice == 17:
                print(cld(figlet_format("GetMail", font="bulbhead"), "yellow"))
                gm_url = str(input(f"{w}[{r}*{w}] {r}({w}{USERNAME}{r}@{w}Hunter{r},{w} Full URL{r})>>{o} "))
                extract_mail_addr = EmailExtractor(gm_url)
                extract_mail_addr.extract_mail_address()
            elif self.menu_option_choice == 99:
                sys.exit(f"\n{w}[{r}*{w}] Goodbye{r},{w} {USERNAME}{r}.{w} Follow the white rabbit {r}...\n")
            else:
                print(f"\n{w}[{y}-{w}] Invalid Input{r}!")
        except KeyboardInterrupt:
            print(f"\n{w}[{y}-{w}] You pressed Ctrl{r}+{w}C{r}.{w} Exit{r}!")
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
            start = str(input(f"{w}[{r}*{w}] Accept{r}?{w} y{r}/{w}n{o} "))
            if start == 'y' or start == 'Y':
                break
            elif start == 'n' or start == 'N':
                sys.exit(f"{w}[{r}*{w}] You need to accept the terms to use the Hunter-Toolkit{r}.{w} Exit {r}...\n")
            else:
                print(f"\n{w}[{y}-{w}] Only 'y/Y' or 'n/N' are allowed{r}!")
        except KeyboardInterrupt:
            sys.exit(f"\n{w}[{y}-{w}] You pressed Ctrl{r}+{w}C{r}.{w} Exit{r}!")

    while True:
        try:
            HunterToolkit.banner()
            HunterToolkit.menu()
            hunter_toolkit = HunterToolkit(int(input(f"{r}({w}{USERNAME}{r}@{w}Hunter{r})>>{o} ")))
            hunter_toolkit.hunter_gate()
        except KeyboardInterrupt:
            sys.exit(f"\n{w}[{y}-{w}] You pressed Ctrl{r}+{w}C{r}.{w} Exit{r}!")
        except ValueError:
            print(f"\n{w}[{y}-{w}] You need to enter a integer value{r}!")
