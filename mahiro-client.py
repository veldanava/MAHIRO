import socket
import random
from threading import Thread
from datetime import datetime
from colorama import Fore, init, Back

print("""
\033[1;31m\033[1;37m
███╗   ███╗ █████╗ ██╗  ██╗██╗██████╗  ██████╗ 
████╗ ████║██╔══██╗██║  ██║██║██╔══██╗██╔═══██╗
██╔████╔██║███████║███████║██║██████╔╝██║   ██║
██║╚██╔╝██║██╔══██║██╔══██║██║██╔══██╗██║   ██║
██║ ╚═╝ ██║██║  ██║██║  ██║██║██║  ██║╚██████╔╝
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝ ╚═════╝ 
                                               
\033[1;31mCLIENT SIDE                   coded by kiana\033[1;31m\033[1;37m""")
print("")

# init colors
init()

# set colors
colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX, 
    Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX, 
    Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX, 
    Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW
]

# choose random color for client
client_color = random.choice(colors)

# get server connection
# for ip u can use, example 127.0.0.1 or ur server/private address
SERVER_HOST = input("input ur address: " ) # server address
SERVER_PORT = 5500 # server port
separator_token = "<SEP>" # separate client name and message

# init socket from server
s = socket.socket()
print(f"[!] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
# connect to server
s.connect((SERVER_HOST, SERVER_PORT))
print("[!] Connected.")
# prompt client username
name = input("input ur name: ")

def listen_message():
    while True:
        message = s.recv(1024).decode()
        print("\n" + message)

# make thread to listen message from client & print
t = Thread(target=listen_message)
# daemon thread
t.daemon = True
# start the thread
t.start()

while True:
    # input message we want to send to the server
    to_send =  input("type: ")
    # exit program
    if to_send.lower() == 'q':
        break
    # add the datetime and name
    date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
    to_send = f"{client_color}[{date_now}] {name} > {to_send}{Fore.RESET}"
    # send
    s.send(to_send.encode())

# close socket
s.close()