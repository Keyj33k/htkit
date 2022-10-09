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

y = "\033[0;33m"
g = "\033[0;32m"
w = "\033[0;37m"
r = "\033[0;31m"

class SystemInformations:

    @staticmethod
    def overview():
        try:
            while True:
                print(cld(figlet_format("system\noverview", font="bulbhead"), "yellow"))
                continue_or_exit = str(input(f"{w}[{r}*{w}] {w}{USERNAME}{r}@{w}Hunter{r},"
                                             f"{w} Enter to continue{r},{w} {r}'{w}x{r}'{w} to exit{r} >>{y} "))
                if continue_or_exit == 'exit' or continue_or_exit == 'x': break
                if continue_or_exit is not "":
                    print(f"{w}[{y}-{w}] Invalid input")
                    break
                start_time = dtt.now()
                get_system = uname()

                print(f"{w}[{r}*{w}] Details\n"
                      f"{w}[{g}+{w}] System{r}:{w} {get_system.system}\n"
                      f"{w}[{g}+{w}] Name{r}:{w} {get_system.node}\n"
                      f"{w}[{g}+{w}] Release{r}:{w} {get_system.release}\n"
                      f"{w}[{g}+{w}] Version{r}:{w} {get_system.version}\n"
                      f"{w}[{g}+{w}] Machine{r}:{w} {get_system.machine}\n"
                      f"{w}[{g}+{w}] Processor{r}:{w} {get_system.processor}\n")

                def show_size(size):
                    for unit in ["B", "KB", "MB", "GB", "TB"]:
                        if size > 1024:
                            size = size / 1024
                        else:
                            return f"{size:.3f}{unit}"

                get_partitions = psutil.disk_partitions()
                print(f"\n{w}[{r}*{w}] Disk")

                for part in get_partitions:
                    print(f"\n{w}[{g}+{w}] Device{r}:{w} {part.device}\n"
                          f"{w}[{g}+{w}] Mounted At{r}:{w} {part.mountpoint}\n"
                          f"{w}[{g}+{w}] Type{r}:{w} {part.fstype}\n")

                    try:
                        part_usage = psutil.disk_usage(part.mountpoint)
                    except PermissionError:
                        continue

                    print(f"{w}[{g}+{w}] Total Size{r}:{w} {show_size(part_usage.total)}\n"
                          f"{w}[{g}+{w}] In Use{r}:{w} {show_size(part_usage.used)}\n"
                          f"{w}[{g}+{w}] Free{r}:{w} {show_size(part_usage.free)}\n"
                          f"{w}[{g}+{w}] Percentance{r}:{w} {part_usage.percent}%")

                disk_io = psutil.disk_io_counters()
                print(f"{w}[{g}+{w}] Read Since Boot{r}:{w} {show_size(disk_io.read_bytes)}\n"
                      f"{w}[{g}+{w}] Written Since Boot{r}:{w} {show_size(disk_io.write_bytes)}\n")

                print(f"{w}[{r}*{w}] CPU\n"
                      f"{w}[{g}+{w}] Cores{r}:{w} {psutil.cpu_count(logical=False)}\n"
                      f"{w}[{g}+{w}] Logical Cores{r}:{w} {psutil.cpu_count(logical=True)}\n"
                      f"{w}[{g}+{w}] Maximal Freq{r}:{w} {psutil.cpu_freq().max:.1f}Mhz\n"
                      f"{w}[{g}+{w}] Current Freq{r}:{w} {psutil.cpu_freq().current:.1f}Mhz\n"
                      f"{w}[{g}+{w}] CPU Usage{r}:{w} {psutil.cpu_percent()}%\n"
                      f"\n{w}[{r}*{w}] CPU Core Usage:\n{y}")

                for core, percentance in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
                    print(f"{w}[{g}+{w}] Core {core}{r}:{w} {percentance}%")

                virtual_mem = psutil.virtual_memory()
                swap = psutil.swap_memory()

                print(f"\n{w}[{r}*{w}] Ram\n"
                      f"{w}[{g}+{w}] Total{r}:{w} {show_size(virtual_mem.total)}\n"
                      f"{w}[{g}+{w}] Available{r}:{w} {show_size(virtual_mem.available)}\n"
                      f"{w}[{g}+{w}] In Use{r}:{w} {show_size(virtual_mem.used)}\n"
                      f"{w}[{g}+{w}] Percentence{r}:{w} {show_size(virtual_mem.percent)}%\n")

                print(f"{w}[{r}*{w}] SWAP\n"
                      f"{w}[{g}+{w}] Total{r}:{w} {show_size(swap.total)}\n"
                      f"{w}[{g}+{w}] Free{r}:{w} {show_size(swap.free)}\n"
                      f"{w}[{g}+{w}] In Use{r}:{w} {show_size(swap.used)}\n"
                      f"{w}[{g}+{w}] Percentence{r}:{w} {swap.percent}%\n")

                print(f"{w}[{r}*{w}] Network")
                if_addrs = psutil.net_if_addrs()

                for interface_name, interface_addresses in if_addrs.items():
                    for address in interface_addresses:
                        print(f"\n{w}[{g}+{w}] Interface{r}:{w} {interface_name}")
                        if str(address.family) == 'AddressFamily.AF_INET':
                            print(f"{w}[{g}+{w}] IP{r}:{w} {address.address}\n"
                                  f"{w}[{g}+{w}] Netmask{r}:{w} {address.netmask}\n"
                                  f"{w}[{g}+{w}] Broadcast IP{r}:{w} {address.broadcast}")
                        elif str(address.family) == 'AddressFamily.AF_PACKET':
                            print(f"{w}[{g}+{w}] MAC{r}:{w} {address.address}\n"
                                  f"{w}[{g}+{w}] Netmask{r}:{w} {address.netmask}\n"
                                  f"{w}[{g}+{w}] Broadcast MAC{r}:{w} {address.broadcast}")

                net_io = psutil.net_io_counters()
                boot_time_timestamp = psutil.boot_time()
                boot_time = dtt.fromtimestamp(boot_time_timestamp)

                print(f"{w}[{g}+{w}] Total Bytes Sent{r}:{w} {show_size(net_io.bytes_sent)}\n"
                      f"{w}[{g}+{w}] Total Bytes Received{r}:{w} {show_size(net_io.bytes_recv)}\n")

                print(f"{w}[{g}+{w}] Boot\n"
                      f"{w}[{g}+{w}] Last Boot{r}:{w} {boot_time.day}.{boot_time.month}.{boot_time.year} "
                      f" {boot_time.hour}:{boot_time.minute}:{boot_time.second}\n")

                print(f"{w}[{r}*{w}] Done, runtime{r}:{w} {dtt.now() - start_time}")
        except PermissionError as permerr:
            print(permerr)

    @staticmethod
    def details():
        def check_root():
            if "SUDO_UID" in os.environ.keys():
                return f"{w}[{g}+{w}] Type{r}:{w} Root"
            else:
                return f"{w}[{g}+{w}] Type{r}:{w} User"

        print(cld(figlet_format("whoami", font="bulbhead"), "yellow"))
        print(f"{w}[{g}+{w}] Username{r}:{w} {USERNAME}\n"
              f"{check_root()}\n"
              f"{w}[{g}+{w}] Hostname{r}:{w} {gethostname()}\n"
              f"{w}[{g}+{w}] IPAddress{r}:{w} {gethostbyname(gethostname())}\n"
              f"{w}[{g}+{w}] Public IPv4{r}:{w} {get('https://api.ipify.org').text}\n"
              f"{w}[{g}+{w}] MACAddress{r}:{w} {':'.join(findall('..', '%012x' % getnode()))}\n"
              f"{w}[{g}+{w}] Current Path{r}:{w} {os.path.abspath(os.getcwd())}")
        input(f"{w}[{r}*{w}] Press enter key to continue")