#!/usr/bin/env python3

try:
    from datetime import datetime as dtt
    from termcolor import colored as cld
    import socket
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
#   Version :   1.1.9                     #
#                                         #
# # # # # # # # # # # # # # # # # # # # # #

w = "\033[0;37m"
g = "\033[0;32m"
r = "\033[0;31m"


class WitcherPortscanner:

    def __init__(
            self,
            target_ipv4: str,
            start_port: int,
            maximum_port: int
    ):
        self.start_port = start_port
        self.target_ipv4 = target_ipv4
        self.maximum_port = maximum_port

    def main(self):
        while True:
            if self.target_ipv4 == 'x' or self.target_ipv4 == 'exit':
                break
            elif self.maximum_port == 0:
                break

            scan_start = dtt.now()
            print(f"\n{w}[{r}*{w}] Started scanning at:\t{scan_start}")
            print("=" * 70)
            time_start = dtt.now()
            print("Protocol\tPort\t\tStatus\t Service\n" + "-" * 70)

            try:
                for target in range(
                        self.start_port,
                        self.maximum_port + 1
                ):
                    socket_sock = socket.socket(
                        socket.AF_INET,
                        socket.SOCK_STREAM
                    )
                    final_result = socket_sock.connect_ex((
                        self.target_ipv4,
                        target
                    ))
                    socket_sock.settimeout(5)
                    
                    if final_result == 0:
                        try:
                            print(f"TCP\t\t{target}  \t\topen\t", socket.getservbyport(target))
                        except:
                            print(f"TCP\t\t{target}  \t\topen\t Unknown")
                            
                    socket_sock.close()
            except socket.error as socket_error:
                print(cld(
                    socket_error,
                    "red"
                ))
                break
            except KeyboardInterrupt:
                print(cld(
                    "\nCtrl+C pressed. Exit.",
                    "red"
                ))
                break

            time_stop = dtt.now()
            needed_time = time_stop - time_start

            print("=" * 70)
            print(f"{w}[{r}*{w}] Scanner done in {needed_time}!")
            print(chr(0xa))
            input(f"{w}[{r}*{w}] Press enter key to continue")
            break
