#!/usr/bin/env python3

from pwd import getpwuid
from os import getuid

Y = "\033[0;33m"
G = "\033[0;32m"
W = "\033[0;37m"
R = "\033[0;31m"

USERNAME = getpwuid(getuid())[0]

def exit_str_err(command: str, tool: str):
    if command == 'x' or command == "exit":
        print(f"{W}[{Y}-{W}] Error{R}:{W} {R}'{W}{command}{R}'{W} is"
              f" invalid{R}.{W} Please use Ctrl{R}+{W}C to exit {tool}{R}!{W}")
        return False
    return True


def exit_int_err(command: int, tool: str):
    if command == 0:
        print(f"{W}[{Y}-{W}] Error{R}:{W} {R}'{W}{command}{R}'{W} is "
              f"invalid{R}.{W} Please use Ctrl{R}+{W}C to exit {tool}{R}!{W}")
        return False
    return True

class InputGrabber:
    @staticmethod
    def grab_wordlist(service: str):
        while True:
            wordlist = str(input(f"{W}[{R}*{W}] {W}{USERNAME}{R}@{W}htkit{R},{W} Wordlist "
                                 f"{R}({W} Enter For Default Wordlist {R}) >>{Y} "))
            if exit_str_err(wordlist, service) is True: return wordlist

    @staticmethod
    def grab_address(service: str):
        while True:
            address = str(input(f"{W}[{R}*{W}] {W}{USERNAME}{R}@{W}htkit{R},{W} Address{R} >>{Y} "))
            if exit_str_err(address, service) is True: return address

    @staticmethod
    def grab_ipv4(service: str):
        while True:
            ipv4 = str(input(f"{W}[{R}*{W}] {W}{USERNAME}{R}@{W}htkit{R},{W} IPv4{R} >>{Y} "))
            if exit_str_err(ipv4, service) is True: return ipv4

    @staticmethod
    def grab_phonenumber(service: str):
        while True:
            phonenumber = str(input(f"{W}[{R}*{W}] {W}{USERNAME}{R}@{W}htkit{R},{W} Phonenumber{R} >>{Y} "))
            if exit_str_err(phonenumber, service) is True: return phonenumber

    @staticmethod
    def grab_url(service: str):
        while True:
            url = str(input(f"{W}[{R}*{W}] {W}{USERNAME}{R}@{W}htkit{R},{W} URL{R} >>{Y} "))
            if exit_str_err(url, service) is True: return url

    @staticmethod
    def grab_int(service: str, category: str):
        while True:
            value = int(input(f"{W}[{R}*{W}] {W}{USERNAME}{R}@{W}htkit{R},{W} {category}{R} >>{Y} "))
            if exit_int_err(value, service) is True: return value

    @staticmethod
    def grab_sec_port(service: str):
        while True:
            last_port = int(input(f"{W}[{R}*{W}] {W}{USERNAME}{R}@{W}htkit{R},{W} Max{R}.{W} Port{R} >>{Y} "))
            if exit_int_err(last_port, service) is True: return last_port

    @staticmethod
    def grab_ip_val(service: str):
        while True:
            value = str(input(f"{W}[{R}*{W}] {W}{USERNAME}{R}@{W}htkit{R},"
                              f"{W} IPv4 Address {R}({W} First Three Octets Only {R}) >>{Y} "))
            if exit_str_err(value, service) is True: return value
