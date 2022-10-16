#!/usr/bin/env python3

try:
    from pyfiglet import figlet_format
    from termcolor import colored as cld
    from datetime import datetime as dtt
    from platform import uname
    import psutil
    from pwd import getpwuid
    import os
    from socket import gethostname, gethostbyname
    from requests import get
    from re import findall
    from uuid import getnode
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

USERNAME = getpwuid(os.getuid())[0]

class SystemInformations:
    @staticmethod
    def overview():
        try:
            while True:
                print(cld(figlet_format("system\noverview", font="bulbhead"), "yellow"))
                continue_or_exit = str(input(f"{W}[{R}*{W}] {W}{USERNAME}{R}@{W}Hunter{R},"
                                             f"{W} Enter to continue{R},{W} {R}'{W}x{R}'{W} to exit{R} >>{Y} "))
                if continue_or_exit == 'exit' or continue_or_exit == 'x': break
                if continue_or_exit != "":
                    print(f"{W}[{Y}-{W}] Invalid input")
                    break
                start_time = dtt.now()
                get_system = uname()
                print(f"{W}[{R}*{W}] Details\n"
                      f"{W}[{G}+{W}] System{R}:{W} {get_system.system}\n"
                      f"{W}[{G}+{W}] Name{R}:{W} {get_system.node}\n"
                      f"{W}[{G}+{W}] Release{R}:{W} {get_system.release}\n"
                      f"{W}[{G}+{W}] Version{R}:{W} {get_system.version}\n"
                      f"{W}[{G}+{W}] Machine{R}:{W} {get_system.machine}\n"
                      f"{W}[{G}+{W}] Processor{R}:{W} {get_system.processor}\n")

                def show_size(size):
                    for unit in ["B", "KB", "MB", "GB", "TB"]:
                        if size > 1024:
                            size = size / 1024
                        else:
                            return f"{size:.3f}{unit}"

                get_partitions = psutil.disk_partitions()
                print(f"\n{W}[{R}*{W}] Disk")
                for part in get_partitions:
                    print(f"\n{W}[{G}+{W}] Device{R}:{W} {part.device}\n"
                          f"{W}[{G}+{W}] Mounted At{R}:{W} {part.mountpoint}\n"
                          f"{W}[{G}+{W}] Type{R}:{W} {part.fstype}\n")

                    try:
                        part_usage = psutil.disk_usage(part.mountpoint)
                    except PermissionError:
                        continue

                    print(f"{W}[{G}+{W}] Total Size{R}:{W} {show_size(part_usage.total)}\n"
                          f"{W}[{G}+{W}] In Use{R}:{W} {show_size(part_usage.used)}\n"
                          f"{W}[{G}+{W}] Free{R}:{W} {show_size(part_usage.free)}\n"
                          f"{W}[{G}+{W}] Percentance{R}:{W} {part_usage.percent}%")

                disk_io = psutil.disk_io_counters()
                print(f"{W}[{G}+{W}] Read Since Boot{R}:{W} {show_size(disk_io.read_bytes)}\n"
                      f"{W}[{G}+{W}] Written Since Boot{R}:{W} {show_size(disk_io.write_bytes)}\n")
                print(f"{W}[{R}*{W}] CPU\n"
                      f"{W}[{G}+{W}] Cores{R}:{W} {psutil.cpu_count(logical=False)}\n"
                      f"{W}[{G}+{W}] Logical Cores{R}:{W} {psutil.cpu_count(logical=True)}\n"
                      f"{W}[{G}+{W}] Maximal Freq{R}:{W} {psutil.cpu_freq().max:.1f}Mhz\n"
                      f"{W}[{G}+{W}] Current Freq{R}:{W} {psutil.cpu_freq().current:.1f}Mhz\n"
                      f"{W}[{G}+{W}] CPU Usage{R}:{W} {psutil.cpu_percent()}%\n"
                      f"\n{W}[{R}*{W}] CPU Core Usage:\n{Y}")

                for core, percentance in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
                    print(f"{W}[{G}+{W}] Core {core}{R}:{W} {percentance}%")

                virtual_mem = psutil.virtual_memory()
                swap = psutil.swap_memory()
                print(f"\n{W}[{R}*{W}] Ram\n"
                      f"{W}[{G}+{W}] Total{R}:{W} {show_size(virtual_mem.total)}\n"
                      f"{W}[{G}+{W}] Available{R}:{W} {show_size(virtual_mem.available)}\n"
                      f"{W}[{G}+{W}] In Use{R}:{W} {show_size(virtual_mem.used)}\n"
                      f"{W}[{G}+{W}] Percentence{R}:{W} {show_size(virtual_mem.percent)}%\n")

                print(f"{W}[{R}*{W}] SWAP\n"
                      f"{W}[{G}+{W}] Total{R}:{W} {show_size(swap.total)}\n"
                      f"{W}[{G}+{W}] Free{R}:{W} {show_size(swap.free)}\n"
                      f"{W}[{G}+{W}] In Use{R}:{W} {show_size(swap.used)}\n"
                      f"{W}[{G}+{W}] Percentence{R}:{W} {swap.percent}%\n")

                print(f"{W}[{R}*{W}] Network")
                if_addrs = psutil.net_if_addrs()

                for interface_name, interface_addresses in if_addrs.items():
                    for address in interface_addresses:
                        print(f"\n{W}[{G}+{W}] Interface{R}:{W} {interface_name}")
                        if str(address.family) == "AddressFamily.AF_INET":
                            print(f"{W}[{G}+{W}] IP{R}:{W} {address.address}\n"
                                  f"{W}[{G}+{W}] Netmask{R}:{W} {address.netmask}\n"
                                  f"{W}[{G}+{W}] Broadcast IP{R}:{W} {address.broadcast}")
                        elif str(address.family) == "AddressFamily.AF_PACKET":
                            print(f"{W}[{G}+{W}] MAC{R}:{W} {address.address}\n"
                                  f"{W}[{G}+{W}] Netmask{R}:{W} {address.netmask}\n"
                                  f"{W}[{G}+{W}] Broadcast MAC{R}:{W} {address.broadcast}")

                net_io = psutil.net_io_counters()
                boot_time_timestamp = psutil.boot_time()
                boot_time = dtt.fromtimestamp(boot_time_timestamp)
                print(f"{W}[{G}+{W}] Total Bytes Sent{R}:{W} {show_size(net_io.bytes_sent)}\n"
                      f"{W}[{G}+{W}] Total Bytes Received{R}:{W} {show_size(net_io.bytes_recv)}\n")

                print(f"{W}[{G}+{W}] Boot\n"
                      f"{W}[{G}+{W}] Last Boot{R}:{W} {boot_time.day}.{boot_time.month}.{boot_time.year} "
                      f" {boot_time.hour}:{boot_time.minute}:{boot_time.second}\n")

                print(f"{W}[{R}*{W}] Done, runtime{R}:{W} {dtt.now() - start_time}")
        except PermissionError as permerr:
            print(permerr)

    @staticmethod
    def details():
        def check_root():
            if "SUDO_UID" in os.environ.keys():
                return f"{W}[{G}+{W}] Type{R}:{W} Root"
            else:
                return f"{W}[{G}+{W}] Type{R}:{W} User"

        print(cld(figlet_format("whoami", font="bulbhead"), "yellow"))
        print(f"{W}[{G}+{W}] Username{R}:{W} {USERNAME}\n"
              f"{check_root()}\n"
              f"{W}[{G}+{W}] Hostname{R}:{W} {gethostname()}\n"
              f"{W}[{G}+{W}] IPAddress{R}:{W} {gethostbyname(gethostname())}\n"
              f"{W}[{G}+{W}] Public IPv4{R}:{W} {get('https://api.ipify.org').text}\n"
              f"{W}[{G}+{W}] MACAddress{R}:{W} {':'.join(findall('..', '%012x' % getnode()))}\n"
              f"{W}[{G}+{W}] Current Path{R}:{W} {os.path.abspath(os.getcwd())}")
        input(f"{W}[{G}*{W}] Press enter key to continue")
