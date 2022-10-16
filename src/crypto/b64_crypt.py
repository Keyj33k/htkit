#!/usr/bin/env python3

try:
    from pyfiglet import figlet_format
    from termcolor import colored as cld
    from pwd import getpwuid
    from os import getuid
    import base64 as b64
    from src.colors.coloring import W, R, Y
except ImportError:
    raise RuntimeError("""
    Oops,
    
    this tool uses important modules, which don't seem to be 
    installed at the moment.
    
    Use the requirements file and this command:
    "pip3 install -r requirements.txt" 
    
    You will find this file in the req directory.
    """)

def build_result(value: str, to_crypt):
    try:
        print(f"{W}[{G}+{W}] {value}{R}:{W} {to_crypt}")
    except Exception as error:
        print(f"{W}[{Y}-{W}] Error{R}:{W} {error}")
    finally:
        input(f"{W}[{R}*{W}] Press enter key to continue")

USERNAME = getpwuid(getuid())[0]

class Crypt:
    @staticmethod
    def main():
        while True:
            print(cld(figlet_format("B64Crypt", font="bulbhead"), "yellow"))
            print(f"\n\t{W}[{R}1{W}] Encoder\n"
                  f"\t{W}[{R}2{W}] Decoder\n"
                  f"\t{W}[{R}x{W}] Exit")
            
            b64_choice = input(f"\n{W}[{R}*{W}] Choice {R}>>{Y} ")
            if b64_choice == "exit" or b64_choice == 'x': break
            
            match b64_choice: 
                case "1":
                    value_to_encrypt = str(input(f"{W}[{R}*{W}] {W}{USERNAME}{R}@{W}Hunter{R},{W} Value{R} >>{Y} "))
                    if value_to_encrypt == "exit" or value_to_encrypt == 'x': break
                    build_result(value_to_encrypt, b64.b64encode(value_to_encrypt.encode('ascii')).decode('ascii'))
                case "2":
                    hash_to_decrypt = str(input(f"{W}[{R}*{W}] {W}{USERNAME}{R}@{W}Hunter{R},{W} Value{R} >>{Y} "))
                    if hash_to_decrypt == "exit" or hash_to_decrypt == 'x': break
                    build_result(hash_to_decrypt, b64.b64decode(hash_to_decrypt.encode('ascii')).decode('ascii'))
                case _:
                    print(cld("Invalid Input!", "red"))
