#!/usr/bin/env python3

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
    [0] Exit
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
        ip_compile = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
        global port_max
        
        try:
            port_max = int(input("Max. Port ~#: "))
            # port_max = 65535
        except ValueError:
            print(cld("You need to enter an integer!", "red"))
            input("\nPress any key ...")
            return Hunter.witcher()

        port_min = 0
        target_address = input("Address(Type 'exit' to exit witcher) ~#: ")

        if target_address == "exit":
            print(cld("Exiting ..."))
            return Hunter()
        elif ip_compile.search(target_address):
            print(f"{target_address} is valid.")
            print("Scanning ...")

        time_start = dtt.now()
        nmap_scanner = nmap.PortScanner()

        for attack in range(port_min, port_max + 1):
            try:
                output = nmap_scanner.scan(target_address, str(attack))
                status = (output['scan'][target_address]['tcp'][attack]['state'])
                print(f"Port: {attack} Status: {status}")
            except KeyboardInterrupt:
                import time
                print(cld("\nCtrl+C pressed ...", "red"))
                time.sleep(0.5)
                print(cld("\nWitcher done!", "cyan"))
                print(chr(0xa))
                input("Press any key ...")
                return Hunter()

        time_stop = dtt.now()
        time_result = time_stop - time_start
        print(f"\nJob done in {time_result}!\n")
        input("\nPress any key ...")

    def subdomain_scanner():
        sds_banner = pfgt.figlet_format("Sub- domain- Scanner", font = "banner3-D")
        print(f"""\n{sds_banner}
\n<by@keyjeek>  |  Follow the white rabbit...
<contact:nomotikag33n@gmail.com> 
        """)
        
        found_subdomain = []
        target_address = input("Target ~#: ")

        with open("subdomains.txt") as FILE:
            read_file = FILE.read()
            SUBDOMAIN = read_file.splitlines()

            for list_domains in SUBDOMAIN:
                UniformResourceLocator = f"http://{list_domains}.{target_address}"

                try:
                    import requests
                    requests.get(UniformResourceLocator)
                except requests.ConnectionError:
                    from termcolor import colored
                    print(colored("Not available!", "red"))
                else:
                    print("Discovered:", UniformResourceLocator)
                    found_subdomain.append(UniformResourceLocator)

    def md5encrypt():
        md5_banner = pfgt.figlet_format("MD5C", font = "banner3-D")
        print(f"""\n{md5_banner} 
\n<by@keyjeek>  |  Follow the white rabbit...
<contact:nomotikag33n@gmail.com>       
[i] md5crypt is made to encrypt your string to an 128 bit hash value
[i] Type 'exit' to exit md5crypt.
        """)
        def md5():
            print(chr(0xa))
            def encrypt(): 
                hash_value = input("Text ~#: ")           
                if hash_value == "exit":
                    print(cld("Exit", "red"))
                    return Hunter()    
                try:
                    result = hashlib.md5(hash_value.encode())
                    print("Result: ", end ="")
                    print(result.hexdigest())
                    input("\nPress any key ...")
                    return Hunter()         
                except Exception as error:
                    print(cld(f"An error was defined! {error}", "red"))
                    input("\nPress any key ...")
                    os.system('clear')
                    return Hunter()
            encrypt()
                    
            def decrypt():
                question_brute = input("Decrypt/Bruteforce the value? y/n ~#: ")
                if question_brute == "y":
                    print("USE THIS LINK: https://www.md5online.org/md5-decrypt.html ") # This program is using a big database to bruteforce the hash for you
                    input("\nPress any key ...")
                    return Hunter()     
                elif question_brute == "n":
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
[i] Type 'exit' to exit ipeye.
            """)
                
            print(chr(0xa))
            ipeye_scanner = input("IPEye Target ~#: ")           
            if ipeye_scanner == "exit":
                print(cld("Exiting ...", "red"))
                return Hunter()      

            time_start = dtt.now()

            try:
                response = requests.post("http://ip-api.com/batch", json=[{"query":ipeye_scanner}]).json()   
            except Exception as error:
                print(cld(f"An error was defined! {error}", "red"))
                input("\nPress any key ...")
                os.system('clear')
                return Hunter()
                        
            os.system('clear')
                    
            for lookup in response:
                for k, j in lookup.items():
                    print(k,j)

            time_stop = dtt.now()
            time_result = time_stop - time_start              
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
        """, "cyan")
        global target_port
        target_address = input("Target ~#: ")

        try:
            target_port = int(input("Port ~#: "))
        except ValueError:
            print(cld("You need to enter an integer!", "red"))
            input("\nPress any key ...")

        if target_port == "exit":
            print(cld("Exiting ...", "red"))
            time.sleep(0.75)
            return Hunter
        elif target_port == "help":
            print(cld("""
 - type 'help'     to show help
 ------------------------------------------
 - type 'exit'     to exit the Banner Grabber
 - type 'clear'    to clear the screen\n 
            """, "yellow"))
            return Hunter.bannerGrabber()

        time_start = dtt.now()

        try:
            socket_sock = socket.socket()
            socket_sock.connect((target_address, target_port))
            print(cld("Getting Banner ... ", "yellow"))
            print(socket_sock.recv(1024))
            time_stop = dtt.now()
            time_result = time_stop - time_start
            print(f"\nJob done in {time_result}!\n")
            input("\nPress any key ...")
            return Hunter.bannerGrabber()
        except Exception as error:
            print(cld("Connection failed due to an error:", "red"))
            print(cld(error, "red"))
            time.sleep(0.75)
            return Hunter.bannerGrabber()

    def base64encode():   
        b64_banner = pfgt.figlet_format("B64-  CRYPT", font = "banner3-D")
        print(f"""\n{b64_banner} 
\n<by@keyjeek>  |  Follow the white rabbit...
<contact:nomotikag33n@gmail.com>       
[i] This Tool helps to encode and decode your text in base64.  
[i] Type 'exit' to exit Base64encode.
\t[1] Encoder
\t[2] Decoder
\t[x] Exit 
        """)
               
        choice = input("Choice ~#: ")
        if choice == "1":
            hash_value = input("Text: ") 
            if hash_value == "exit":
                return Hunter()     

            try:    
                m_bytes = hash_value.encode('ascii')
                b64_e = base64.b64encode(m_bytes)
                b64_hash = b64_e.decode('ascii')
                print(b64_hash)
                input("\nPress any key ...")
                return Hunter.base64encode()  
            except Exception as error:
                print(cld(f"An error was defined: {error}"))
                input("\nPress any key ...")
                return Hunter.base64encode()
                     
        elif choice == '2':
            decode_hash = input("Hash ~#: ")     
            if decode_hash == 'exit':
                print(cld("Exit", "red"))
                return Hunter()   
            try:
                b64_d = decode_hash.encode('ascii')
                m_byte = base64.b64decode(b64_d)
                result = m_byte.decode('ascii')
                print(result)
                input("\nPress any key ...")
                return Hunter.base64encode()   
            except Exception as error:
                print(cld(f"An error was defined: {error}"))
                input("\nPress any key ...")
                return Hunter.base64encode()

    def number_tracker():
        def PhoneStalk():
            pnsk_banner = pfgt.figlet_format("Phone- Stalk", font = "banner3-D")
            print(f"""\n{pnsk_banner} 
\n<by@keyjeek>  |  Follow the white rabbit...
<contact:nomotikag33n@gmail.com>       
[i] This Tool helps to find out some informations about a phonenumber. 
[i] Type 'exit' to exit PhoneStalk.
            """)

            while True:
                print(chr(0xa))
                target_phonenumber = input('PhoneStalk Target ~#: ')
                        
                if target_phonenumber == "exit":
                    print(cld("Exit", "red"))
                    return Hunter()    
                elif target_phonenumber == "help":
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
                time_start = dtt.now()

                print("Request\t\tResponse\n------------------------------------\n")
                    
                try:
                    valid_check = pnmb.parse(target_phonenumber)
                    finally_valid = pnmb.is_valid_number(valid_check)
                    print(f"Validation:\t{finally_valid}")
                    phonenumbers_timezone = pnmb.parse(target_phonenumber, "en")
                    final_timezone = tz.time_zones_for_number(phonenumbers_timezone)
                    print(f"Timezone:\t{final_timezone}")
                    phonenumbers_location = pnmb.parse(target_phonenumber, "CH")
                    final_phonenumbers_location = gc.description_for_number(phonenumbers_location, "en")
                    print(f"Location:\t{final_phonenumbers_location}")
                    phonenumbers_provider = pnmb.parse(target_phonenumber, "RO")
                    final_phonenumbers_provider = cr.name_for_number(phonenumbers_provider, "en")
                    print(f"Provider:\t{final_phonenumbers_provider}")
                    time_stop = dtt.now()
                    time_result = time_stop - time_start
                    print(f"\nJob done in {time_result}")        
                except Exception as error:
                    print(cld("[i] AN ERROR WAS DEFINED !", "red"))
                    print(cld(error, "red"))
                    time.sleep(2)
                    return Hunter()
                        
                print(chr(0xa))
                input("Press any key ...")
                return Hunter()
        PhoneStalk()   

if __name__ == "__main__":
    def hunter_main():
        while True:

            Hunter.banner()
            Hunter.menu()
            global hunter_choice

            try:
                hunter_choice = int(input("Choice ~#: "))
            except ValueError:
                print(cld("You need to enter an integer!", "red"))
                input("\nPress any key ...")
                return hunter_main()

            if hunter_choice == 1:
                Hunter.witcher()
            elif hunter_choice == 2:
                Hunter.md5encrypt()
            elif hunter_choice == 3:
                Hunter.eye_main()
            elif hunter_choice == 4:
                Hunter.bannerGrabber()
            elif hunter_choice == 5:
                Hunter.base64encode()
            elif hunter_choice == 6:
                Hunter.number_tracker()
            elif hunter_choice == 7:
                try:
                    Hunter.subdomain_scanner()
                except KeyboardInterrupt:
                    print(cld("\nCtrl+C pressed, Exiting ...", "red"))
                    input("\nPress any key ...")
                    return hunter_main()
            elif hunter_choice == 0:
                ex_banner = pfgt.figlet_format("Exit", font = "digital")
                print(cld(ex_banner, "red"))
                sys.exit(0)
            else:
                print(cld("Invalid Input!", "red"))
                input("\nPress any key ...")
                return hunter_main()
    hunter_main()
