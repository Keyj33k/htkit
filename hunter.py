########### Hunter Ver.: 1.0.2 ############

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

# # # # # # # # # # # # # # # # # # # # # #
#                                         #
#   Author  :   Keyj33k                   #
#   Contact :   nomotikag33n@gmail.com    #
#   Twitter :   @keyjeek                  #
#   Github  :   @keyj33k                  #
#   Version :   1.0.1                     #
#                                         #
# # # # # # # # # # # # # # # # # # # # # # 

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
banner()

def HUNT3R():
   
    def menu():
         
        print(colored("""
[1] WITCHER
[2] MD5ENCRYPT
[3] IPEYE
[4] BANNER_GRABBER
[5] B64CRYPT
[6] WIFI-STALKER    >>     [i] Need monitor mode !
[7] WHEREAREYOU
[x] EXIT
[c] CLEAR
        """, "yellow"))
      
    menu()
    
    def hunter():
      
        choice = input("[*] NUMBER: ")
         
        if choice == 'x':
            print(colored("[i] EXIT", "red"))
            sys.exit()
            
        elif choice == 'exit':
            print(colored("[*] EXIT", "red"))
            sys.exit()
            
        elif choice == 'c':
            os.system('clear')
            return HUNT3R()
         
        elif choice == 'clear':
            os.system('clear')
            return HUNT3R()

        elif choice == '1':
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
[i] Type x in <target ip> part to exit Witcher. 
                """)

                ip_compile = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
                port_min = 0
                print(chr(0xa))
                port_max = int(input("[*] ENTER MAX. PORT: \n[*]--> ")) 
                open_ports = []
                tstart = datetime.now()
                
                while True:
                     
                    target_ip = input("[*] TARGET IP: \n[*]--> ")
                  
                    if target_ip == 'x':
                        print(colored("[i] EXIT", "red"))
                        return HUNT3R()
                     
                    elif target_ip == 'exit':
                        print(colored("[*] EXIT", "red"))
                        return HUNT3R()
                     
                    elif target_ip == 'clear':
                        os.system('clear')
                        return witcher()
                     
                    elif target_ip == 'c':
                        os.system('clear')
                        return witcher()
                     
                    elif ip_compile.search(target_ip):
                        print(f"[i] {target_ip} is valid. Please wait, it'll take some time..")

                    ## Print a progress bar
                    for i in tqdm (range(100), desc="Loading ..."): 
                        try:
                            for port in range(port_min, port_max + 1):
                                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: ## sock_DGRAM/UPD
                                    s.settimeout(0.5) 
                                    s.connect((target_ip, port))
                                    open_ports.append(port)
                              
                        except Exception:
                            print(colored("[*] Can't connect to target!", "red"))
                            time.sleep(3)
                            input("Press any key ...")
                            return HUNT3R()
                  
                        for port in open_ports:
                            print(f"[+] TCP/{port}  OPEN")
                     
                        tend = datetime.now()
                        diff = tend - tstart
                    
                        print(chr(0xa))
                        print("[i] SCAN COMPLETE IN " + str(diff) + " SECONDS ...")
                        time.sleep(2)
                
                        print("[i] WITCHER DONE !")
                        print(chr(0xa))
                        return HUNT3R()
            
            witcher() 

        elif choice == '2':
         
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
                            return HUNT3R()
                        
                        elif hash_val == 'exit':
                            print(colored("[i] EXIT", "red"))
                            return HUNT3R()
                        
                        elif hash_val == 'clear':
                            os.system('clear')
                            return md5encrypt()
                        
                        elif hash_val == 'c':
                            os.system('clear')
                            return md5encrypt()
                        
                        result = hashlib.md5(hash_val.encode())
                        print("[+] RESULT: ", end ="")
                        print(result.hexdigest())
                        
                    encrypt()
                  
                    def decrypt():
                        
                        question_brute = input("[?] DECRYPT/BRUTEFORCE THE HASH? y/n: ")
                        
                        if question_brute == 'y':
                            print("[i] USE THIS LINK: https://www.md5online.org/md5-decrypt.html ")## This program is using a big database to bruteforce the hash for you
                            return encrypt()
                        
                        elif question_brute == 'x':
                            print(colored("[i] EXIT", "red"))
                            return HUNT3R()
                        
                        elif question_brute == 'exit':
                            print(colored("[i] EXIT", "red"))
                            return HUNT3R()
                        
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
                                return HUNT3R()
                           
                            elif question_exit == 'x':
                                print(colored("[i] Exit", "red"))
                                return HUNT3R()
                              
                            elif question_exit == 'n':
                                return encrypt()
                              
                            else:
                                print("[i] INVALID INPUT !")
                                return HUNT3R()
                    decrypt()
                  
                md5()
               
            md5encrypt()

        elif choice == '3':
         
            def eye_main():
               
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
                
                def eye(): 
                     
                    print(chr(0xa))
                    scanner = input('[*] IP: ')
                     
                    if scanner == 'x':
                        print(colored("[i] EXIT", "red"))
                        return HUNT3R()
                     
                    elif scanner == 'exit':
                        print(colored("[i] EXIT", "red"))
                        return HUNT3R()
                     
                    elif scanner == 'clear':
                        os.system('clear')
                        return eye_main()
                     
                    elif scanner == 'c':
                        os.system('clear')
                        return eye_main()
                     
                    try:
                        response = requests.post("http://ip-api.com/batch", json=[{"query":scanner}]).json()
                        
                    except Exception:
                        print(colored("CAN'T CONNECT. AN ERROR WAS DEFINED !", "red"))
                        input("Press any key ...")
                        os.system('clear')
                        return HUNT3R()
                     
                    os.system('clear')
                  
                    for ip in response:
                        for k, j in ip.items():
                            print(k,j)
                              
                    print(chr(0xa))
                    print("[i] SCANNER DONE !")
                    print(chr(0xa))
                    return HUNT3R()
               
                eye()
               
            eye_main()
            
        elif choice == '4':
         
            os.system('clear')
            
            def banner_grabber_part():
         
                print(chr(0xa))

                print("""
█████░   ██   ██   █ ██   █ ██████ █████          ▒███▒ █████    ██   █████░
█   ▒█   ██   ██░  █ ██░  █ █      █   ▓█        ░█▒ ░█ █   ▓█   ██   █   ▒█
█    █  ▒██▒  █▒▓  █ █▒▓  █ █      █    █        █▒     █    █  ▒██▒  █    █
█   ▒█  ▓▒▒▓  █ █  █ █ █  █ █      █   ▒█        █      █   ▒█  ▓▒▒▓  █   ▒█
█████░  █░░█  █ ▓▓ █ █ ▓▓ █ ██████ █████         █   ██ █████   █░░█  █████░
█   ▒█  █  █  █  █ █ █  █ █ █      █  ░█▒        █    █ █  ░█▒  █  █  █   ▒█
█    █ ▒████▒ █  ▓▒█ █  ▓▒█ █      █   ░█        █▒   █ █   ░█ ▒████▒ █    █
█   ▒█ ▓▒  ▒▓ █  ░██ █  ░██ █      █    █        ▒█░ ░█ █    █ ▓▒  ▒▓ █   ▒█
█████░ █░  ░█ █   ██ █   ██ ██████ █    ▒         ▒███▒ █    ▒ █░  ░█ █████░
                                        ██████
<   coded by@keyj33k    >
[i] Type x to exit banner_grabber
                """)

                def banner_grab():
                     
                    print(chr(0xa))

                    target_ip = input("[*] TARGET_IP: ")
                     
                    if target_ip == 'x':
                        print(colored("[*] Exiting ...", "red"))
                        time.sleep(1)
                        return HUNT3R()
                     
                    elif target_ip == 'exit':
                        print(colored("[*] Exiting ...", "red"))
                        time.sleep(1)
                        return HUNT3R()
                     
                    elif target_ip == 'c':
                        os.system('clear')
                        return banner_grabber_part()
                     
                    elif target_ip == 'clear':
                        os.system('clear')
                        return banner_grabber_part()

                    target_port = input("[*] TARGET_PORT: ")

                    try:
                        socket_sock = socket.socket()
                        socket_sock.connect((target_ip, int(target_port)))
                        print(socket_sock.recv(1024))
                        time.sleep(1)
                        return HUNT3R()
                     
                    except Exception:
                        print(colored("[i] Can't connect to target. An error was defined !", "red"))
                        time.sleep(1)
                        
                        retry_option = input("[*] Retry? (y/N) ")
                        
                        if retry_option == 'y':
                            return banner_grabber_part()
                           
                        elif retry_option == 'n':
                            print(colored("[*] Exiting ...", "red"))
                            time.sleep(1)
                            return HUNT3R()
                           
                        else:
                            print(colored("[i] Invalid input !"))
                            time.sleep(1)
                            return banner_grabber_part()

                banner_grab()

            banner_grabber_part()

        elif choice == '5':
         
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
                                return HUNT3R()
                           
                            elif exit_choice == 'n':
                                return chse()
                           
                            else:
                                print(colored("[i] INVALID INPUT!", "red"))
                                return chse()
                              
                        elif hash_value == 'clear':
                            os.system('clear')
                            return base64encode()
                        
                        elif hash_value == 'c':
                            os.system('clear')
                            return base64encode()
                        
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
                                return HUNT3R()
                              
                            elif b64_hash_val == 'exit':
                                print(colored("[i] EXIT", "red"))
                                return HUNT3R()
                           
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
                        
                    elif choice == 'c':
                        os.system('clear')
                        return chse()
                     
                    elif choice == 'clear':
                        os.system('clear')
                        return chse()
                     
                    elif choice == 'x':
                        print(colored("[i] EXIT", "red"))
                        return HUNT3R()
                     
                    elif choice == 'exit':
                        print(colored("[i] EXIT", "red"))
                        return HUNT3R()
                     
                    else:
                        print(colored("[i] INVALID INPUT !", "red"))
                        return HUNT3R()
                     
                chse()
               
            base64encode()

        elif choice == '6':
         
            os.system('clear')
            
            def wifiStalker():
               
                networks = pandas.DataFrame(columns=["BSSID", "SSID", "dBm_Signal", "Channel", "Crypto"])
                networks.set_index("BSSID", inplace=True)
               
                def callback(packet):
                     
                    if  packet.haslayer(Dot11Beacon):
                        bssid = packet[Dot11].addr2
                        ssid = packet[Dot11Elt].info.decode()
                        
                        try:
                            dbm_signal = packet.dBm_AntSignal
                              
                        except:
                            dbm_signal = "N/A"
                              
                        stats = packet[Dot11Beacon].network_stats()
                        channel = stats.get("channel")
                        crypto = stats.get("crypto")
                        networks.loc[bssid] = (ssid, dbm_signal, channel, crypto)
                        
                def print_all():
                  
                    while True:
                        os.system("clear")
                        print(networks)
                        time.sleep(0.5)        
                        
                if __name__ == "__main__":
                    interface = "wlan0mon"
                    printer = Thread(target=print_all)
                    printer.daemon = True
                    printer.start()
                    sniff(prn=callback, iface=interface)
                     
                def change_channel():
                  
                    ch = 1
                     
                    while True:
                        os.system(f"iwconfig {interface} channel {ch}")
                        ch = ch%14+1
                        time.sleep(0.5)
                        channel_change = Thread(target=change_channel)
                        channel_changer.daemon = True
                        channel_changer.start()
                        
            wifiStalker()
        
        elif choice == '7':
            
            def number_tracker():
                try:
                    banner_whereareyou.set_banner_whereareryou()
                except:
                    print(colored("Banner not available !", "red"))

                while True:
                    print(chr(0xa))
                    number = input('[*] PHONENUMBER: ')
                    
                    if number == '/x':
                        print(colored("[i] EXIT", "red"))
                        return HUNT3R()
                    
                    elif number == '/exit':
                        print(colored("[i] EXIT", "red"))
                        return HUNT3R()
                    
                    elif number == '/c':
                        os.system('clear')
                        return HUNT3R()
                    
                    elif number == '/clear':
                        os.system('clear')
                        return HUNT3R()

                    elif number == '/help':
                        banner_whereareyou.set_help_banner()
                        return HUNT3R()
            
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
                        return HUNT3R()
                    
                    print(chr(0xa))
                    input('Press any key ...')
                    return number_tracker()
                
            number_tracker()
        
        else:
            print(colored("[i] INVALID INPUT !", "red"))
            return HUNT3R()

    hunter()
    
HUNT3R()
