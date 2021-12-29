from datetime import datetime
import requests
import hashlib
import socket
import base64
import socket
import time
import sys
import os
import re


def banner():   
    print("     _   _ _   _ _   _ _____ _____ ____     ")
    print("    | | | | | | | \ | |_   _| ____|  _ \    ")
    print("    | |_| | | | |  \| | | | |  _| | |_) |   ")
    print("    |  _  | |_| | |\  | | | | |___|  _ <    ")
    print("    |_| |_|\___/|_| \_| |_| |_____|_| \_\    ")
    print("")
    print("<by@keyjeek>  |  Follow the white rabbit... ")
    print(" <contact:nomotikag33n@gmail.com>           ")
    print(" [i] Hunter is a small Toolkit to perform Information Gathering   ")
    print(" [i] Type x to exit Hunter.                 ")
banner()

def HUNT3R():
    def menu():
        print("""

            [1] Witcher
            [2] md5encrypt
            [3] eye
            [4] eye_of_sauron
            [5] base64encode
            [x] Exit

    """)
    menu()
    def hunter():
        c=input("[*] Enter your number: ")
        if c=='x':
            print("[i] Exit")
            sys.exit()
        elif c=='1':
            def witcher():
                print("     __        ___ _       _                  ")
                print("     \ \      / (_) |_ ___| |__   ___ _ __    ")
                print("      \ \ /\ / /| | __/ __| '_ \ / _ \ '__|   ")
                print("       \ V  V / | | || (__| | | |  __/ |      ")
                print("        \_/\_/  |_|\__\___|_| |_|\___|_|      ")
                print("                                              ")
                print("   <by@keyjeek>  |  Follow the white rabbit...")
                print("   <contact:nomotikag33n@gmail.com>       ")
                print("   [i] Witcher is a simple port scanner.  ")
                print("   [i] Type x to exit Witcher.")


                ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
                port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
                port_min = 0
                port_max = int(input("\n[*] Enter maximum Port you want to scan: \n[]--> "))
                open_ports = []

                tstart = datetime.now()

                while True:
                    ip_add_entered = input("\n[*] Enter the IP you want to scan: \n[*]--> ")
                    if ip_add_entered == 'x':
                        print("[i] Exit")
                        sys.exit()
    
                    elif ip_add_pattern.search(ip_add_entered):
                        print(f"[i] {ip_add_entered} is valid. Please wait, it'll take some time..\n")        
                        def spinning_cursor():
                            while True:
                                for cursor in '|/-\\':
                                    yield cursor
                        spinner = spinning_cursor()
                        print("[i] loading..")
                        for _ in range(port_max):    ####1000
                            sys.stdout.write(next(spinner))
                            sys.stdout.flush()
                            time.sleep(0.2)
                            sys.stdout.write('\b')           
                        break
                print("\n\n[i] Almost finished..\n")
                print("[r] Open connections:\n ")


                for port in range(port_min, port_max + 1):
                    try:
                        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                            s.settimeout(0.5)
                            s.connect((ip_add_entered, port))
                            open_ports.append(port)
                    except:
                        pass

                for port in open_ports:
                    print(f"[+] TCP/{port}  open")
                tend = datetime.now()
                diff = tend - tstart
                print("\n[!] Scan complete in " + str(diff) + " seconds")

                print("[i] Witcher done.")
                return HUNT3R()
            witcher()
            
        elif c=='2':
            def md5encrypt():
                def banner():
                    print("""   
                       _ ____                                   _
         _ __ ___   __| | ___|  ___ _ __   ___ _ __ _   _ _ __ | |_
        | '_ ` _ \ / _` |___ \ / _ \ '_ \ / __| '__| | | | '_ \| __|
        | | | | | | (_| |___) |  __/ | | | (__| |  | |_| | |_) | |_
        |_| |_| |_|\__,_|____/ \___|_| |_|\___|_|   \__, | .__/ \__|
                                                    |___/|_|
            <by@keyjeek>  |  Follow the white rabbit...
            <contact:nomotikag33n@gmail.com>       
            [i] md5encrypt is made to encrypt your string to an 128 bit hash value
            [i] Type x to exit md5encrypt.
                """)
                banner()

                def md5():
                    def encrypt(): 
                        s=input("\n[*] Enter your text to hash: ")
                        if s=='x':
                            print("[i] Exit")
                            sys.exit()
                        r=hashlib.md5(s.encode())
                        print("[+] Result: ", end ="")
                        print(r.hexdigest())
                    encrypt()

                    def decrypt():
                        a=input("\n[?] Do you want to decrypt/bruteforce the hash? y/n: ")
                        if a=='y':
                            print("[i] Use this Link and enter your hash: https://www.md5online.org/md5-decrypt.html ")                 ##this program is using a big database to bruteforce the hash for you##
                            return encrypt()
                        elif a=='x':
                            print("[i] Exit")
                            sys.exit()
                        elif a=='n':
                            e=input("[?] Do you want to exit? y/n ")
                            if e=='y':
                                print("[i] Exit")
                                sys.exit()
                        elif e=='x':
                            print("[i] Exit")
                            sys.exit()
                        elif e=='n':
                            return encrypt()
                        else:
                            print("[i] Invalid input")
                            return HUNT3R()
                    decrypt()
                md5()
            md5encrypt()

        elif c=='3':
            def eye(): 
                print("      ___ ____  _____                ")
                print("     |_ _|  _ \| ____|   _  ___      ")
                print("      | || |_) |  _|| | | |/ _ \     ")
                print("      | ||  __/| |__| |_| |  __/     ")
                print("     |___|_|   |_____\__, |\___|     ")
                print("                     |___/           ")
                print("\n <by@keyjeek>  |  Follow the white rabbit...")
                print("   <contact:nomotikag33n@gmail.com>       ")
                print("   [i] IPEye is a Tool to find out\n       some information about an IP.  ")
                print("   [i] Type x to exit IPEye.")
                print("")

                q = input('[*] Enter the target IP you want to scan: ')
                if q == 'x':
                    print("[i] Exit")
                    sys.exit()
                response = requests.post("http://ip-api.com/batch", json=[
                    {"query":q}
                ]).json()

                for ip in response:
                    for k,v in ip.items():
                        print(k,v)
                        print("\n")
                        return HUNT3R()
            eye()
        elif c=='4':
            def eye_of_sauron():
                print("      _____                     __   ____  _  _                             ")
                print("     |___ / _   _  ___    ___  / _| / ___|| || |  _   _ _ __ ___  _ __      ")
                print("       |_ \| | | |/ _ \  / _ \| |_  \___ \| || |_| | | | '__/ _ \| '_ \     ")
                print("      ___) | |_| |  __/ | (_) |  _|  ___) |__   _| |_| | | | (_) | | | |    ")
                print("     |____/ \__, |\___|  \___/|_|   |____/   |_|  \__,_|_|  \___/|_| |_|    ")
                print("            |___/                                                           ")
                print("\n        <by@keyjeek>  |  Follow the white rabbit...")
                print("          <contact:nomotikag33n@gmail.com>       ")
                print("          [i] This Tool is made to banner grabbing   ")
                print("")

                def grabber(i, p):
                    s = socket.socket()
                    s.connect((i, int(p)))
                    banner = s.recv(1024)
                    print(banner)

                def main():
                    if len(sys.argv) <= 1:
                        print("[!] Use --help\n")
                    elif sys.argv[1] == "--help":
                        print("[*] Usage: ./eye_of_sauron.py <IP/Domain> <port> ")
                        exit(0)
                    elif len(sys.argv) == 3:
                        print("[!] success!")
                        i = sys.argv[1]
                        p = sys.argv[2]
                        grabber(i, p)
                        exit(0)
                        
                main()
            eye_of_sauron()
        elif c=='5':
            def base64encode():
                def banner():
                    print("""
                     ____                  __   _  _                            _
                    | __ )  __ _ ___  ___ / /_ | || |   ___ _ __   ___ ___   __| | ___
                    |  _ \ / _` / __|/ _ \ '_ \| || |_ / _ \ '_ \ / __/ _ \ / _` |/ _ 
                    | |_) | (_| \__ \  __/ (_) |__   _|  __/ | | | (_| (_) | (_| |  __/
                    |____/ \__,_|___/\___|\___/   |_|  \___|_| |_|\___\___/ \__,_|\___|
                    <by@keyjeek>  |  Follow the white rabbit...
                        <contact:nomotikag33n@gmail.com>       
                    [i] This Tool helps to encode and decode your text in base64.  
                    [i] Type x to exit Base64encode.
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
                    c=input("[*] Enter your choice: ")
                    if c=='1':
                        m=input("\n[*] Enter your text to hash: ")
                        if m=='x':
                            x=input("\n[?] Do you want to exit? y/n ")
                            if x=='y':
                                print("[i] Exit")
                                sys.exit()
                            elif x=='n':
                                return chse()
                            else:
                                print("[i] Invalid Input")
                                return chse()
                        m_bytes=m.encode('ascii')
                        b64_bytes=base64.b64encode(m_bytes)
                        b64_m=b64_bytes.decode('ascii')
                        print(b64_m)
                        return chse()       
                    elif c=='2':
                        b64_m=input("\n[*] Enter your hash to decode: \n")
                        if b64_m=='x':
                            print("[i] Exit")
                            sys.exit()
                        b64_b=b64_m.encode('ascii')
                        m_bytes=base64.b64decode(b64_b)
                        m=m_bytes.decode('ascii')
                        print(m)
                        return chse()
                    elif c=='x':
                        print("[i] Exit")
                        sys.exit()
                    else:
                        print("[i] Invalid input")
                        return HUNT3R()

                chse()
            base64encode()
    hunter()
HUNT3R()
