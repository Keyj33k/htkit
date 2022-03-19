#!/usr/bin/env python3

# # # # # # # # # # # # # # # # # # # # # #
#                                         #
#   Author  :   Keyj33k                   #
#   Contact :   nomotikag33n@gmail.com    #
#   Twitter :   @keyjeek                  #
#   Github  :   @keyj33k                  #
#   Version :   1.0.0                     #
#                                         #
# # # # # # # # # # # # # # # # # # # # # # 

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
[i] Hunter is a small toolkit to perform information gathering.   
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
                HASHVAL = input("Text: ")
                        
                if HASHVAL == 'x':
                    print(colored("[i] EXIT", "red"))
                    return Hunter()
                        
                elif HASHVAL == 'c':
                    os.system('clear')
                    return md5()
                        
                result = hashlib.md5(HASHVAL.encode())
                print("[+] RESULT: ", end ="")
                print(result.hexdigest())
                return Hunter()
                        
            encrypt()
                  
            def decrypt():
                question_brute = input("Decrypt/Bruteforce the value? y/n: ")
                        
                if question_brute == 'y':
                    print("[i] USE THIS LINK: https://www.md5online.org/md5-decrypt.html ")## This program is using a big database to bruteforce the hash for you
                    return encrypt()
                        
                elif question_brute == 'x':
                    print(colored("Exiting ...", "red"))
                    return Hunter()
                        
                elif question_brute == 'c':
                    os.system('clear')
                    return decrypt()
                        
                elif question_brute == 'n':
                    question_exit = input("Exiting ...? y/n ")
                              
                    if question_exit == 'y':
                        print(colored("Exiting ...", "red"))
                        return Hunter()
                           
                    elif question_exit == 'x':
                        print(colored("Exiting ...", "red"))
                        return Hunter()
                              
                    elif question_exit == 'n':
                        return encrypt()
                              
                    else:
                        print(colored("Invalid Input!"))
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
            SCANNER = input('Target: ')
                        
            if SCANNER == 'x':
                print(colored("Exiting ...", "red"))
                return Hunter()
                        
            elif SCANNER == 'c':
                os.system('clear')
                return ipeye()
                        
            try:
                response = requests.post("http://ip-api.com/batch", json=[{"query":SCANNER}]).json()
                            
            except Exception:
                print(colored("CAN'T CONNECT. AN ERROR WAS DEFINED !", "red"))
                input("Press any key ...")
                os.system('clear')
                return Hunter()
                        
            os.system('clear')
                    
            for LOOKUP in response:
                for k, j in LOOKUP.items():
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
            CHOICE = input("[*] CHOICE: ")
                  
            if CHOICE == '1':
                HASH = input("[*] ENTER MESSAGE: ")
                        
                if HASH == 'x':
                    EXIT_CHOICE = input("[?] EXIT? y/n ")
                              
                    if EXIT_CHOICE == 'y':
                        print(colored("[i] Exit", "red"))
                        return Hunter()
                           
                    elif EXIT_CHOICE == 'n':
                        return chse()
                           
                    else:
                        print(colored("[i] INVALID INPUT!", "red"))
                        return chse()
                              
                elif HASH == 'clear':
                    os.system('clear')
                    return Hunter.base64encode()
                        
                elif HASH == 'c':
                    os.system('clear')
                    return Hunter.base64encode()
                        
                M_BYTES = CHOICE.encode('ascii')
                B64_E = base64.b64encode(M_BYTES)
                B64_HASH = B64_E.decode('ascii')
                print(B64_HASH)
                return chse()  
                     
            elif CHOICE == '2':
                def b64_decrypt():
                    print(chr(0xa))
                    B64_VAL = input("[*] ENTER HASH TO DECODE: ")
                           
                    if B64_VAL == 'x':
                        print(colored("[i] EXIT", "red"))
                        return Hunter()
                              
                    elif B64_VAL == 'exit':
                        print(colored("[i] EXIT", "red"))
                        return Hunter()
                           
                    elif B64_VAL == 'clear':
                        os.system('clear')
                        return b64_decrypt()
                              
                    elif B64_VAL == 'c':
                        os.system('clear')
                        return b64_decrypt()
                           
                    B64_D = B64_VAL.encode('ascii')
                    M_BYTE = base64.b64decode(B64_D)
                    RESULT = M_BYTE.decode('ascii')
                    print(RESULT)
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

 <by@keyjeek>  |  Follow the white rabbit...
<contact:nomotikag33n@gmail.com>       
[i] This Tool helps to find out some informations about a phonenumber. 
[i] Type 'x' or 'exit' to exit PhoneStalk.
[i] Type 'c' or 'clear' to clear the screen.
            """, "cyan"))

            while True:
                print(chr(0xa))
                TARGET_NUMBER = input('PHONENUMBER: ')
                        
                if TARGET_NUMBER == 'x':
                    print(colored("[i] EXIT", "red"))
                    return Hunter()
                        
                elif TARGET_NUMBER == 'c':
                    os.system('clear')
                    return Hunter()

                elif TARGET_NUMBER == 'help':
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
                    VALID_CHECK = phonenumbers.parse(TARGET_NUMBER)
                    IS_VALID = phonenumbers.is_valid_number(VALID_CHECK)
                    print(colored("Validation:", "yellow"))
                    print(IS_VALID)
                    print(chr(0xa))
                            
                    print(colored("Timezone:", "yellow"))
                    TIMEZONE = phonenumbers.parse(TARGET_NUMBER, "en")
                    print(timezone.time_zones_for_number(TIMEZONE))
                    print(chr(0xa))
                            
                    print(colored("Location:", "yellow"))
                    LOCATION = phonenumbers.parse(TARGET_NUMBER, "CH")
                    print(geocoder.description_for_number(LOCATION, "en"))

                    try:
                        print(colored("Provider:", "yellow"))
                        PROVIDER = phonenumbers.parse(TARGET_NUMBER, "RO")
                        print(carrier.name_for_number(PROVIDER, "en"))
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
