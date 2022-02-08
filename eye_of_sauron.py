import socket
import sys
import os

os.system('clear')
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

    def grabber(k, j):
        sock = socket.socket()
        sock.connect((k, int(j)))
        banner = sock.recv(1024)
        print(banner)
        
    def main():
        if len(sys.argv) <= 1:
            print("[!] Use --help\n")
        elif sys.argv[1] == "--help":
            print("[*] Usage: ./eye_of_sauron.py <IP/Domain> <port> ")
            exit(0)
        elif len(sys.argv) == 3:
            print("[!] success!")
            k = sys.argv[1]
            j = sys.argv[2]
            grabber(k, j)
            exit(0)                       
    main()
eye_of_sauron()
