import socket
import sys
import os

os.system('clear')
def eye_of_sauron():
    print("""
    

      ▓███▒   ██   █    █ █████   ▓██▓  ██   █        ███████▒   ▒█ ██████
     █▓  ░█   ██   █    █ █   ▓█ ▒█  █▒ ██░  █        █     ░█   █░ █
     █       ▒██▒  █    █ █    █ █░  ░█ █▒▓  █        █      ▒█ █▒  █
     █▓░     ▓▒▒▓  █    █ █   ▒█ █    █ █ █  █        █       █▓█   █
      ▓██▓   █░░█  █    █ █████  █    █ █ ▓▓ █        ██████  ▒█▒   ██████
         ▓█  █  █  █    █ █  ░█▒ █    █ █  █ █        █        █    █
          █ ▒████▒ █    █ █   ░█ █░  ░█ █  ▓▒█        █        █    █
     █░  ▓█ ▓▒  ▒▓ █▒  ▒█ █    █ ▒█  █▒ █  ░██        █        █    █
     ▒████░ █░  ░█  ████  █    ▒  ▓██▓  █   ██        ██████   █    ██████


                                              ██████
            <by@keyjeek>  |  Follow the white rabbit...
              <contact:nomotikag33n@gmail.com>      
              [i] This Tool is made to banner grabbing  
    """)

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
