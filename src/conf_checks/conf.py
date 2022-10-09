#!/usr/bin/env python3

W = "\033[0;37m"
R = "\033[0;31m"
Y = "\033[0;33m"

class Conf:
    @staticmethod
    def hosts(min_host: int, max_host: int):
        if min_host <= 0 or min_host >= 252:
            print(f"\n{W}[{Y}-{W}] Invalid min host config ( {min_host} )!")
            return False
        elif max_host <= 0 or max_host >= 253:
            print(f"\n{W}[{Y}-{W}] Invalid max host config ( {max_host} )!")
            return False
        elif min_host > max_host:
            print(f"\n{W}[{Y}-{W}] Invalid host config{R}:{W} min host value "
                  f"cannot be bigger than the max host value{R}!{W}")
            return False

    @staticmethod
    def ports(min_port: int, max_port: int):
        if min_port <= 0 or min_port >= 65534:
            print(f"\n{W}[{Y}-{W}] Port {min_port} is invalid{R}!")
            return False
        elif max_port <= 1 or max_port >= 65535:
            print(f"\n{W}[{Y}-{W}] Port {max_port} is invalid{R}!")
            return False

    @staticmethod
    def octets(ipv4_addr: str, num_of_octets: int):
        split_address = ipv4_addr.split(".")
        if len(split_address) != num_of_octets:
            print(f"\n{W}[{Y}-{W}] The given address is invalid{R}!")
            return False

        for octet in range(num_of_octets):
            if int(split_address[octet]) <= 0 or int(split_address[octet]) >= 253:
                print(f"\n{W}[{Y}-{W}] Octet {octet + 1} ( {split_address[octet]} ) is invalid{R}!")
                return False

