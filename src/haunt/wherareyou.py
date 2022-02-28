from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier
from termcolor import colored
import phonenumbers
import haunt
import os

def number_tracker():
               
    print("""
█     █ █    █ ██████ █████  ██████ █████  █    █
█░ █ ░█ █    █ █      █   ▓█ █      █   ▓█ █    █
█░▒█▒░█ █    █ █      █    █ █      █    █ █    █
▓▒███▒█ █    █ █      █   ▒█ █      █   ▒█ █    █
▒▒█▒█▒▓ ██████ ██████ █████  ██████ █████  █    █
▒██ ██▓ █    █ █      █  ░█▒ █      █  ░█▒ █    █
▒█▓ ▓█▒ █    █ █      █   ░█ █      █   ░█ █    █
░█▒ ▒█▒ █    █ █      █    █ █      █    █ █▒  ▒█
 █   █▒ █    █ ██████ █    ▒ ██████ █    ▒  ████
 
<by@keyjeek>  |  Follow the white rabbit...
<contact:nomotikag33n@gmail.com>    
[i] Phonenumber tracking tool
[i] Type 'c' or 'clear' to clear the screen
[i] Type 'x' or 'exit' to exit whereareyou
                """)

    while True:
                  
        def check_number():
            print(chr(0xa))                     
            number = input('[*] PHONENUMBER: ')
                        
            if number == 'x':
                print(colored("[i] EXIT", "red"))
                return haunt.banner_hunter()
                        
            elif number == 'exit':
                print(colored("[i] EXIT", "red"))
                return haunt.banner_hunter()
                        
            elif number == 'clear':
                os.system('clear')
                return number_tracker()
                        
            elif number == 'c':
                os.system('clear')
                return number_tracker()
                        
            ## check if valid
            print(chr(0xa))
            valid_check = phonenumbers.parse(number)
            is_valid = phonenumbers.is_valid_number(valid_check)
            print("VALID: ")
            print(is_valid)
                        
            ## get timezone
            timezone_number = phonenumbers.parse(number, "en")
            print(timezone.time_zones_for_number(timezone_number))
                        
            ## get location
            target_number = phonenumbers.parse(number, "CH")
            print(geocoder.description_for_number(target_number, "en"))
                        
            ## get provider information
            provider_info = phonenumbers.parse(number, "RO")
            print(carrier.name_for_number(provider_info, "en"))
            print(chr(0xa))
            input('Press any key..')
            return check_number()
                     
        check_number()
                  
number_tracker()