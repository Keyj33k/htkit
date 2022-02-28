from termcolor import colored
import requests
import haunt
import time
import sys
import os

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
            ## return haunt.banner_hunter()
            sys.exit()
                     
        elif scanner == 'exit':
            print(colored("[i] EXIT", "red"))
            ## return haunt.banner_hunter()
            sys.exit()
                     
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
            ## return haunt.banner_hunter()
            print(colored("[*] Exit", "red"))
            time.sleep(2)
            sys.exit()
                     
        os.system('clear')
                  
        for ip in response:
            for k, j in ip.items():
                print(k,j)
                              
            print(chr(0xa))
        print("[i] SCANNER DONE !")
        print(colored("[*] Exit", "red"))
        time.sleep(2)
        print(chr(0xa))
        sys.exit()
        ## return haunt.banner_hunter()
               
    eye()
               
eye_main()