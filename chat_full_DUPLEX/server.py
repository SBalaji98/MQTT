"""
this program is a chat application using udp.
this is the server script.

"""
import socket
import threading
from itertools import count
import time


def send_msg(c):
   # for x in count(1):
    #    c.send(str.encode(str(i)))
     #   time.sleep(1)
    x = input()
    client_socket.send(str.encode(f"message:{x}"))


listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 8000
max_con = 999
IP = " 192.168.1.25"
# IP= socket.get()
listen_socket.bind(('', port))
listen_socket.listen(max_con)

print(f"Server started at {IP} on port {port}")
(client_socket, address) = listen_socket.accept()
print("New connection made")

t = threading.Thread(target=send_msg, args=(client_socket,))
t.start()

while True:
    message = client_socket.recv(1024).decode()
    print(f"Message: {message}")

