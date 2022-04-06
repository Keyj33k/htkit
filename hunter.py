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
#   Version :   1.0.7                     #
#                                         #
# # # # # # # # # # # # # # # # # # # # # # 

class Hunter:

    def banner(): 
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
        """, "cyan"))

    def menu():
        print(cld("""
    [0] Clear Screen
    [1] Witcher
    [2] MD5Crypt
    [3] IPEye
    [4] BannerGrabber
    [5] B64Crypt
    [6] PhoneStalk
    [7] SubdomainScanner
    [99] Exit
        """, "yellow"))

    def witcher():  
        import socket
        print(chr(0xa))
        witcher_banner = pfgt.figlet_format("welcome", font="banner3-D")
        print(cld(witcher_banner, "cyan"))
        import time
        time.sleep(1.05)

        os.system("clear")
        witcher_banner = pfgt.figlet_format("witcher", font="banner3-D")
        print(cld(witcher_banner, "cyan"))
        print("*" * 18, "A python portscanner project ...", "*" * 18)
        print("*" * 24, " *writtenby@Keyj33k ", "*" * 24)

        try:
            print(cld("\nTarget ~#:", "yellow"))
            target_address = input()
            if target_address == "exit":
                return Hunter()
        except ValueError:
            print(cld("\nYou need to enter a string!", "red"))
            input("\nPress any key ...")

        print("-" * 70)
        scan_start = dtt.now()
        print(cld(f"Started scanning at:\t\t\t{scan_start}", "green"))
        print("-" * 70)
        time_start = dtt.now()

        try:
            for target in range(1, 65535):
                socket_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
                socket_sock.settimeout(1) 

                final_result = socket_sock.connect_ex((target_address, target)) 
                if final_result == 0: 
                    print("Port\t{}\t\t\t\t\t   open".format(target))
                socket_sock.close() 

        except socket.error as socket_error:
            print(cld(socket_error, "red"))

        except KeyboardInterrupt:
            print(cld("\nCtrl+C pressed. Exit.", "red"))
            return Hunter()

        time_stop = dtt.now() 
        needed_time = time_stop - time_start
        print("-" * 70)
        print(cld(f"\nScanner done in {needed_time}!", "green"))
        print(chr(0xa))
        input("Press any key ...")

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

    def banner_grabber():
        import socket 

        tab2 = "\t" * 2
        tab3 = "\t" * 3
        line = "--" * 42

        info_array = ["@Keyj33k", "1.0.1", "06.04.22", "Python3"]
        links = ["https://github.com/Keyj33k", "https://www.instagram.com/keyjeek/", "nomotikag33n@gmail.com"]
        author_name = info_array[0]
        version_num = info_array[1]
        written_on = info_array[2]
        progr_lang = info_array[3]
        instagram = links[1]
        github = links[0]
        email = links[2]

        while True:
            print(cld("\n[*] Target (Type 'exit' to exit banner grabber) ~#:", "yellow"))
            target_host = input()
            if target_host == "exit":
                os.system("clear")
                return Hunter()
            print(cld("[*] Port (Type 'exit' to exit banner grabber) ~#:", "yellow"))
            target_port = input()
            if target_port == "exit":
                os.system("clear")
                return Hunter()

            try:
                socket_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket_sock.connect_ex((str(target_host), int(target_port)))
                banner_result = socket_sock.recv(1024)
                time_start = dtt.now()
                bannergrab_banner = pfgt.figlet_format("Banner Grabber", font="alligator")
                print(cld(bannergrab_banner, "cyan"))
                print(line) 

                print(cld(f"""
    Auth.:\t{author_name}{tab2}Github: {github}
    Date :\t{written_on}{tab2}Instagram: {instagram}
    Lang.:\t{progr_lang}{tab3}Email: {email}
    Vers.:\t{version_num}
                """, "magenta"))

                print(line) 
                print(cld(f" Started at:{tab3}{time_start}", "yellow"))
                print(line + "\n")
                print(cld(f" Target Host:{tab3}{target_host}"))
                print(cld(f" Target Port:{tab3}{target_port}"))
                print(cld(f"\n Result:{tab3}{banner_result}", "green"))
                print("\n" + line)

                time_end = dtt.now()
                time_result = time_end - time_start
                print(cld(f" Job done in:{tab3}{time_result}", "green"))
                print(line)
                
                print(chr(0xa))
                input("Press any key ...")

            except socket.error as sock_err:
                os.system("clear")
                print(cld(f"\nAn error was defined: {sock_err}", "red"))
                return Hunter.banner_grabber()

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
            hash_value = input("Text ~#: ") 
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
                Hunter.banner_grabber()
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
                
            elif hunter_choice == 99:
                ex_banner = pfgt.figlet_format("Exit", font = "digital")
                print(cld(ex_banner, "red"))
                sys.exit(0)
            elif hunter_choice == 0:
                os.system("clear")
                return hunter_main()
            else:
                print(cld("Invalid Input!", "red"))
                input("\nPress any key ...")
                return hunter_main()
            
    hunter_main()
