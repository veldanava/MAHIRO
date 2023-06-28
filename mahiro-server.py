import socket
from threading import Thread

print("""
\033[1;31m\033[1;37m
███╗   ███╗ █████╗ ██╗  ██╗██╗██████╗  ██████╗ 
████╗ ████║██╔══██╗██║  ██║██║██╔══██╗██╔═══██╗
██╔████╔██║███████║███████║██║██████╔╝██║   ██║
██║╚██╔╝██║██╔══██║██╔══██║██║██╔══██╗██║   ██║
██║ ╚═╝ ██║██║  ██║██║  ██║██║██║  ██║╚██████╔╝
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝ ╚═════╝ 
                                               
\033[1;31mSERVER SIDE                   coded by  kiana\033[1;31m\033[1;37m""")
print("")

# server address
SERVER_HOST = input("input ur address: " ) # u can change this with ur ip private or server
SERVER_PORT = 5500 # i'll use this port
separator_token = "<sep>" # to separate client name and message

# initialize
client_sockets = set()
# tcp socket
s = socket.socket()
# make reusable port
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# bind socket
s.bind((SERVER_HOST, SERVER_PORT))
# listen
s.listen(5)
print(f"[!] Listening as {SERVER_HOST}:{SERVER_PORT}")

# lsiten the client
def listen_client(cs):
  while True:
    try:
      # keep listening a message from socket
      msg = cs.recv(1024).decode()
    except Exception as e:
      # if client no longer connected, remove it from server
      print(f"[!] Error: {e}")
      client_sockets.remove(cs)
    else:
      # replace <sep> if server get an message
      msg = msg.replace(separator_token, ": ")
    # iterate
    for client_socket in client_sockets:
      # send message
      client_socket.send(msg.encode())
      
while True:
  # keep listening for new connections
  client_socket, client_address = s.accept()
  print(f"[!] {client_address} connected")
  # add new connection
  client_sockets.add(client_socket)
  # start new thread to listen client messages
  t = Thread(target=listen_client, args=(client_socket,))
  t.daemon = True
  # start thread
  t.start()
  
# close socket (client)
for cs in client_sockets:
  cs.close()
# close socket (server)
s.close()