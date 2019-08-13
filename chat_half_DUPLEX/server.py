"""
this program is a chat application using udp.
this is the server script.

"""
import socket
import threading


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

while True:

    message = client_socket.recv(1024).decode()
    print(f"Message: {message}")
    mesg = input('enter message')
    client_socket.send(str.encode(f"message:{mesg}"))