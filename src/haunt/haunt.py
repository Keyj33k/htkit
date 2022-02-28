from termcolor import colored
#import ipeye
import banner
import witch
import time
import sys
import os

def banner_hunter(): 

#    print(colored("""
#    █    █                 █
#    █    █                 █
#    █    █ █   █  █▒██▒  █████   ███    █▒██▒
#    █    █ █   █  █▓ ▒█    █    ▓▓ ▒█   ██  █
#    ██████ █   █  █   █    █    █   █   █
#    █    █ █   █  █   █    █    █████   █
#    █    █ █   █  █   █    █    █       █
#    █    █ █▒ ▓█  █   █    █░   ▓▓  █   █
#    █    █ ▒██▒█  █   █    ▒██   ███▒   █
    
#    <by@keyjeek>  |  Follow the white rabbit... 
#    <contact:nomotikag33n@gmail.com>           
#    [i] Hunter is a small toolkit to perform information gathering   
#    [i] Type x to exit Hunter.              

#    [1] WITCHER
#    [2] MD5CRYPT
#    [3] IPEYE
#    [4] BANNER_GRABBER
#    [5] B64CRYPT
#    [6] WHEREAREYOU
#    [98] EXIT
#    [99] CLEAR
#    """, "yellow"))

    print(banner.main()) ## banner

    hunter_choice = int(input("[*] Number: "))

    if hunter_choice == 11:
        print(witch)
        return banner_hunter()

    elif hunter_choice == 2:
        from md5crypt import md5encrypt
        print(md5encrypt)
        return banner_hunter()
    
    elif hunter_choice == 3:
        import ipeye
        print(ipeye.eye_main())
        return banner_hunter()

    elif hunter_choice == 4:
        import banner_grab
        print(banner_grab.banner_grabber_part())
        return banner_hunter()

    elif hunter_choice == 5:
        from b64crypt import base64encode
        print(base64encode)
        return banner_hunter()
    
    elif hunter_choice == 6:
        import wherareyou
        print(wherareyou.number_tracker())
        #return banner_hunter()
    
    elif hunter_choice == 98:
        os.system('clear')
        return banner_hunter()
    
    elif hunter_choice == 99:
        print(colored("[*] Exiting ...", "red"))
        time.sleep(2)
        sys.exit()
        
banner_hunter()
