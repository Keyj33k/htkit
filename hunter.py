#!/usr/bin/env python3

# # # # # # # # # # # # # # # # # # # # # #
#                                         #
#   Author  :   Keyj33k                   #
#   Contact :   nomotikag33n@gmail.com    #
#   Twitter :   @keyjeek                  #
#   Github  :   @keyj33k                  #
#   Insta   :   @keyjeek                  #
#   Version :   1.0.4                     #
#                                         #
# # # # # # # # # # # # # # # # # # # # # # 

from phonenumbers import timezone as tz
from phonenumbers import geocoder as gc
from phonenumbers import carrier as cr
from termcolor import colored as cld
from datetime import datetime as dtt
import phonenumbers as pnmb
import pyfiglet as pfgt
import requests
import hashlib
import base64
import time
import sys
import os

class Hunter:

    def banner(): 
        os.system('clear')
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
   
    <by@keyjeek>  |  Follow the white rabbit... 
    <contact:nomotikag33n@gmail.com>           
    [i] Hunter is a small toolkit to perform information gathering.   
    [i] Type x to exit Hunter.              
        """, "cyan"))

    def menu():
        print(cld("""
    [1] Witcher
    [2] MD5Crypt
    [3] IPEye
    [4] BannerGrabber
    [5] B64Crypt
    [6] PhoneStalk
    [7] SubdomainScanner
    [exit] Exit
        """, "yellow"))

    def witcher():  
        w_banner = pfgt.figlet_format("Witcher", font = "banner3-D")
        print(f"""\n{w_banner}
\n<by@keyjeek>  |  Follow the white rabbit...
<contact:nomotikag33n@gmail.com>      
[i] Witcher is a simple port scanner.  
                """)

        import nmap
        import re

        IP_COMPILE = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
        PORT_MAX = int(input("Max. Port: "))
        # PORT_MAX = 65535
        PORT_MIN = 0
        TARGET_ADDR = input("Address(Type 'exit' to exit witcher): ")

        if TARGET_ADDR == "exit":
            print(cld("Exiting ..."))
            return Hunter()
        
        elif IP_COMPILE.search(TARGET_ADDR):
            print(f"{TARGET_ADDR} is valid.")
            print("Scanning ...")

        timestart = dtt.now()

        SCANNER = nmap.PortScanner()

        for ATTACK in range(PORT_MIN, PORT_MAX + 1):
            try:
                OUTPUT = SCANNER.scan(TARGET_ADDR, str(ATTACK))
                STATUS = (OUTPUT['scan'][TARGET_ADDR]['tcp'][ATTACK]['state'])
                print(f"Port: {ATTACK} Status: {STATUS}")
                    
            except KeyboardInterrupt:
                import time
                print(cld("\nCtrl+C pressed. Exiting ...", "red"))
                time.sleep(1.25)
                print(cld("Witcher done!", "cyan"))
                print(chr(0xa))
                input("Press any key ...")
                return Hunter()

        timestop = dtt.now()
        time_result = timestop - timestart
        print(f"\nJob done in {time_result}!\n")
        input("Press any key ...")

    def subdomain_scanner():
        sds_banner = pfgt.figlet_format("Sub- domain- Scanner", font = "banner3-D")
        print(f"""\n{sds_banner}
\n<by@keyjeek>  |  Follow the white rabbit...
<contact:nomotikag33n@gmail.com> 
        """)
        
        FOUND_SD = []
        TARGET_ADDR = input("Target: ")

        with open("subdomains.txt") as FILE:
            READFILE = FILE.read()
            SUBDOMAIN = READFILE.splitlines()

            for LIST_DOMAINS in SUBDOMAIN:
                UniformResourceLocator = f"http://{LIST_DOMAINS}.{TARGET_ADDR}"

                try:
                    import requests
                    requests.get(UniformResourceLocator)

                except requests.ConnectionError:
                    from termcolor import colored
                    print(colored("Not available!", "red"))

                else:
                    print("Discovered:", UniformResourceLocator)
                    FOUND_SD.append(UniformResourceLocator)

    def md5encrypt():
        md5_banner = pfgt.figlet_format("MD5C", font = "banner3-D")
        print(f"""\n{md5_banner} 
\n<by@keyjeek>  |  Follow the white rabbit...
<contact:nomotikag33n@gmail.com>       
[i] md5crypt is made to encrypt your string to an 128 bit hash value
[i] Type 'exit' or 'exit' to exit md5crypt.
[i] Type 'clear' or 'clear' to clear the screen.
        """)
        def md5():
            print(chr(0xa))
            def encrypt(): 
                HASHVAL = input("Text: ")
                            
                if HASHVAL == "exit":
                    print(cld("Exit", "red"))
                    return Hunter()
                            
                elif HASHVAL == "clear":
                    os.system('clear')
                    return md5()
                            
                result = hashlib.md5(HASHVAL.encode())
                print("Result: ", end ="")
                print(result.hexdigest())
                return Hunter()
                            
            encrypt()
                    
            def decrypt():
                question_brute = input("Decrypt/Bruteforce the value? y/n: ")
                            
                if question_brute == "y":
                    print("USE THIS LINK: https://www.md5online.org/md5-decrypt.html ")## This program is using a big database to bruteforce the hash for you
                    input("Press any key ...")
                    return Hunter()
                            
                elif question_brute == "n":
                    question_exit = input("Exiting ...? y/n ")
                                
                    if question_exit == "y":
                        print(cld("Exiting ...", "red"))
                        return Hunter()
                        #break
                            
                    elif question_exit == "exit":
                        print(cld("Exiting ...", "red"))
                        return Hunter()
                                
                    elif question_exit == "n":
                        return encrypt()
                            
                    else:
                        print(cld("Invalid Input!"))
                        return Hunter()

            decrypt()
                    
        md5()

    def eye_main():
        def ipeye():
            ipe_banner = pfgt.figlet_format("IPEYE", font = "banner3-D")
            print(f"""\n{ipe_banner} 
\n<by@keyjeek>  |  Follow the white rabbit...
<contact:nomotikag33n@gmail.com>       
[i] IPEye is a Tool to find out
   --> some information about an IP.  
[i] Type 'exit' or 'exit' to exit ipeye.
[i] Type 'clear' or 'clear' to clear the screen.
            """)
                
            print(chr(0xa))
            SCANNER = input("IPEye Target: ")
                        
            if SCANNER == "exit":
                print(cld("Exiting ...", "red"))
                return Hunter()
                        
            elif SCANNER == "clear":
                os.system('clear')
                return ipeye()

            timestart = dtt.now()

            try:
                response = requests.post("http://ip-api.com/batch", json=[{"query":SCANNER}]).json()
                            
            except Exception:
                print(cld("An error was defined!", "red"))
                input("Press any key ...")
                os.system('clear')
                return Hunter()
                        
            os.system('clear')
                    
            for LOOKUP in response:
                for k, j in LOOKUP.items():
                    print(k,j)

            timestop = dtt.now()
            time_result = timestop - timestart
                                
            print(chr(0xa))
            print(f"Scanner done in {time_result}!")
            print(chr(0xa))
            input("Press any key ...")
            return Hunter()

        ipeye()

    def bannerGrabber():

        import socket
        bg_banner = pfgt.figlet_format("Banner-Grabber", font = "banner3-D")
        print(f"""\n{bg_banner} 
\n<by@keyjeek>  |  Follow the white rabbit...
<contact:nomotikag33n@gmail.com>  
[i] Type 'exit' or 'exit' to exit banner grabber.
[i] Type 'clear' or 'clear' to clear the screen.
        """, "cyan")
        TARGET_ADDR = input("Target: ")
        TARGET_PORT = input("Port: ")

        if TARGET_PORT == "exit":
            print(cld("Exiting ...", "red"))
            time.sleep(1.25)
            return Hunter

        elif TARGET_PORT == "clear":
            os.system('clear')
            return Hunter.bannerGrabber()

        elif TARGET_PORT == "help":
            print(cld("""
 - type 'help'     to show help
 ------------------------------------------
 - type 'exit'     to exit the Banner Grabber
 - type 'clear'    to clear the screen
                    
            """, "yellow"))
            return Hunter.bannerGrabber()

        timestart = dtt.now()

        try:
            socket_sock = socket.socket()
            socket_sock.connect((TARGET_ADDR, int(TARGET_PORT)))
            print(cld("Result: ", "yellow"))
            print(socket_sock.recv(1024))
            timestop = dtt.now()
            time_result = timestop - timestart
            print(f"\nJob done in {time_result}!\n")
            input("Press any key ...")
            return Hunter.bannerGrabber()

        except Exception as ERROR:
            print(cld("Connection failed due to an error:", "red"))
            print(ERROR)
            time.sleep(1.25)
            return Hunter.bannerGrabber()

    def base64encode():   
        b64_banner = pfgt.figlet_format("B64CRYPT", font = "banner3-D")
        print(f"""\n{b64_banner} 
\n<by@keyjeek>  |  Follow the white rabbit...
<contact:nomotikag33n@gmail.com>       
[i] This Tool helps to encode and decode your text in base64.  
[i] Type 'exit' or 'exit' to exit Base64encode.
[i] Type 'clear' or 'clear' to clear the screen.
\t[1] Encoder
\t[2] Decoder
\t[x] Exit 
        """)
               
        def chse():
            CHOICE = input("Choice: ")
                  
            if CHOICE == "1":
                HASH = input("Text: ")
                        
                if HASH == "exit":
                    EXIT_CHOICE = input("Exit? y/n ")
                              
                    if EXIT_CHOICE == "y":
                        print(cld("Exit", "red"))
                        time.sleep(1.25)
                        return Hunter()
                           
                    elif EXIT_CHOICE == "n":
                        return chse()
                           
                    else:
                        print(cld("Invalid input!", "red"))
                        input("Press any key ...")
                        return chse()
                              
                elif HASH == "clear":
                    os.system('clear')
                    return Hunter.base64encode()
                        
                M_BYTES = HASH.encode('ascii')
                B64_E = base64.b64encode(M_BYTES)
                B64_HASH = B64_E.decode('ascii')
                print(B64_HASH)
                return chse()  
                     
            elif CHOICE == '2':
                def b64_decrypt():
                    B64_VAL = input("Hash: ")
                              
                    if B64_VAL == 'exit':
                        print(cld("Exit", "red"))
                        return Hunter()
                           
                    elif B64_VAL == 'clear':
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
            pnsk_banner = pfgt.figlet_format("Phone- Stalk", font = "banner3-D")
            print(f"""\n{pnsk_banner} 
\n<by@keyjeek>  |  Follow the white rabbit...
<contact:nomotikag33n@gmail.com>       
[i] This Tool helps to find out some informations about a phonenumber. 
[i] Type 'exit' or 'exit' to exit PhoneStalk.
[i] Type 'clear' or 'clear' to clear the screen.
            """)

            while True:
                print(chr(0xa))
                TARGET_NUMBER = input('PhoneStalk Target: ')
                        
                if TARGET_NUMBER == "exit":
                    print(cld("Exit", "red"))
                    return Hunter()
                        
                elif TARGET_NUMBER == "clear":
                    os.system('clear')
                    return Hunter()

                elif TARGET_NUMBER == "help":
                    print(cld("""
 HELP; WhoAreYou
< ============= >
'exit'        Return Menu / Exit WhoAreYou
'clear'       Clear Screen             
                """, "yellow"))
                    print(chr(0xa))
                    input("Press any key ...")
                    return Hunter()
                
                print(chr(0xa))

                timestart = dtt.now()
                    
                try:
                    VALID_CHECK = pnmb.parse(TARGET_NUMBER)
                    IS_VALID = pnmb.is_valid_number(VALID_CHECK)
                    print(cld("Validation:", "yellow"))
                    print(IS_VALID)
                    print(chr(0xa))
                            
                    print(cld("Timezone:", "yellow"))
                    TIMEZONE = pnmb.parse(TARGET_NUMBER, "en")
                    print(tz.time_zones_for_number(TIMEZONE))
                    print(chr(0xa))
                            
                    print(cld("Location:", "yellow"))
                    LOCATION = pnmb.parse(TARGET_NUMBER, "CH")
                    print(gc.description_for_number(LOCATION, "en"))

                    print(cld("Provider:", "yellow"))
                    PROVIDER = pnmb.parse(TARGET_NUMBER, "RO")
                    print(cr.name_for_number(PROVIDER, "en"))
                    print(chr(0xa))

                    timestop = dtt.now()
                    time_result = timestop - timestart
                    print(f"Job done in {time_result}")
                            
                except Exception as error:
                    print(cld("[i] AN ERROR WAS DEFINED !", "red"))
                    print(cld(error, "red"))
                    time.sleep(2)
                    return Hunter()
                        
                print(chr(0xa))
                input('Press any key ...')
                return Hunter()

        PhoneStalk()   

if __name__ == "__main__":
    def hunter_main():
        while True:

            Hunter.banner()
            Hunter.menu()
            CHOICE = input("Choice: ")

            if CHOICE == "1":
                Hunter.witcher()
            elif CHOICE == "2":
                Hunter.md5encrypt()
            elif CHOICE == "3":
                Hunter.eye_main()
            elif CHOICE == "4":
                Hunter.bannerGrabber()
            elif CHOICE == "5":
                Hunter.base64encode()
            elif CHOICE == "6":
                Hunter.number_tracker()
            elif CHOICE == "7":
                timestart = dtt.now()
                try:
                    Hunter.subdomain_scanner()
                except KeyboardInterrupt:
                    print(cld("\nCtrl+C pressed, Exiting ...", "red"))
                    input("Press any key ...")
                    return hunter_main()
            elif CHOICE == "exit" or "x":
                print(cld("Exiting ...", "red"))
                sys.exit(0)
            else:
                print(cld("Invalid Input!", "red"))
                input("Press any key ...")
                return hunter_main()

    hunter_main()
