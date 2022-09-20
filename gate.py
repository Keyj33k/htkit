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
    from src.infg.get_http_header import GetHTTPHeader
    from src.infg.link_collector import LinkCollector
    from src.infg.banner_grabber import BannerGrabber
    from src.crypto.md5encrypt import MD5Encrypt
    from src.infg.ipv4_whois import IPv4Lookup
    from src.infg.url2ip import GetIPv4fromURL
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
#   Contact :   nomotikag33n@gmail.com    #
#   Github  :   @Keyj33k                  #
#   Version :   1.1.11                    #
#                                         #
# # # # # # # # # # # # # # # # # # # # # #

m = "\033[0;35m"
y = "\033[0;33m"
g = "\033[0;32m"
w = "\033[0;37m"
c = "\033[0;36m"
r = "\033[0;31m"
o = "\033[0;93m"


class HunterToolkit:

    def __init__(self, menu_option_choice: int):
        self.menu_option_choice = menu_option_choice

    @staticmethod
    def banner():
        print(cld(pfgt.figlet_format("Hunter", font="poison"), "white"))
        print(f" {r}<{w} by{r}@{w}keyjeek {r}> {o}Happy Hunting! {r}< {w}Ver{r}.:{w}1{r}.{w}1{r}.{w}11 {r}>")
        print(f"\n {r}[{w}*{r}] {w}Hunter {r}-{w} Penetration Testing Assistant{r},\n\t\t{w}Information Gathering And More{r}.")

    @staticmethod
    def menu():
        print(f"{r}=" * 70)
        print(f"{r}[{w}0{r}]{w} Clear Screen\t\t{r}[{w}10{r}]{w} Extract IPv4 From URL")
        print(f"{r}[{w}1{r}]{w} Port Scanner\t\t{r}[{w}11{r}]{w} Password Generator")
        print(f"{r}[{w}2{r}]{w} MD5 Encryption\t\t{r}[{w}12{r}]{w} Whois URL")
        print(f"{r}[{w}3{r}]{w} Whois IPv4\t\t\t{r}[{w}13{r}]{w} Get HTTP Header")
        print(f"{r}[{w}4{r}]{w} Banner Grabber\t\t{r}[{w}14{r}]{w} HREF Collector")
        print(f"{r}[{w}5{r}]{w} B64 En-/Decrypt\t\t{r}[{w}15{r}]{w} Ping")
        print(f"{r}[{w}6{r}]{w} Whois Phonenumber\t\t{r}[{w}16{r}]{w} IPSweep")
        print(f"{r}[{w}7{r}]{w} Subdomain Scanner\t\t{r}[{w}17{r}]{w} External Tools")
        print(f"{r}[{w}8{r}]{w} Whoami\t\t\t{r}[{w}18{r}]{w} Get Status Code")
        print(f"{r}[{w}9{r}]{w} System Overview\t\t{r}[{w}19{r}]{w} Extract Email Addresses from URL")
        print(f"{r}[{w}99{r}]{w} Exit")
        print(f"{r}=" * 70)

    @staticmethod
    def my_system():
        try:
            while True:
                print(cld(figlet_format("MySystem", font="bulbhead"), "yellow"))

                continue_or_exit = str(input(f"{w}[{r}*{w}] {r}({w}{pwd.getpwuid(os.getuid())[0]}{r}@{w}Hunter{r},{w} Enter to continue{r},{w} 'x' to exit{r})>>{o} "))
                start_time = dtt.now()

                if continue_or_exit == 'exit' or continue_or_exit == 'x':
                    break

                get_system = platform.uname()

                print(f"{m}=" * 24, f"{c}|{m} Sys_Info {c}|{m}", f"{m}=" * 24)
                print(f"\n{c}System {m}-> {y}{get_system.system}")
                print(f"{c}Name {m}-> {y}{get_system.node}")
                print(f"{c}Release {m}-> {y}{get_system.release}")
                print(f"{c}Version {m}-> {y}{get_system.version}")
                print(f"{c}Machine {m}-> {y}{get_system.machine}")
                print(f"{c}Processor {m}-> {y}{get_system.processor} \n")

                def show_size(size):
                    f = 1024
                    for t in ["B", "KB", "MB", "GB", "TB"]:
                        if size > f:
                            size = size / f
                        else:
                            return f"{size:.3f}{t}"  # output formatted to 3 decimal places

                get_partitions = psutil.disk_partitions()

                print(f"{m}=" * 20, f"{c}|{m} Disk Information {c}|{m}", "=" * 20)

                for part in get_partitions:
                    print(f"\n{c}Device {m}-> {y}{part.device}")
                    print(f"{c}Mounted At {m}-> {y}{part.mountpoint}")
                    print(f"{c}Type {m}-> {y}{part.fstype}")

                    try:
                        part_usage = psutil.disk_usage(part.mountpoint)
                    except PermissionError:
                        continue

                    print(f"{c}Total Size {m}-> {y}{show_size(part_usage.total)}")
                    print(f"{c}In Use {m}-> {y}{show_size(part_usage.used)}")
                    print(f"{c}Free {m}-> {y}{show_size(part_usage.free)}")
                    print(f"{c}Percentance {m}-> {y}{part_usage.percent}%")

                disk_io = psutil.disk_io_counters()

                print(f"{c}Read Since Boot {m}-> {y}{show_size(disk_io.read_bytes)}")
                print(f"{c}Written Since Boot {m}-> {y}{show_size(disk_io.write_bytes)} \n")
                print(f"{m}=" * 22, f"{c}|{m} CPU_Info {c}|{m}", "=" * 26)
                print(f"\n{c}Cores {m}-> {y}{psutil.cpu_count(logical=False)}")
                print(f"{c}Logical Cores {m}-> {y}{psutil.cpu_count(logical=True)}")
                print(f"{c}Maximal Freq {m}-> {y}{psutil.cpu_freq().max:.1f}Mhz")
                print(f"{c}Current Freq {m}-> {y}{psutil.cpu_freq().current:.1f}Mhz")
                print(f"{c}CPU Usage {m}-> {y}{psutil.cpu_percent()}%")
                print(f"\n{c}CPU Core Usage: \n{y}")

                for core, percentance in enumerate(
                        psutil.cpu_percent(
                            percpu=True,
                            interval=1
                        )
                ):  
                    print(f"{c}Core {core} {m}-> {y}{percentance}% ")

                virtual_mem = psutil.virtual_memory()
                swap = psutil.swap_memory()

                print(f"{m}=" * 23, f"{c}|{m} RAM_Info {c}|{m}", "=" * 25)
                print(f"\n{c}Total {m}-> {y}{show_size(virtual_mem.total)}")
                print(f"\n{c}Available {m}-> {y}{show_size(virtual_mem.available)}")
                print(f"{c}In Use {m}-> {y}{show_size(virtual_mem.used)}")
                print(f"{c}Percentence {m}-> {y}{show_size(virtual_mem.percent)}% \n")
                print(f"{m}=" * 26, f"{c}|{m} SWAP {c}|{m}", "=" * 26)
                print(f"\n{c}Total {m}-> {y}{show_size(swap.total)}")
                print(f"{c}Free {m}-> {y}{show_size(swap.free)}")
                print(f"{c}In Use {m}-> {y}{show_size(swap.used)}")
                print(f"{c}Percentence {m}-> {y}{swap.percent}%\n")
                print(f"{m}=" * 18, f"{c}|{m} Network Information {c}|{m}", "=" * 19)

                if_addrs = psutil.net_if_addrs()

                for interface_name, interface_addresses in if_addrs.items():
                    for address in interface_addresses:
                        print(f"{c}Interface {m}-> {y}{interface_name}")
                        if str(address.family) == 'AddressFamily.AF_INET':
                            print(f"{c}IP {m}-> {y}{address.address}")
                            print(f"{c}Netmask {m}-> {y}{address.netmask}")
                            print(f"{c}Broadcast IP {m}-> {y}{address.broadcast}")
                        elif str(address.family) == 'AddressFamily.AF_PACKET':
                            print(f"{c}MAC {m}-> {y}{address.address}")
                            print(f"{c}Netmask {m}-> {y}{address.netmask}")
                            print(f"{c}Broadcast MAC {m}-> {y}{address.broadcast}")

                net_io = psutil.net_io_counters()

                print(f"{c}Total Bytes Sent {m}-> {y}{show_size(net_io.bytes_sent)}")
                print(f"{c}Total Bytes Received {m}-> {y}{show_size(net_io.bytes_recv)}\n")

                boot_time_timestamp = psutil.boot_time()
                boot_time = dtt.fromtimestamp(boot_time_timestamp)

                print(f"{m}=" * 27, f"{c}|{m} Boot {c}|{m}", "=" * 25)
                print(f"\n{c}Last Boot {m}-> {y}{boot_time.day}.{boot_time.month}.{boot_time.year}{boot_time.hour}:{boot_time.minute}:{boot_time.second}\n")

                end_time = dtt.now() 
                needed_time = end_time - start_time

                print(f"{c}Job Done In {g}{needed_time}")

        except PermissionError as permerr:
            print(permerr)

    def hunter_gate(self):
        try:
            if self.menu_option_choice == 0:
                call(["clear"])
            elif self.menu_option_choice == 1:
                print(cld(figlet_format("Witcher", font="bulbhead"), "yellow"))
                ip_gipv4u = str(input(f"{w}[{r}*{w}] {r}({w}{pwd.getpwuid(os.getuid())[0]}{r}@{w}Hunter{r},{w} Address{r})>>{o} "))

                if ip_gipv4u == 'x' or ip_gipv4u == 'exit':
                    print(f"{w}[{o}-{w}] Sorry{r},{w} But command '{ip_gipv4u}' is invalid{r}.{w} Please use Ctrl+C to exit Witcher{r}!{w}")

                sp_gipv4u = int(input(f"{w}[{r}*{w}] {r}({w}{pwd.getpwuid(os.getuid())[0]}{r}@{w}Hunter{r},{w} Min{r}.{w} Port{r})>>{o} "))
                mp_gipv4u = int(input(f"{w}[{r}*{w}] {r}({w}{pwd.getpwuid(os.getuid())[0]}{r}@{w}Hunter{r},{w} Max{r}.{w} Port{r})>>{o} "))
                extract_ipv4 = WitcherPortscanner(ip_gipv4u, sp_gipv4u, mp_gipv4u)
                extract_ipv4.main()
            elif self.menu_option_choice == 2:
                print(cld(figlet_format("MD5Crypt", font="bulbhead"), "yellow"))
                string_to_encrypt = str(input(f"{w}[{r}*{w}] {r}({w}{pwd.getpwuid(os.getuid())[0]}{r}@{w}Hunter{r},{w} String{r})>>{o} "))
                md5crypt = MD5Encrypt(string_to_encrypt)
                md5crypt.main()
            elif self.menu_option_choice == 3:
                print(cld(figlet_format("IPv4Whois", font="bulbhead"), "yellow"))
                ipv4_address = str(input(f"{w}[{r}*{w}] {r}({w}{pwd.getpwuid(os.getuid())[0]}{r}@{w}Hunter{r},{w} IPv4{r})>>{o} "))
                ipv4_lookup = IPv4Lookup(ipv4_address)
                ipv4_lookup.main()
            elif self.menu_option_choice == 4:
                print(cld(figlet_format("Banner\nGrabber", font="bulbhead"), "yellow"))
                ipv4_address = str(input(f"{w}[{r}*{w}] {r}({w}{pwd.getpwuid(os.getuid())[0]}{r}@{w}Hunter{r},{w} Address{r})>>{o} "))

                if ipv4_address == 'x' or ipv4_address == 'exit':
                    print(f"{w}[{o}-{w}] Sorry{r},{w} But command '{ipv4_address}' is invalid{r}.{w} Please use Ctrl+C to exit BannerGrabber{r}!")

                target_port = int(input(f"{w}[{r}*{w}] {r}({w}{pwd.getpwuid(os.getuid())[0]}{r}@{w}Hunter{r},{w} Port{r})>>{o} "))
                get_service = BannerGrabber(ipv4_address, target_port)
                get_service.main()
            elif self.menu_option_choice == 5:
                while True:
                    print(cld(figlet_format("B64Crypt", font="bulbhead"), "yellow"))
                    print(f"\n\t{w}[{r}1{w}] Encoder")
                    print(f"\t{w}[{r}2{w}] Decoder")
                    print(f"\t{w}[{r}x{w}] Exit")

                    b64_choice = input(f"\n{w}[{r}*{w}] Choice {r}>>{o} ")

                    if b64_choice == "1":
                        hash_value = str(input(f"{w}[{r}*{w}] {r}({w}{pwd.getpwuid(os.getuid())[0]}{r}@{w}Hunter{r},{w} Value{r})>>{o} "))
                        
                        if hash_value == 'exit' or hash_value == 'x':
                            break

                        try:
                            m_bytes = hash_value.encode('ascii')
                            b64_e = b64.b64encode(m_bytes)
                            b64_hash = b64_e.decode('ascii')

                            print(f"{r}=" * 70)
                            print(f"{w}[{g}+{w}] {hash_value} {r}->{w} {b64_hash}")
                            print(f"{r}=" * 70)
                            print(chr(0xa))
                            input(f"{w}[{r}*{w}] Press enter key to continue")
                        except Exception as error:
                            print(cld(f"An error was defined: {error}", "red"))
                            print(chr(0xa))
                            input(f"{w}[{r}*{w}] Press enter key to continue")
                    elif b64_choice == "2":
                        decode_hash = str(input(f"{w}[{r}*{w}] {r}({w}{pwd.getpwuid(os.getuid())[0]}{r}@{w}Hunter{r},{w} Value{r})>>{o} "))

                        if decode_hash == 'exit' or decode_hash == 'x':
                            break

                        try:
                            b64_d = decode_hash.encode('ascii')
                            m_byte = b64.b64decode(b64_d)
                            result = m_byte.decode('ascii')

                            print(f"{r}=" * 70)
                            print(f"{w}[{g}+{w}] {decode_hash} {r}->{w} {result}")
                            print(f"{r}=" * 70)
                            print(chr(0xa))
                            input(f"{w}[{r}*{w}] Press enter key to continue")
                        except Exception as error:
                            print(cld(f"An error was defined:\n{error}", "red"))
                            print(chr(0xa))
                            input(f"{w}[{r}*{w}] Press enter key to continue")
                    elif b64_choice == 'x' or b64_choice == 'exit':
                        break
                    else:
                        print(cld("Invalid Input!", "red"))
            elif self.menu_option_choice == 6:
                print(cld(figlet_format("Whois\nPhonenumber", font="bulbhead"), "yellow"))
                url_ps = str(input(f"{w}[{r}*{w}] {r}({w}{pwd.getpwuid(os.getuid())[0]}{r}@{w}Hunter{r},{w} Phonenumber{r})>>{o} "))
                phon_inf = PhonenumberWhois(url_ps)
                phon_inf.main()
            elif self.menu_option_choice == 7:
                print(cld(figlet_format("Subdomain\nScanner", font="bulbhead"), "yellow"))
                url_sds = str(input(f"{w}[{r}*{w}] {r}({w}{pwd.getpwuid(os.getuid())[0]}{r}@{w}Hunter{r},{w} URL{r})>>{o} "))

                if url_sds == 'x' or url_sds == 'exit':
                    print(f"{w}[{o}-{w}] Sorry{r},{w} But command '{url_sds}' is invalid{r}.{w} Please use Ctrl+C to exit SubdomainScanner{r}!")

                wordl = str(input(
                    f"{w}[{r}*{w}] {r}({w}{pwd.getpwuid(os.getuid())[0]}{r}@{w}Hunter{r},{w} Wordlist{r}[{w}empty for default wordlist{r}])>>{o} "
                ))
                bruteforce_subdomains = SubdomainScanner(url_sds, wordl)
                bruteforce_subdomains.main()
            elif self.menu_option_choice == 8:
                get_mac = ":".join(re.findall("..", "%012x" % uuid.getnode()))
                get_hostname = socket.gethostname()
                get_host_ip = socket.gethostbyname(get_hostname)
                get_username = pwd.getpwuid(os.getuid())[0]
                get_path = os.path.abspath(os.getcwd())
                get_time = dtt.now()
                public_ipv4 = get("https://api.ipify.org").text

                def check_root():
                    if "SUDO_UID" in os.environ.keys():
                        print(f"{w}[{g}+{w}] Type         {r}:{y}\tRoot User")
                    else:
                        print(f"{w}[{g}+{w}] Type         {r}:{y}\tNormal User")

                print(f"{c}\t\t\tWhoami")
                print(f"{m}< ", f"{g}=" * 66 + f"{m} >")
                print(f"{w}[{g}+{w}] Date         {r}:{y}\t{get_time}")
                print(f"{w}[{g}+{w}] Username     {r}:{y}\t{get_username}")
                
                check_root()
                
                print(f"{w}[{g}+{w}] Hostname     {r}:{y}\t{get_hostname}")
                print(f"{w}[{g}+{w}] IPAddress    {r}:{y}\t{get_host_ip}")
                print(f"{w}[{g}+{w}] Public IPv4  {r}:{y}\t{public_ipv4}")
                print(f"{w}[{g}+{w}] MACAddress   {r}:{y}\t{get_mac}")
                print(f"{w}[{g}+{w}] Current Path {r}:{y}\t{get_path}")
                print(f"{m}< ", f"{g}=" * 66 + f"{m} >")
                print(chr(0xa))
                input(f"{w}[{r}*{w}] Press enter key to continue")
            elif self.menu_option_choice == 9:
                HunterToolkit.my_system()
            elif self.menu_option_choice == 10:
                print(cld(figlet_format("URL2IPv4", font="bulbhead"), "yellow"))

                url_gipv4u = str(input(f"{w}[{r}*{w}] {r}({w}{pwd.getpwuid(os.getuid())[0]}{r}@{w}Hunter{r},{w} URL{r})>>{o} "))
                extract_ipv4 = GetIPv4fromURL(url_gipv4u)
                extract_ipv4.main()
            elif self.menu_option_choice == 11:
                print(cld(figlet_format("Password\nGenerator", font="bulbhead"), "yellow"))

                passw_length = int(input(f"{w}[{r}*{w}] {r}({w}{pwd.getpwuid(os.getuid())[0]}{r}@{w}Hunter{r},{w} Password length{r})>>{o} "))
                extract_ipv4 = PasswordGenerator(passw_length)
                extract_ipv4.main()
            elif self.menu_option_choice == 12:
                print(cld(figlet_format("URLWhois", font="bulbhead"), "yellow"))

                url_whois = str(input(f"{w}[{r}*{w}] {r}({w}{pwd.getpwuid(os.getuid())[0]}{r}@{w}Hunter{r},{w} URL{r})>>{o} "))
                get_lookup = WhoisLookupForURL(url_whois)
                get_lookup.main()
            elif self.menu_option_choice == 13:
                print(cld(figlet_format("HTTPHeader", font="bulbhead"), "yellow"))

                url_ghttph = str(input(f"{w}[{r}*{w}] {r}({w}{pwd.getpwuid(os.getuid())[0]}{r}@{w}Hunter{r},{w} URL{r})>>{o} "))
                gethttpheader = GetHTTPHeader(url_ghttph)
                gethttpheader.main()
            elif self.menu_option_choice == 14:
                print(cld(figlet_format("Link\nCollector", font="bulbhead"), "yellow"))

                url_lc = str(input(f"{w}[{r}*{w}] {r}({w}{pwd.getpwuid(os.getuid())[0]}{r}@{w}Hunter{r},{w} URL{r})>>{o} "))
                linkcollector = LinkCollector(url_lc)
                linkcollector.main()
            elif self.menu_option_choice == 15:
                print(cld(figlet_format("Ping", font="bulbhead"), "yellow"))

                addr = str(input(f"{w}[{r}*{w}] {r}({w}{pwd.getpwuid(os.getuid())[0]}{r}@{w}Hunter{r},{w} Address{r})>>{o} "))
                check = CheckHostAvailability(addr)
                check.main()
            elif self.menu_option_choice == 16:
                print(cld(figlet_format("IPSweep", font="bulbhead"), "yellow"))

                ipv4 = str(input(
                    f"{w}[{r}*{w}] {r}({w}{pwd.getpwuid(os.getuid())[0]}{r}@{w}Hunter{r},{w} IPv4 Address(First Three Octets Only){r})>>{o} "
                ))

                if ipv4 == 'x' or ipv4 == 'exit':
                    print(f"{w}[{o}-{w}] Sorry{r},{w} But command '{ipv4}' is invalid{r}.{w} Please use Ctrl+C to exit IPSweep{r}!")

                start_range = int(input(f"{w}[{r}*{w}] {r}({w}{pwd.getpwuid(os.getuid())[0]}{r}@{w}Hunter{r},{w} Start Range{r})>>{o} "))
                last_range = int(input(f"{w}[{r}*{w}] {r}({w}{pwd.getpwuid(os.getuid())[0]}{r}@{w}Hunter{r},{w} Last Range{r})>>{o} "))
                ping_count = str(input(f"{w}[{r}*{w}] {r}({w}{pwd.getpwuid(os.getuid())[0]}{r}@{w}Hunter{r},{w} Ping Count{r})>>{o} "))

                if ping_count == 'x' or ping_count == 'exit':
                    print(f"{w}[{o}-{w}] Sorry{r},{w} But command '{ping_count}' is invalid{r}.{w} Please use Ctrl+C to exit IPSweep{r}!")

                ipsweep = IPv4Sweep(ipv4, start_range, last_range, ping_count)
                ipsweep.get_status()
            elif self.menu_option_choice == 17:
                print(f"\n{w}[{r}*{w}] Most Used Tools{r}:")
                print("=" * 25)
                print(f"{c}[{r}FindEmailAddresses{c}]{w} https://hunter.io/")
                print(f"{c}[{r}PwnedEmailAddress/Phonenumber{c}]{w} https://haveibeenpwned.com/")
                print(f"{c}[{r}PwnedPassword{c}]{w} https://haveibeenpwned.com/Passwords")
                print(f"{c}[{r}RedHawk{c}]{w} https://github.com/Tuhinshubhra/RED_HAWK")
                print(f"{c}[{r}TheHarvester{c}]{w} https://github.com/laramies/theHarvester")
                print(f"{c}[{r}SherlockProject{c}]{w} https://github.com/sherlock-project/sherlock")
                print(f"{c}[{r}BurpSuite{c}]{w} https://portswigger.net/burp/communitydownload")
                print(f"{c}[{r}Wireshark{c}]{w} https://www.wireshark.org/")
                print(chr(0xa))
                input(f"\n{w}[{r}*{w}] Press enter key to continue")
            elif self.menu_option_choice == 18:
                print(cld(figlet_format("GetStat", font="bulbhead"), "yellow"))

                gs_url = str(input(f"{w}[{r}*{w}] {r}({w}{pwd.getpwuid(os.getuid())[0]}{r}@{w}Hunter{r},{w} Address{r})>>{o} "))
                get_status_code = RemoteServerStatusCode(gs_url)
                get_status_code.get_code()
            elif self.menu_option_choice == 19:
                print(cld(figlet_format("GetMail", font="bulbhead"), "yellow"))

                gm_url = str(input(f"{w}[{r}*{w}] {r}({w}{pwd.getpwuid(os.getuid())[0]}{r}@{w}Hunter{r},{w} Full URL{r})>>{o} "))
                extract_mail_addr = EmailExtractor(gm_url)
                extract_mail_addr.extract_mail_address()
            elif self.menu_option_choice == 99:
                print(f"\n{w}[{r}*{w}] Goodbye{r},{w} {pwd.getpwuid(os.getuid())[0]}{r}.{w} Follow the white rabbit {r}...\n")
                sys.exit(0)
            else:
                print(f"\n{w}[{y}-{w}] Invalid Input{r}!")
        except KeyboardInterrupt:
            print(f"\n{w}[{y}-{w}] You pressed Ctrl+C{r}.{w} Exit{r}!")
        except Exception:
            raise ValueError(f"{w}[{y}-{w}] Invalid Input{r}!")


if __name__ == "__main__":
    while True:
        print(cld("""
\t\tWelcome To Hunter Toolkit!
< =============================================================== >

\n Please note that actions like portscanning etc. can be illegal. 
 If you want to use this tool, follow the conditions:
 
- This tool is made for ethical purposes only.
- I'm not responsible for your actions.
- With great force follows great responsibility.

If you accept the conditions type 'y' and 'n' for decline.
Thank you and have a nice day!

~ Keyjeek\n
        """, "red"))

        try:
            start = str(input(f"{w}[{r}*{w}] Accept{r}?{w} y{r}/{w}n{o} "))

            if start == 'y' or start == 'Y':
                break
            elif start == 'n' or start == 'N':
                print(f"{w}[{r}*{w}] You need to accept the terms to use the Hunter-Toolkit{r}.{w} Exit {r}...\n")
                sys.exit(0)
            else:
                print(f"\n{w}[{y}-{w}] Only 'y/Y' or 'n/N' are allowed{r}!")
        except KeyboardInterrupt:
            print(f"\n{w}[{y}-{w}] You pressed Ctrl+C{r}.{w} Exit{r}!")
            sys.exit(1)

    while True:
        try:
            HunterToolkit.banner()
            HunterToolkit.menu()
            hunter_choice = int(input(f"{r}({w}{pwd.getpwuid(os.getuid())[0]}{r}@{w}Hunter{r})>>{o} "))
            hunter_toolkit = HunterToolkit(hunter_choice)
            hunter_toolkit.hunter_gate()
        except KeyboardInterrupt:
            print(f"\n{w}[{y}-{w}] You pressed Ctrl+C{r}.{w} Exit{r}!")
            sys.exit(1)
        except ValueError:
            print(f"\n{w}[{y}-{w}] You need to enter a integer value{r}!")




