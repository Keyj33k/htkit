from termcolor import colored
import base64
import haunt
import os

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
                    return haunt.banner_hunter()
                           
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
                    return haunt.banner_hunter()
                              
                elif b64_hash_val == 'exit':
                    print(colored("[i] EXIT", "red"))
                    return haunt.banner_hunter()
                           
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
            return haunt.banner_hunter()
                     
        elif choice == 'exit':
            print(colored("[i] EXIT", "red"))
            return haunt.banner_hunter()
                     
        else:
            print(colored("[i] INVALID INPUT !", "red"))
            return haunt.banner_hunter()
                     
    chse()
               
base64encode()