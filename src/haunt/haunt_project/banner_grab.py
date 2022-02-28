from termcolor import colored
import socket
import haunt
import time
import sys
import os

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
            ## return haunt.banner_hunter()
            sys.exit()
                     
        elif target_ip == 'exit':
            print(colored("[*] Exiting ...", "red"))
            time.sleep(1)
            ## return haunt.banner_hunter()
            sys.exit()
                     
        elif target_ip == 'c':
            os.system('clear')
            ## return banner_grabber_part()
            sys.exit()
                     
        elif target_ip == 'clear':
            os.system('clear')
            return banner_grabber_part()

        target_port = input("[*] TARGET_PORT: ")

        try:
            ## grab banner with tcp socket 
            socket_sock = socket.socket()
            socket_sock.connect((target_ip, int(target_port)))
            print(socket_sock.recv(1024))
            time.sleep(1)
            ## return haunt.banner_hunter()
                     
        except Exception:
            print(colored("[i] Can't connect to target. An error was defined !", "red"))
            time.sleep(1)
                        
            retry_option = input("[*] Retry? (y/N) ")
                        
            if retry_option == 'y':
                return banner_grabber_part()
                           
            elif retry_option == 'n':
                print(colored("[*] Exiting ...", "red"))
                time.sleep(1)
                ## return haunt.banner_hunter()
                sys.exit()
                           
            else:
                print(colored("[i] Invalid input !"))
                time.sleep(1)
                return banner_grabber_part()

    banner_grab()

banner_grabber_part()
