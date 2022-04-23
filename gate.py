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
import socket
import base64
import time
import sys
import os

magenta = "\033[0;35m"
yellow  = "\033[0;33m"
green   = "\033[0;32m"
cyan    = "\033[0;36m"
red     = "\033[0;31m"

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
               
        """, "cyan"))
        print(magenta + " <"  + green + " by@keyjeek " + magenta + ">"     + cyan    + " | " + green + "Follow the white rabbit ...") 
        print(magenta + " <"  + green + " contact:nomotikag33n@gmail.com " + magenta + ">")           
        print(cyan    + "\n[" + red   + "i" + cyan + "] " + yellow         + "Hunter is a small toolkit to perform information gathering.")   

    def menu():
        print(magenta + "=" * 70)
        print(green   + "\n[" + red + "0"  + green + "]" + cyan+ " Clear Screen")
        print(green   + "["   + red + "1"  + green + "]" + cyan + " Witcher\t\t"         + yellow + " A simple port scanner.")
        print(green   + "["   + red + "2"  + green + "]" + cyan + " MD5Crypt\t\t"        + yellow + " MD5 encryption.")
        print(green   + "["   + red + "3"  + green + "]" + cyan + " IPEye\t\t"           + yellow + " Get informations about an ip address.")
        print(green   + "["   + red + "4"  + green + "]" + cyan + " BannerGrabber\t"     + yellow + " Get service behind a port.")
        print(green   + "["   + red + "5"  + green + "]" + cyan + " B64Crypt\t\t"        + yellow + " En- and Decryption used base64.")
        print(green   + "["   + red + "6"  + green + "]" + cyan + " PhoneStalk\t\t"      + yellow + " Get informations about a phonenumber")
        print(green   + "["   + red + "7"  + green + "]" + cyan + " SubdomainScanner\t"  + yellow + " Get subdomains from any url.")
        print(green   + "["   + red + "8"  + green + "]" + cyan + " Whoami\t\t"          + yellow + " Get infos like current ip address etc.")
        print(green   + "["   + red + "99" + green + "]" + cyan + " Exit\n")
        print(magenta + "="   * 70)

    def whoami_():
        get_hostname  = socket.gethostname()
        get_host_ip   = socket.gethostbyname(get_hostname)
        get_username  = os.getlogin()
        get_path      = os.path.abspath(os.getcwd())

        print(cyan    + "\t\t\tWhoami")
        print(magenta + "< " + green + "=" * 66 + magenta + " >")
        print(yellow  + "\t\tUsername     :"    + green   + f"\t{get_username}")
        print(yellow  + "\t\tHostname     :"    + green   + f"\t{get_hostname}")
        print(yellow  + "\t\tIPAddress    :"    + green   + f"\t{get_host_ip}")
        print(yellow  + "\t\tCurrent Path :"    + green   + f"\t{get_path}")
        input(cyan    + "\nPress any key to continue")
        return Hunter()

    def witcher():  
        os.system("clear")
        witcher_banner          = pfgt.figlet_format("witcher", font="banner3-D")
        print(cld(witcher_banner, "cyan"))
        print(magenta           + "#" * 17 + green, " A python portscanner project ... " + magenta, "#" * 17)
        print("#" * 24          + green, " *writtenby@Keyj33k " + magenta, "#" * 24 + "\n")

        try:
            target_address      = str(input(yellow + "Target (Exit with 'exit' or 'x'): " + red))
            if target_address   == 'exit' or target_address == 'x':
                return Hunter()
        except ValueError:
            print(cld("\nYou need to enter a string!", "red"))
            input(cyan          + "Press any key to continue")

        try:
            target_port         = int(input(yellow + "Max. Port (exit with '0'): " + red))
            if target_port      == 'exit' or target_port == 'x':
                return Hunter()
        except ValueError:
            print(cld("\nYou need to enter a integer!", "red"))
            input(cyan          + "Press any key to continue")

        print(magenta           + "=" * 70)
        scan_start              = dtt.now()
        print(green             + f"Started scanning at:\t\t\t{scan_start}")
        print(magenta           + "=" * 70)
        time_start              = dtt.now()

        try:
            for target in range(1, target_port):
                socket_sock     = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
                final_result    = socket_sock.connect_ex((target_address, target)) 
                socket_sock.settimeout(1) 
                if final_result == 0: 
                    print(green + "Port\t{}\t\t\t\t\t   open".format(target))
                socket_sock.close() 
        except socket.error as socket_error:
            print(cld(socket_error, "red"))
        except KeyboardInterrupt:
            print(cld("\nCtrl+C pressed. Exit.", "red"))
            return Hunter()

        time_stop     = dtt.now() 
        needed_time   = time_stop - time_start
        print(magenta + "=" * 70)
        print(cld(f"Scanner done in {needed_time}!", "green"))
        print(magenta + "=" * 70)
        print(chr(0xa))
        input(cyan    + "Press any key to continue")

    def subdomain_scanner():
        sds_banner                       = pfgt.figlet_format("Sub- domain- Scanner", font = "banner3-D")
        print(yellow                     + sds_banner)
        print(magenta                    + "\n< " + green + "by@keyjeek" + magenta + " >" + cyan + " | " + yellow + "Follow the white rabbit ...")
        print(magenta                    + "< " + green + "contact:nomotikag33n@gmail.com" + magenta + " >") 

        found_subdomain                  = []
        target_address                   = input(yellow + "\nTarget " + magenta + "~#$ " + red)
        if target_address                == 'exit' or target_address == 'x':
            return Hunter()

        with open("subdomains.txt") as FILE:
            read_file                    = FILE.read()
            SUBDOMAIN                    = read_file.splitlines()
            for list_domains in SUBDOMAIN:
                UniformResourceLocator   = f"http://{list_domains}.{target_address}"
                try:
                    import requests
                    requests.get(UniformResourceLocator)
                except requests.ConnectionError:
                    from termcolor import colored
                    print(colored("Not available!", "red"))
                else:
                    print(green         + "Discovered:", UniformResourceLocator)
                    found_subdomain.append(UniformResourceLocator)

        input(cyan       + "Press any key to continue")
        return Hunter()

    def md5encrypt():
        md5_banner    = pfgt.figlet_format("MD5C", font = "banner3-D")
        print(cld(md5_banner, "cyan")) 
        print(magenta + "\n< " + green + "by@keyjeek" + magenta + " >" + cyan + " | " + yellow + "Follow the white rabbit ...")
        print(magenta + "< "   + green + "contact:nomotikag33n@gmail.com" + magenta + " >")       
        print(cyan    + "["    + red   + "i" + cyan + "]" + yellow + " md5crypt is made to encrypt your string to an 128 bit hash value")
        print(cyan    + "["    + red   + "i" + cyan + "]" + yellow + " Type 'exit' to exit md5crypt.")

        def md5():
            print(chr(0xa))
            
            def encrypt(): 
                hash_value          = input(cyan + "Text " + magenta + "~#$ " + yellow)  
                if hash_value       == 'exit' or hash_value == 'x':
                    print(cld("Exit", "red"))
                    return Hunter()    
                
                try:
                    result          = hashlib.md5(hash_value.encode())
                    print(cyan      + "\nResult: " + green, end ="")
                    print(result.hexdigest())
                    input(cyan      + "\nPress any key to continue")
                    return Hunter()         
                except Exception as error:
                    print(cld(f"An error was defined! {error}", "red"))
                    input(cyan      + "Press any key to continue")
                    os.system('clear')
                    return Hunter()
            encrypt()
                    
            def decrypt():
                question_brute      = input(green + "Decrypt/Bruteforce? y/n ~#: " + cyan)
                if question_brute   == 'y' or question_brute == 'Y':
                    print(yellow    + "USE THIS LINK: https://www.md5online.org/md5-decrypt.html ") # This program is using a big database to bruteforce the hash for you
                    input(cyan      + "\nPress any key ...")
                    return Hunter()     
                elif question_brute == 'n' or question_brute == 'N':
                    return Hunter()
            decrypt()
        md5()

    def conditions():
        os.system("clear")
        print(cld("""
 \t\t\tWelcome To Hunter Toolkit!
 < =============================================================================== >
 \n Please note that actions like portscanning etc. can be illegal. 
 If you want to use this tool, follow the conditions:

  - This tool is made for ethical purposes only.
  - I'm not responsible for your actions.
  - With great force follows great responsibility.

 If you accept the conditions type 'y' and 'n' for decline.
 Thank you and have a nice day!

  ~ Keyjeek\n
        """, "red"))

        choice      = input(yellow   + "$ " + cyan)
        if choice   == 'y' or choice == 'Y':
            pass
        elif choice == 'n' or choice == 'N':
            print(cld("Exit", "red"))
            sys.exit(0)
        else:
            os.system("clear")
            print(cld("Invalid Input!", "red"))
            input(cyan + "Press any key to continue")
            os.system("clear")
            return Hunter.conditions()

    def eye_main():
        def ipeye():
            ipe_banner       = pfgt.figlet_format("IPEYE", font = "banner3-D")
            print(cld(ipe_banner, "yellow"))
            print(magenta    + "\n< " + green   + "by@keyjeek"  + magenta + " >"   + cyan    + " | " + yellow + "Follow the white rabbit ...")
            print(magenta    + "< "   + green   + "contact:nomotikag33n@gmail.com" + magenta + " >")       
            print(red        + "["    + cyan    + "i"  + red    + "]"     + yellow + "IPEye is a Tool to find out")
            print(red        + "--"   + magenta + "> " + yellow + "some information about an IP Address.")  
            print(red        + "["    + cyan    + "i"  + red    + "]"     + yellow + "Type 'exit' to exit ipeye.")
            print(chr(0xa))
            ipeye_scanner    = input(cyan + "IPEye Target " + magenta + "~#: " + red)     
            if ipeye_scanner == 'exit' or ipeye_scanner == 'x':
                print(cld("Exiting ...", "red"))
                return Hunter()      
            time_start       = dtt.now()
            print(green      + "\nResults:")

            try:
                response     = requests.post("http://ip-api.com/batch", json=[{"query":ipeye_scanner}]).json()   
            except Exception as error:
                print(cld(f"An error was defined! {error}", "red"))
                input(cyan   + "Press any key to continue")
                os.system('clear')
                return Hunter()
            
            print(magenta    + "=" * 70)      
            for lookup in response:
                for k, j in lookup.items():
                    print(yellow + "\n" + k,j)

            time_stop        = dtt.now()
            time_result      = time_stop - time_start   
            print("\n"       + magenta + "=" * 70)
            print(chr(0xa))
            print(green      + f"Scanner done in {time_result}!")
            input(cyan       + "Press any key to continue")
            return Hunter()
        ipeye()

    def banner_grabber():
        import socket 
        tab2        = "\t" * 2
        tab3        = "\t" * 3
        line        = magenta + "==" * 42
        info_array  = ["@Keyj33k", "1.0.1", "06.04.22", "Python3"]
        links       = ["https://github.com/Keyj33k", "https://www.instagram.com/keyjeek/", "nomotikag33n@gmail.com"]
        author_name = info_array[0]
        version_num = info_array[1]
        written_on  = info_array[2]
        progr_lang  = info_array[3]
        instagram   = links[1]
        github      = links[0]
        email       = links[2]

        while True:
            target_host           = input(red + "\n[" + cyan + "*" + red + "]" + cyan + " Target " + yellow + "(Exit with 'exit' or 'x'): " + red)
            if target_host        == 'exit' or target_host == 'x':
                os.system("clear")
                return Hunter()
            
            target_port           = input(red + "[" + cyan + "*" + red + "]" + cyan + " Port " + yellow + "(Exit with 'exit' or 'x'): " + red)
            if target_port        == "exit" or target_host == 'x':
                os.system("clear")
                return Hunter()

            try:
                socket_sock       = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket_sock.connect_ex((str(target_host), int(target_port)))
                socket_sock.settimeout(1)
                banner_result     = socket_sock.recv(1024).decode()
                time_start        = dtt.now()
                bannergrab_banner = pfgt.figlet_format("Banner Grabber", font="alligator")
                print(cld(bannergrab_banner, "cyan"))
                print(line) 
                print(cyan        + " Auth.:\t" + yellow + f"{author_name}{tab2}" + cyan + "Github: "    + yellow + f"{github}")
                print(cyan        + " Date :\t" + yellow + f"{written_on}{tab2}"  + cyan + "Instagram: " + yellow + f"{instagram}")
                print(cyan        + " Lang.:\t" + yellow + f"{progr_lang}{tab3}"  + cyan + "Email: "     + yellow + f"{email}")
                print(cyan        + " Vers.:\t" + yellow + f"{version_num}")
                print(line) 
                print(cld(f" Started at:{tab3}{time_start}", "yellow"))
                print(line        + "\n")
                print(cld(f" Started at:{tab3}{time_start}", "yellow"))
                print(cld(f" Target Host:{tab3}{target_host}", "yellow"))
                print(cld(f" Target Port:{tab3}{target_port}", "yellow"))
                print(cld(f"\n Result:{tab3}{banner_result}", "green"))
                print(line)
                time_end          = dtt.now()
                time_result       = time_end - time_start
                print(cld(f" Job done in:{tab3}{time_result}", "green"))
                print(line)
                print(chr(0xa))
                input(cyan        + "Press any key to continue")
            except socket.error as sock_err:
                os.system("clear")
                print(cld(f"\nAn error was defined: {sock_err}", "red"))
                return Hunter.banner_grabber()

    def base64encode():   
        b64_banner              = pfgt.figlet_format("B64-  CRYPT", font = "banner3-D")
        print(cld(b64_banner, "green")) 
        print(magenta           + "\n< "  + yellow + "by@keyjeek" + magenta + " >" + cyan + " | " + red + "Follow the white rabbit ...")
        print(magenta           + "< "    + green  + "contact:nomotikag33n@gmail.com" + magenta + " >")       
        print(red               + "["     + cyan   + "i" + red + "] " + yellow + "This Tool helps to encode and decode your text in base64.")  
        print(red               + "["     + cyan   + "i" + red + "] " + yellow + "Type 'exit' to exit Base64crypt.")
        print(red               + "\n\t[" + cyan   + "1" + red + "] " + yellow + "Encoder")
        print(red               + "\t["   + cyan   + "2" + red + "] " + yellow + "Decoder")
        print(red               + "\t["   + cyan   + "x" + red + "] " + yellow + "Exit")

        choice                  = input(cyan + "\nChoice " + magenta + "~#$ " + red)
        if choice               == "1":
            hash_value          = input(cyan + "Text: " + magenta + "~#$ " + red) 
            if hash_value       == 'exit' or hash_value == 'x':
                return Hunter()     

            try:    
                m_bytes         = hash_value.encode('ascii')
                b64_e           = base64.b64encode(m_bytes)
                b64_hash        = b64_e.decode('ascii')
                print(b64_hash)
                input(cyan      + "Press any key to continue")
                return Hunter.base64encode()  
            except Exception as error:
                print(cld(f"An error was defined: {error}"))
                input(cyan      + "Press any key to continue")
                return Hunter.base64encode()
                        
        elif choice             == '2':
            decode_hash         = input(cyan + "Hash: " + magenta + "~#$ " + red) 
            if decode_hash      == 'exit' or decode_hash == 'x':
                print(cld("Exit", "red"))
                return Hunter()   
            
            try:
                b64_d           = decode_hash.encode('ascii')
                m_byte          = base64.b64decode(b64_d)
                result          = m_byte.decode('ascii')
                print(result)
                input(cyan      + "Press any key to continue")
                return Hunter.base64encode()   
            except Exception as error:
                print(cld(f"An error was defined: {error}"))
                input(cyan      + "Press any key to continue")
                return Hunter.base64encode()

    def number_tracker():
        def PhoneStalk():
            pnsk_banner   = pfgt.figlet_format("Phone- Stalk", font = "banner3-D")
            print(cld(pnsk_banner, "magenta")) 
            print(magenta + "\n< " + green + "by@keyjeek" + magenta + " >" + cyan + " | " + yellow + "Follow the white rabbit...")
            print(magenta + "< "   + green + "contact:nomotikag33n@gmail.com" + magenta + " >")       
            print(red     + "["    + cyan  + "i" + red + "]" + yellow + "This Tool helps to find out some informations\n about a phonenumber.") 
            print(red     + "["    + cyan  + "i" + red + "]" + yellow + "Type 'exit' to exit PhoneStalk.")

            while True:
                print(chr(0xa))
                target_phonenumber      = input(yellow + "PhoneStalk Target " + magenta + "~#: " + red) 
                if target_phonenumber   == 'exit' or target_phonenumber == 'x':
                    print(cld("Exit", "red"))
                    return Hunter()    
                elif target_phonenumber == "help" or target_phonenumber == 'h':
                    print(cyan          + "\nHELP; "       + yellow + "Phone-Stalk")
                    print(magenta       + "< "             + green  + "=" * 15 + magenta + " >")
                    print(red           + "'exit'        " + yellow + "Return Menu / Exit PhoneStalk")
                    print(red           + "'clear'       " + yellow + "Clear Screen")             
                    print(chr(0xa))
                    input(cyan          + "Press any key to continue")
                    return Hunter()
                
                print(chr(0xa))
                time_start         = dtt.now()
                print(magenta      + "=" * 55)
                print(yellow       + "Request\t\tResponse\n" + magenta + "=" * 55 + "\n")
                    
                try:
                    valid_check    = pnmb.parse(target_phonenumber)
                    finally_valid  = pnmb.is_valid_number(valid_check)
                    print(green    + f"Validation:\t{finally_valid}")
                    phonenumbers_timezone = pnmb.parse(target_phonenumber, "en")
                    final_timezone = tz.time_zones_for_number(phonenumbers_timezone)
                    print(green    + f"Timezone:\t{final_timezone}")
                    phonenumbers_location = pnmb.parse(target_phonenumber, "CH")
                    final_phonenumbers_location = gc.description_for_number(phonenumbers_location, "en")
                    print(green    + f"Location:\t{final_phonenumbers_location}")
                    phonenumbers_provider = pnmb.parse(target_phonenumber, "RO")
                    final_phonenumbers_provider = cr.name_for_number(phonenumbers_provider, "en")
                    print(green    + f"Provider:\t{final_phonenumbers_provider}")
                    time_stop      = dtt.now()
                    time_result    = time_stop - time_start
                    print("\n"     + magenta + "=" * 55)
                    print(green    + f"Job done in {time_result}") 
                    print(magenta  + "=" * 55)
                except Exception as error:
                    print(cld("[i] An error was defined!", "red"))
                    print(cld(error, "red"))
                    input(red      + "Press any key to continue")
                    return Hunter()
                        
                print(chr(0xa))
                input(cyan         + "Press any key to continue")
                return Hunter()
        PhoneStalk()   

if __name__ == "__main__":
    Hunter.conditions()
    
    def start():
        os.system("clear")
        time_now               = dtt.now()
        username               = os.getlogin()
        print(cld(f"Welcome {username}. Today is the {time_now}", "yellow"))
        time.sleep(1.25)
        start_hunter           = input(yellow + "\nDo you want to start hunter? (y/n) " + cyan)
        if start_hunter        == 'y' or start_hunter == 'Y':
            pass
        elif start_hunter      == 'n' or start_hunter == 'N':
            sys.exit(0)
        else:
            print(cld("Invalid Input!", "red"))
            input(cyan         + "Press any key to continue")
            return start()
    start()

    def hunter_main():
        while True:
            Hunter.banner()
            Hunter.menu()
            global hunter_choice

            try:
                hunter_choice  = int(input(cyan + "\n~#" + magenta + "$ " + red))
            except KeyboardInterrupt:
                print(red      + "\nCtrl-C pressed. Exit")
                return Hunter()
            except ValueError:
                print(cld("You need to enter an integer!", "red"))
                input(cyan     + "Press any key to continue")
                return hunter_main()

            if hunter_choice   == 1:
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
                    input(cyan + "Press any key to continue")
                    return hunter_main()

            elif hunter_choice == 8:
                Hunter.whoami_()
            elif hunter_choice == 99:
                ex_banner      = pfgt.figlet_format("Exit", font = "digital")
                print(cld(ex_banner, "red"))
                sys.exit(0)
            elif hunter_choice == 0:
                os.system("clear")
                return hunter_main()
            else:
                print(cld("Invalid Input!", "red"))
                input(cyan     + "Press any key to continue")
                return hunter_main()
    hunter_main()
    
   
