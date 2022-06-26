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

class WitcherPortscanner:

    def __init__(
            self,
            target_ipv4: str,
            maximum_port: int
    ):
        self.target_ipv4 = target_ipv4
        self.maximum_port = maximum_port

    def main(self):
        while True:
            if self.target_ipv4 == 'x' or self.target_ipv4 == 'exit':
                break
            elif self.maximum_port == 0:
                break

            print("=" * 70)
            scan_start = dtt.now()
            print(f"Started scanning at:\t\t\t{scan_start}")
            print("=" * 70)
            time_start = dtt.now()
            print("Protocol\tPort\t\tStatus\t Service\n" + "-" * 70)

            try:
                for target in range(
                        1, self.maximum_port
                ):
                    socket_sock = socket.socket(
                        socket.AF_INET,
                        socket.SOCK_STREAM
                    )
                    final_result = socket_sock.connect_ex((
                        self.target_ipv4,
                        target
                    ))
                    socket_sock.settimeout(1)
                    if final_result == 0:
                        try:
                            print(f"TCP\t\t\t{target}  \t\topen\t", socket.getservbyport(target))
                        except:
                            print(f"TCP\t\t\t{target}  \t\topen\t Unknown")
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
            print(cld(
                f"Scanner done in {needed_time}!",
                "green"
            ))
            print("=" * 70)
            print(chr(0xa))
            input("Press enter key to continue")
            break
