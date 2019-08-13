""""
This program is a chat application using UDP.
This script is the Client script.
1. First we send a message to the server.
2. server recieves the message and then only when server responds to the message, we will be able to send another.
"""
import socket
import threading


def get_msg(c):
    while True:
        data = c.recv(1024)
        if data:
            print(f"From server: {data}")


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = '192.168.1.25'
port = 8000
lock = threading.Lock()
t = threading.Thread(target=get_msg, args=(s, lock,))
s.connect((hostname, port))
t.start()
while True:
    x = input("Enter a message")
    s.send(x.encode())