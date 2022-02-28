########### Hunter Ver.: 1.0.2 ############

from termcolor import colored
import banner
import witch
import time
import sys
import os

# # # # # # # # # # # # # # # # # # # # # #
#                                         #
#   Author  :   Keyj33k                   #
#   Contact :   nomotikag33n@gmail.com    #
#   Twitter :   @keyjeek                  #
#   Github  :   @keyj33k                  #
#   Version :   1.0.2                     #
#                                         #
# # # # # # # # # # # # # # # # # # # # # # 


def banner_hunter(): 
    print(banner.main(banner)) 

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
