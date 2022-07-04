#!/usr/bin/env python3

try:
    from src.witcher_portscanner import WitcherPortscanner
    from src.md5encrypt import MD5Encrypt
    from src.ipv4_whois import IPv4Lookup
    from src.banner_grabber import BannerGrabber
    from src.phonenumber_lookup import PhonenumberWhois
    from src.subdomain_scanner import SubdomainScanner
    from src.url2ip import GetIPv4fromURL
    from src.password_generator import PasswordGenerator
    from src.whois_lookup_for_url import WhoisLookupForURL
    from src.get_http_header import GetHTTPHeader
    from src.link_collector import LinkCollector
    from src.check_host_availability import CheckHostAvailability
    from src.ipsweep import IPv4Sweep
    
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
    import uuid
    import sys
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
#   Version :   1.1.5                     #
#                                         #
# # # # # # # # # # # # # # # # # # # # # #

magenta = "\033[0;35m"
yellow = "\033[0;33m"
green = "\033[0;32m"
white = "\033[0;37m"
cyan = "\033[0;36m"
red = "\033[0;31m"


class HunterToolkit:

    def __init__(
            self,
            menu_option_choice: int
    ):
        self.menu_option_choice = menu_option_choice

    @staticmethod
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
            magenta + ">" + yellow + " Ver" + magenta + ".:" + red + "1.1.5"
        )
        print(
            cyan + "\n[" + red + "*" + cyan + "] " + yellow +
            "Hunter - Penetration Testing Assistant,\n\t\tInformation Gathering And More."
        )

    @staticmethod
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
            " PassGen " + magenta + ">> " + yellow + " Generate a random password."
        )
        print(
            green + "{" + red + "12" + green + "}" + cyan +
            " WhoisForURL " + magenta + ">> " + yellow + " Whois lookup for URL."
        )
        print(
            green + "{" + red + "13" + green + "}" + cyan +
            " GetHeader " + magenta + ">> " + yellow + " Get header from url."
        )
        print(
            green + "{" + red + "14" + green + "}" + cyan +
            " LinkCollector " + magenta + ">> " + yellow + " Get links from any website."
        )
        print(
            green + "{" + red + "15" + green + "}" + cyan +
            " Ping " + magenta + ">> " + yellow + " Check remote host availability."
        )
        print(
            green + "{" + red + "16" + green + "}" + cyan +
            " IPSweep " + magenta + ">> " + yellow + " Check host range for active devices."
        )

        print(green + "{" + red + "99" + green + "}" + green + " Exit\n")

        print(magenta + "=" * 70)

    @staticmethod
    def my_system():
        try:
            while True:
                print(cld(figlet_format(
                    "MySystem",
                    font="bulbhead"
                )))

                continue_or_exit = str(input(
                    white + "[" + red + "*" + white +
                    f"] ({os.getlogin()}" + red + "@" + white + "Hunter, Enter to continue, 'x' to exit)>> "
                ))

                start_time = dtt.now()
                if continue_or_exit == 'exit' or continue_or_exit == 'x':
                    break

                get_system = platform.uname()

                print(
                    magenta + "=" * 45,
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
                    magenta + "=" * 40,
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
                    magenta + "=" * 40,
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
                print(cyan + "\nCPU Core Usage: \n" + yellow)

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
                    magenta + "=" * 40,
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
                    magenta + "=" * 45,
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
                    magenta + "=" * 40,
                    "| Network Information |",
                    "=" * 40,
                    "\n"
                )

                if_addrs = psutil.net_if_addrs()

                for interface_name, interface_addresses in if_addrs.items():
                    for address in interface_addresses:
                        print(
                            cyan + "Interface: " + yellow +
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
                    magenta + "=" * 40,
                    "| Boot |",
                    "=" * 55
                )

                print(
                    cyan + "\nLast Boot: " + yellow +
                    f"{boot_time.day}.{boot_time.month}.{boot_time.year} " +
                    f"{boot_time.hour}:{boot_time.minute}:{boot_time.second}\n"
                )

                end_time = dtt.now()  # get end time
                needed_time = end_time - start_time

                print(cyan + "Job Done In " + green + f"{needed_time}")

        except PermissionError as permerr:
            print(permerr)

        input("\nPress enter key to continue")

    def hunter_gate(self):
        try:
            if self.menu_option_choice == 0:
                call(["clear"])
            elif self.menu_option_choice == 1:
                print(cld(figlet_format(
                    "Witcher",
                    font="bulbhead"
                )))

                ip_gipv4u = str(input(
                    white + "[" + red + "*" + white +
                    f"] ({os.getlogin()}" + red + "@" + white + "Hunter, Address)>> "
                ))
                sp_gipv4u = int(input(
                    white + "[" + red + "*" + white +
                    f"] ({os.getlogin()}" + red + "@" + white + "Hunter, Min. Port)>> "
                ))
                mp_gipv4u = int(input(
                    white + "[" + red + "*" + white +
                    f"] ({os.getlogin()}" + red + "@" + white + "Hunter, Max. Port)>> "
                ))
                extract_ipv4 = WitcherPortscanner(
                    ip_gipv4u,
                    sp_gipv4u,
                    mp_gipv4u
                )

                extract_ipv4.main()

            elif self.menu_option_choice == 2:
                print(cld(figlet_format(
                    "MD5Crypt",
                    font="bulbhead"
                )))

                string_to_encrypt = str(input(
                    white + "[" + red + "*" + white +
                    f"] ({os.getlogin()}" + red + "@" + white + "Hunter, String)>> "
                ))
                md5crypt = MD5Encrypt(string_to_encrypt)

                md5crypt.main()

            elif self.menu_option_choice == 3:
                print(cld(figlet_format(
                    "IPv4Whois",
                    font="bulbhead"
                )))

                ipv4_address = str(input(
                    white + "[" + red + "*" + white +
                    f"] ({os.getlogin()}" + red + "@" + white + "Hunter, IPv4)>> "
                ))
                ipv4_lookup = IPv4Lookup(ipv4_address)

                ipv4_lookup.main()

            elif self.menu_option_choice == 4:
                print(cld(figlet_format(
                    "Port\nService",
                    font="bulbhead"
                )))

                ipv4_address = str(input(
                    white + "[" + red + "*" + white +
                    f"] ({os.getlogin()}" + red + "@" + white + "Hunter, Address)>> "
                ))
                target_port = int(input(
                    white + "[" + red + "*" + white +
                    f"] ({os.getlogin()}" + red + "@" + white + "Hunter, Port)>> "
                ))
                get_service = BannerGrabber(ipv4_address, target_port)

                get_service.main()

            elif self.menu_option_choice == 5:
                while True:
                    print(cld(figlet_format(
                        "B64Crypt",
                        font="bulbhead"
                    )))
                    print("This Tool encode and decode your text in base64.")
                    print("Type 'exit' to exit Base64crypt.")
                    print("\n\t[1] Encoder")
                    print("\t[2] Decoder")
                    print("\t[x] Exit")

                    b64_choice = input("\nChoice >> ")

                    if b64_choice == "1":
                        hash_value = str(input(
                            white + "[" + red + "*" + white +
                            f"({os.getlogin()}" + red + "@" + white + "Hunter, Value)>> "
                        ))
                        if hash_value == 'exit' or hash_value == 'x':
                            break

                        try:
                            m_bytes = hash_value.encode('ascii')
                            b64_e = b64.b64encode(m_bytes)
                            b64_hash = b64_e.decode('ascii')
                            print(b64_hash)
                            input("Press enter key to continue")

                        except Exception as error:
                            print(cld(
                                f"An error was defined: {error}"
                            ))
                            input("Press enter key to continue")

                    elif b64_choice == "2":
                        decode_hash = str(input(
                            white + "[" + red + "*" + white +
                            f"({os.getlogin()}" + red + "@" + white + "Hunter, Value)>> "
                        ))

                        if decode_hash == 'exit' or decode_hash == 'x':
                            print(cld(
                                "Exit",
                                "red"
                            ))

                            break

                        try:
                            b64_d = decode_hash.encode('ascii')
                            m_byte = b64.b64decode(b64_d)
                            result = m_byte.decode('ascii')
                            print(result)
                            input("Press enter key to continue")

                        except Exception as error:
                            print(cld(
                                f"An error was defined: {error}"
                            ))
                            input(cyan + "Press enter key to continue")

                    elif b64_choice == 'x' or b64_choice == 'exit':
                        break
                    else:
                        print(cld("Invalid Input!"))

            elif self.menu_option_choice == 6:
                print(cld(figlet_format(
                    "PhoneStalk",
                    font="bulbhead"
                )))

                url_ps = str(input(
                    white + "[" + red + "*" + white +
                    f"] ({os.getlogin()}" + red + "@" + white + "Hunter, Phonenumber)>> "
                ))
                phon_inf = PhonenumberWhois(url_ps)

                phon_inf.main()

            elif self.menu_option_choice == 7:
                print(cld(figlet_format(
                    "Subdomain\nScanner",
                    font="bulbhead"
                )))

                url_sds = str(input(
                    white + "[" + red + "*" + white +
                    f"] ({os.getlogin()}" + red + "@" + white + "Hunter, URL)>> "
                ))
                bruteforce_subdomains = SubdomainScanner(url_sds)

                bruteforce_subdomains.main()

            elif self.menu_option_choice == 8:
                get_mac = ':'.join(
                    re.findall(
                        '..', '%012x' % uuid.getnode()
                    )
                )
                get_hostname = socket.gethostname()
                get_host_ip = socket.gethostbyname(get_hostname)
                get_username = os.getlogin()
                get_path = os.path.abspath(os.getcwd())
                get_time = dtt.now()
                public_ipv4 = get("https://api.ipify.org").text

                def check_root():
                    if "SUDO_UID" in os.environ.keys():
                        print(cyan + "\tType         :" + yellow + "\tRoot User")
                    else:
                        print(cyan + "\tType         :" + yellow + "\tNormal User")

                print(cyan + "\t\t\tWhoami")
                print(magenta + "< " + green + "=" * 66 + magenta + " >")
                print(cyan + "\tDate         :" + yellow + f"\t{get_time}")
                print(cyan + "\tUsername     :" + yellow + f"\t{get_username}")
                check_root()
                print(cyan + "\tHostname     :" + yellow + f"\t{get_hostname}")
                print(cyan + "\tIPAddress    :" + yellow + f"\t{get_host_ip}")
                print(cyan + "\tPublic IPv4  :" + yellow + f"\t{public_ipv4}")
                print(cyan + "\tMACAddress   :" + yellow + f"\t{get_mac}")
                print(cyan + "\tCurrent Path :" + yellow + f"\t{get_path}")
                input(cyan + "\nPress enter key to continue")

            elif self.menu_option_choice == 9:
                HunterToolkit.my_system()
            elif self.menu_option_choice == 10:
                print(cld(figlet_format(
                    "URL2IPv4",
                    font="bulbhead"
                )))

                url_gipv4u = str(input(
                    white + "[" + red + "*" + white +
                    f"] ({os.getlogin()}" + red + "@" + white + "Hunter, URL)>> "
                ))
                extract_ipv4 = GetIPv4fromURL(url_gipv4u)

                extract_ipv4.main()

            elif self.menu_option_choice == 11:
                print(cld(figlet_format(
                    "PassGen",
                    font="bulbhead"
                )))

                passw_length = int(input(
                    white + "[" + red + "*" + white +
                    f"] ({os.getlogin()}" + red + "@" + white + "Hunter, Password length)>> "
                ))
                extract_ipv4 = PasswordGenerator(passw_length)

                extract_ipv4.main()

            elif self.menu_option_choice == 12:
                print(cld(figlet_format(
                    "URLWhois",
                    font="bulbhead"
                )))

                url_whois = str(input(
                    white + "[" + red + "*" + white +
                    f"] ({os.getlogin()}" + red + "@" + white + "Hunter, URL)>> "
                ))
                get_lookup = WhoisLookupForURL(url_whois)

                get_lookup.main()

            elif self.menu_option_choice == 13:
                print(cld(figlet_format(
                    "GetHTTP\nHeader",
                    font="bulbhead"
                )))

                url_ghttph = str(input(
                    white + "[" + red + "*" + white +
                    f"] ({os.getlogin()}" + red + "@" + white + "Hunter, URL)>> "
                ))
                gethttpheader = GetHTTPHeader(url_ghttph)

                gethttpheader.main()

            elif self.menu_option_choice == 14:
                print(cld(figlet_format(
                    "LinkCollect",
                    font="bulbhead"
                )))

                url_lc = str(input(
                    white + "[" + red + "*" + white +
                    f"] ({os.getlogin()}" + red + "@" + white + "Hunter, URL)>> "
                ))
                linkcollector = LinkCollector(url_lc)

                linkcollector.main()

            elif self.menu_option_choice == 15:
                print(cld(figlet_format(
                    "CheckAvail",
                    font="bulbhead"
                )))

                addr = str(input(
                    white + "[" + red + "*" + white +
                    f"] ({os.getlogin()}" + red + "@" + white + "Hunter, Address)>> "
                ))
                check = CheckHostAvailability(addr)

                check.main()

            elif self.menu_option_choice == 16:
                print(cld(figlet_format(
                    "IPSweep",
                    font="bulbhead"
                )))

                ipv4 = str(input(
                    white + "[" + red + "*" + white +
                    f"] ({os.getlogin()}" + red + "@" + white + "Hunter, Address)>> "
                ))

                start_range = int(input(
                    white + "[" + red + "*" + white +
                    f"] ({os.getlogin()}" + red + "@" + white + "Hunter, Start Range)>> "
                ))

                last_range = int(input(
                    white + "[" + red + "*" + white +
                    f"] ({os.getlogin()}" + red + "@" + white + "Hunter, Last Range)>> "
                ))

                ipsweep = IPv4Sweep(
                    ipv4,
                    start_range,
                    last_range
                )

                ipsweep.get_status()

            elif self.menu_option_choice == 99:
                sys.exit(0)
                
            else:
                print("Invalid Input!")
                
        except KeyboardInterrupt:
            print("\nYou pressed Ctrl+C. EXIT!")
        
        except Exception:
            raise ValueError("Invalid Input!")


if __name__ == "__main__":
    while True:
        call(["clear"])

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
            break
            
        elif choice == 'n' or choice == 'N':
            print(cld(
                "You need to accept the terms above to use Hunter. Exit.",
                "red"
            ))
            
            sys.exit(1)
            
        else:
            print(cld(
                "Invalid Input!",
                "red"
            ))
            
            pass

    while True:
        try:
            HunterToolkit.banner()
            HunterToolkit.menu()

            hunter_choice = int(input(
                cyan + "(" + yellow + f"{os.getlogin()}@" +
                red + "Hunter" + cyan + ")>> " + magenta
            ))
            hunter_toolkit = HunterToolkit(hunter_choice)
            
            hunter_toolkit.hunter_gate()
            
        except KeyboardInterrupt:
            print("\nYou pressed Ctrl+C.EXIT!")
            sys.exit(1)
            
        except ValueError:
            print("You need to enter a integer value!")


