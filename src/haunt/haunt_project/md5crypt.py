from termcolor import colored
import hashlib
import haunt
import time
import sys
import os

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
                sys.exit()
                ## return haunt.banner_hunter()
                        
            elif hash_val == 'exit':
                print(colored("[i] EXIT", "red"))
                sys.exit()
                ## return haunt.banner_hunter()
                        
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
                sys.exit()
                ## return haunt.banner_hunter()
                        
            elif question_brute == 'exit':
                print(colored("[i] EXIT", "red"))
                sys.exit()
                ## return haunt.banner_hunter()
                        
            elif question_brute == 'clear':
                os.system('clear')
                return decrypt()
                        
            elif question_brute == 'c':
                os.system('clear')
                return decrypt()
                        
            elif question_brute == 'n':
                ## return md5()
                print(colored("[i] Exit", "red"))
                time.sleep(2)
                sys.exit()
                           
                #question_exit = input("[?] EXIT? y/n ")
                              
                #if question_exit == 'y':
                #    print(colored("[i] Exit", "red"))
                #    return haunt.banner_hunter()
                           
                #elif question_exit == 'x':
                #    print(colored("[i] Exit", "red"))
                #    return haunt.banner_hunter()
                              
                #elif question_exit == 'n':
                #    return encrypt()
                              
                #else:
                #    print("[i] INVALID INPUT !")
                #    return haunt.banner_hunter()
        decrypt()
                  
    md5()
               
md5encrypt()