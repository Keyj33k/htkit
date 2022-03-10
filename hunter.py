#!/usr/bin/env python3

from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier
from termcolor import colored
from datetime import datetime
from threading import Thread
import banner_whereareyou
from scapy.all import *
from tqdm import tqdm
import phonenumbers
import requests
import hashlib
import base64
import socket
import pandas
import time
import sys
import os
import re

class Hunter:

    def banner(): 
        os.system('clear')
        print(colored("""
█    █                 █
█    █                 █
█    █ █   █  █▒██▒  █████   ███    █▒██▒
█    █ █   █  █▓ ▒█    █    ▓▓ ▒█   ██  █
██████ █   █  █   █    █    █   █   █
█    █ █   █  █   █    █    █████   █
█    █ █   █  █   █    █    █       █
█    █ █▒ ▓█  █   █    █░   ▓▓  █   █
█    █ ▒██▒█  █   █    ▒██   ███▒   █
   
<by@keyjeek>  |  Follow the white rabbit... 
<contact:nomotikag33n@gmail.com>           
[i] Hunter is a small toolkit to perform information gathering   
[i] Type x to exit Hunter.              
        """, "cyan"))

    def menu():
        print(colored("""
[1] Witcher
[2] MD5Crypt
[3] IPEye
[4] Banner Grabber
[5] B64Crypt
[6] PhoneStalk
[x] EXIT
        """, "yellow"))

    def witcher():   
        print("""
          █                  █
█     █          █           █
█░ █ ░█          █           █
█░▒█▒░█ ███    █████   ▓██▒  █▒██▒   ███    █▒██▒
▓▒███▒█   █      █    ▓█  ▓  █▓ ▒█  ▓▓ ▒█   ██  █
▒▒█▒█▒▓   █      █    █░     █   █  █   █   █
▒██ ██▓   █      █    █      █   █  █████   █
▒█▓ ▓█▒   █      █    █░     █   █  █       █
░█▒ ▒█▒   █      █░   ▓█  ▓  █   █  ▓▓  █   █
 █   █▒ █████    ▒██   ▓██▒  █   █   ███▒   █
 
<by@keyjeek>  |  Follow the white rabbit...
<contact:nomotikag33n@gmail.com>      
[i] Witcher is a simple port scanner.  
[i] Type x to exit Witcher. 
                """)

        from termcolor import colored
        import nmap
        import re
        IP_COMPILE = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
        PORT_MAX = 65535
        PORT_MIN = 0
        TARGET_ADDR = input("Address: ")

        if TARGET_ADDR == 'x':
            print(colored("Exiting ..."))
            return Hunter()
        elif IP_COMPILE.search(TARGET_ADDR):
            print(f"{TARGET_ADDR} is valid.")
            print("Scanning ...")

        SCANNER = nmap.PortScanner()

        for ATTACK in range(PORT_MIN, PORT_MAX + 1):
            try:
                OUTPUT = SCANNER.scan(TARGET_ADDR, str(ATTACK))
                STATUS = (OUTPUT['scan'][TARGET_ADDR]['tcp'][ATTACK]['state'])
                print(f"Port: {ATTACK} Status: {STATUS}")
                    
            except KeyboardInterrupt:
                import time
                print(colored("\nCtrl+C pressed. Exiting ...", "red"))
                time.sleep(1.25)
                print(colored("Witcher done!", "cyan"))
                print(chr(0xa))
                input("Press any key ...")
                return Hunter()

    def md5encrypt():
        def banner():
            print("""   
            █
            █  █████                                             █
            █  █                                                 █
██▓█▓   ██▓█  █       ███   █▒██▒   ▓██▒   █▒██▒ █░  █  █▓██   █████
█▒█▒█  █▓ ▓█  ████▒  ▓▓ ▒█  █▓ ▒█  ▓█  ▓   ██  █ ▓▒ ▒▓  █▓ ▓█    █
█ █ █  █   █     ░█▓ █   █  █   █  █░      █     ▒█ █▒  █   █    █
█ █ █  █   █       █ █████  █   █  █       █      █ █   █   █    █
█ █ █  █   █       █ █      █   █  █░      █      █▓▓   █   █    █
█ █ █  █▓ ▓█  █░  █▓ ▓▓  █  █   █  ▓█  ▓   █      ▓█▒   █▓ ▓█    █░
█ █ █   ██▓█  ▒███▓   ███▒  █   █   ▓██▒   █      ▒█    █▓██     ▒██
                                                  ▒█    █
                                                  █▒    █
                                                  ██    █
<by@keyjeek>  |  Follow the white rabbit...
<contact:nomotikag33n@gmail.com>       
[i] md5encrypt is made to encrypt your string to an 128 bit hash value
[i] Type x to exit md5encrypt.
            """)
        banner()
               
        def md5():
            print(chr(0xa))
            def encrypt(): 
                hash_val = input("[*] TEXT TO HASH: ")
                        
                if hash_val == 'x':
                    print(colored("[i] EXIT", "red"))
                    return Hunter()
                        
                elif hash_val == 'exit':
                    print(colored("[i] EXIT", "red"))
                    return Hunter()
                        
                elif hash_val == 'clear':
                    os.system('clear')
                    return md5()
                        
                elif hash_val == 'c':
                    os.system('clear')
                    return md5()
                        
                result = hashlib.md5(hash_val.encode())
                print("[+] RESULT: ", end ="")
                print(result.hexdigest())
                return Hunter()
                        
            encrypt()
                  
            def decrypt():
                question_brute = input("[?] DECRYPT/BRUTEFORCE THE HASH? y/n: ")
                        
                if question_brute == 'y':
                    print("[i] USE THIS LINK: https://www.md5online.org/md5-decrypt.html ")## This program is using a big database to bruteforce the hash for you
                    return encrypt()
                        
                elif question_brute == 'x':
                    print(colored("[i] EXIT", "red"))
                    return Hunter()
                        
                elif question_brute == 'exit':
                    print(colored("[i] EXIT", "red"))
                    return Hunter()
                        
                elif question_brute == 'clear':
                    os.system('clear')
                    return decrypt()
                        
                elif question_brute == 'c':
                    os.system('clear')
                    return decrypt()
                        
                elif question_brute == 'n':
                    question_exit = input("[?] EXIT? y/n ")
                              
                    if question_exit == 'y':
                        print(colored("[i] Exit", "red"))
                        return Hunter()
                           
                    elif question_exit == 'x':
                        print(colored("[i] Exit", "red"))
                        return Hunter()
                              
                    elif question_exit == 'n':
                        return encrypt()
                              
                    else:
                        print("[i] INVALID INPUT !")
                        return Hunter()

            decrypt()
                  
        md5()

    def eye_main():
        def ipeye():
            print("""
  █████  █████░
    █    █   ▓█
    █    █    █  ███   █░  █   ███
    █    █   ▓█ ▓▓ ▒█  ▓▒ ▒▓  ▓▓ ▒█
    █    █████░ █   █  ▒█ █▒  █   █
    █    █      █████   █ █   █████
    █    █      █       █▓▓   █
    █    █      ▓▓  █   ▓█▒   ▓▓  █
 █████   █       ███▒   ▒█     ███▒
                        ▒█
                        █▒
                        ██
<by@keyjeek>  |  Follow the white rabbit...")
<contact:nomotikag33n@gmail.com>       ")
[i] IPEye is a Tool to find out
   --> some information about an IP.  ")
[i] Type x to exit IPEye.")
            """)
                
            print(chr(0xa))
            scanner = input('[*] IP: ')
                        
            if scanner == 'x':
                print(colored("[i] EXIT", "red"))
                return Hunter()
                        
            elif scanner == 'exit':
                print(colored("[i] EXIT", "red"))
                return Hunter()
                        
            elif scanner == 'clear':
                os.system('clear')
                return ipeye()
                        
            elif scanner == 'c':
                os.system('clear')
                return ipeye()
                        
            try:
                response = requests.post("http://ip-api.com/batch", json=[{"query":scanner}]).json()
                            
            except Exception:
                print(colored("CAN'T CONNECT. AN ERROR WAS DEFINED !", "red"))
                input("Press any key ...")
                os.system('clear')
                return Hunter()
                        
            os.system('clear')
                    
            for ip in response:
                for k, j in ip.items():
                    print(k,j)
                                
            print(chr(0xa))
            print("[i] SCANNER DONE !")
            print(chr(0xa))
            input("Press any key ...")
            return Hunter()

        ipeye()

    def bannerGrabber():
        import socket
        print(colored("""
                                                                       █
 █████░                                            ▒███▒               █
 █   ▒█                                           ░█▒ ░█               █
 █    █ ░███░  █▒██▒  █▒██▒   ███    █▒██▒        █▒      █▒██▒ ░███░  █▓██
 █   ▒█ █▒ ▒█  █▓ ▒█  █▓ ▒█  ▓▓ ▒█   ██  █        █       ██  █ █▒ ▒█  █▓ ▓█
 █████░     █  █   █  █   █  █   █   █            █   ██  █         █  █   █
 █   ▒█ ▒████  █   █  █   █  █████   █            █    █  █     ▒████  █   █
  █    █ █▒  █  █   █  █   █  █       █            █▒   █  █     █▒  █  █   █
 █   ▒█ █░ ▓█  █   █  █   █  ▓▓  █   █            ▒█░ ░█  █     █░ ▓█  █▓ ▓█
 █████░ ▒██▒█  █   █  █   █   ███▒   █             ▒███▒  █     ▒██▒█  █▓██
                                          ██████

        """, "cyan"))
        TARGET_ADDR = input("Target: ")
        TARGET_PORT = input("Port: ")

        if TARGET_PORT == 'x':
            print(colored("Exiting ...", "red"))
            sys.exit(0)

        elif TARGET_PORT == 'c':
            os.system('clear')
            return Hunter.bannerGrabber()

        elif TARGET_PORT == 'h':
            print(colored("""

 - type 'h'     to show help
 ------------------------------------------
 - type 'x'     to exit the Banner Grabber
 - type 'c'     to clear the screen
                    
            """, "yellow"))
            return Hunter.bannerGrabber()

        try:
            socket_sock = socket.socket()
            socket_sock.connect((TARGET_ADDR, int(TARGET_PORT)))
            print(colored("Result: ", "yellow"))
            print(socket_sock.recv(1024))
            input("Press any key ...")
            return Hunter.bannerGrabber()

        except Exception as ERROR:
            print(colored("Connection failed due to an error:", "red"))
            print(ERROR)
            time.sleep(1.25)
            return Hunter.bannerGrabber()

    def base64encode():   
        def banner():
            print("""
                                                                  
                                                        
█████░  ▒███▒    ██   ░███▒ █████ █▒   ▒█ █████░███████
█   ▒█ ░█▒  ▓   ▒██  ░█▒ ░█ █   ▓█░█   █░ █   ▓█   █   
█    █ █▒       █░█  █▒     █    █ ▒█ █▒  █    █   █   
█   ▒█ █▒███   ▓▓ █  █      █   ▒█  █▓█   █   ▓█   █   
█████░ █▓  ▓█ ░█  █  █      █████   ▒█▒   █████░   █   
█   ▒█ █    █ █▒  █  █      █  ░█▒   █    █        █   
█    █ █    █ ██████ █▒     █   ░█   █    █        █   
█   ▒█ ▒▓  ▓█     █  ░█▒ ░▓ █    █   █    █        █   
█████░  ▓███      █   ▒███▒ █    ▒   █    █        █    
<by@keyjeek>  |  Follow the white rabbit...
<contact:nomotikag33n@gmail.com>       
[i] This Tool helps to encode and decode your text in base64.  
[i] Type 'x' or 'exit' to exit Base64encode.
[i] Type 'c' or 'clear' to clear the screen.
            """)

        banner()
               
        def menu():
            print("""
[1] Encoder
[2] Decoder
[x] Exit 
            """)
                  
        menu()
               
        def chse():
            choice = input("[*] CHOICE: ")
                  
            if choice == '1':
                hash_value = input("[*] ENTER MESSAGE: ")
                        
                if hash_value == 'x':
                    exit_choice = input("[?] EXIT? y/n ")
                              
                    if exit_choice == 'y':
                        print(colored("[i] Exit", "red"))
                        return Hunter()
                           
                    elif exit_choice == 'n':
                        return chse()
                           
                    else:
                        print(colored("[i] INVALID INPUT!", "red"))
                        return chse()
                              
                elif hash_value == 'clear':
                    os.system('clear')
                    return Hunter.base64encode()
                        
                elif hash_value == 'c':
                    os.system('clear')
                    return Hunter.base64encode()
                        
                m_bytes = choice.encode('ascii')
                b64_e = base64.b64encode(m_bytes)
                b64_hash = b64_e.decode('ascii')
                print(b64_hash)
                return chse()  
                     
            elif choice == '2':
                def b64_decrypt():
                    print(chr(0xa))
                    b64_hash_val = input("[*] ENTER HASH TO DECODE: ")
                           
                    if b64_hash_val == 'x':
                        print(colored("[i] EXIT", "red"))
                        return Hunter()
                              
                    elif b64_hash_val == 'exit':
                        print(colored("[i] EXIT", "red"))
                        return Hunter()
                           
                    elif b64_hash_val == 'clear':
                        os.system('clear')
                        return b64_decrypt()
                              
                    elif b64_hash_val == 'c':
                        os.system('clear')
                        return b64_decrypt()
                           
                    b64_d = b64_hash_val.encode('ascii')
                    m_bytes = base64.b64decode(b64_d)
                    result = m_bytes.decode('ascii')
                    print(result)
                    return chse()
                           
                b64_decrypt()

        chse()

    def number_tracker():
        def PhoneStalk():
            print(colored("""

        █                                                ███    █
 █████░ █                            ▓███▒   █             █    █
 █   ▓█ █                           █▓  ░█   █             █    █
 █    █ █▒██▒   ███   █▒██▒   ███   █      █████  ░███░    █    █  ▒█
 █   ▓█ █▓ ▒█  █▓ ▓█  █▓ ▒█  ▓▓ ▒█  █▓░      █    █▒ ▒█    █    █ ▒█
 █████░ █   █  █   █  █   █  █   █   ▓██▓    █        █    █    █▒█
 █      █   █  █   █  █   █  █████      ▓█   █    ▒████    █    ██▓
 █      █   █  █   █  █   █  █           █   █    █▒  █    █    █░█░
 █      █   █  █▓ ▓█  █   █  ▓▓  █  █░  ▓█   █░   █░ ▓█    █░   █ ░█
 █      █   █   ███   █   █   ███▒  ▒████░   ▒██  ▒██▒█    ▒██  █  ▒█

            """, "cyan"))

            while True:
                print(chr(0xa))
                number = input('PHONENUMBER: ')
                        
                if number == 'x':
                    print(colored("[i] EXIT", "red"))
                    return Hunter()
                        
                elif number == 'c':
                    os.system('clear')
                    return Hunter()

                elif number == 'help':
                    print(colored("""
 HELP; WhoAreYou
< ============= >
'/x' or '/exit'        Return Menu / Exit WhoAreYou
'/c' or '/clear'       Clear Screen             
                """, "yellow"))
                    print(chr(0xa))
                    input("Press any key ...")
                    return Hunter()
                
                print(chr(0xa))
                    
                try:
                    valid_check = phonenumbers.parse(number)
                    is_valid = phonenumbers.is_valid_number(valid_check)
                    print(colored("Validation:", "yellow"))
                    print(is_valid)
                    print(chr(0xa))
                            
                    print(colored("Timezone:", "yellow"))
                    timezone_number = phonenumbers.parse(number, "en")
                    print(timezone.time_zones_for_number(timezone_number))
                    print(chr(0xa))
                            
                    print(colored("Location:", "yellow"))
                    target_number = phonenumbers.parse(number, "CH")
                    print(geocoder.description_for_number(target_number, "en"))

                    try:
                        print(colored("Provider:", "yellow"))
                        provider_info = phonenumbers.parse(number, "RO")
                        print(carrier.name_for_number(provider_info, "en"))
                        print(chr(0xa))

                    except Exception:
                        print(colored("Provider info not available !", "red"))
                        time.sleep(2)
                            
                except Exception:
                    print(colored("[i] AN ERROR WAS DEFINED !", "red"))
                    time.sleep(2)
                    return Hunter()
                        
                print(chr(0xa))
                input('Press any key ...')
                return PhoneStalk()

        PhoneStalk()   

if __name__ == "__main__":
    while True:
        Hunter.banner()
        Hunter.menu()
        CHOICE = input("Choice: ")

        if CHOICE == '1':
            Hunter.witcher()

        elif CHOICE == '2':
            Hunter.md5encrypt()

        elif CHOICE == '3':
            Hunter.eye_main()

        elif CHOICE == '4':
            Hunter.bannerGrabber

        elif CHOICE == '5':
            Hunter.base64encode()

        elif CHOICE == '6':
            Hunter.number_tracker()

        elif CHOICE == 'x':
            print(colored("Exiting ..."))
            sys.exit(0)

        else:
            print(colored("Invalid Input!", "red"))
