from termcolor import colored
from datetime import datetime
import socket
import haunt
import time
import sys
import re
import os


def witcher_hunter():
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
            return haunt.banner_hunter()
                     
        elif target_ip == 'exit':
            print(colored("[*] EXIT", "red"))
            return haunt.banner_hunter()
                     
        elif target_ip == 'clear':
            os.system('clear')
            return witcher_hunter()
                     
        elif target_ip == 'c':
            os.system('clear')
            return witcher_hunter()
                     
        elif ip_compile.search(target_ip):
            print(f"[i] {target_ip} is valid. Please wait, it'll take some time..")
          
            def spinning_cursor():
                while True:
                    for cursor in '|/-\\':
                        yield cursor
                              
            spinner = spinning_cursor()
            print("[i] LOADING ...")
                        
            for _ in range(port_max):   
                sys.stdout.write(next(spinner))
                sys.stdout.flush()
                time.sleep(0.2)
                sys.stdout.write('\b')           
            break
                        
        print("[i] Listing open connections ...")
               
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
            return haunt.banner_hunter()
                  
        for port in open_ports:
            print(f"[+] TCP/{port}  OPEN")
                     
        tend = datetime.now()
        diff = tend - tstart
                  
        print(chr(0xa))
        print("[i] SCAN COMPLETE IN " + str(diff) + " SECONDS ...")
        time.sleep(2)
               
        print("[i] WITCHER DONE !")
        print(chr(0xa))
        return haunt.banner_hunter()
            
witcher_hunter() 