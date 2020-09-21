from threading import Thread

import socket

client_socket = socket.socket()

client_socket.connect(("localhost", 2021))

name = input("Enter client's name :")

client_socket.sendall(name.encode())


def send():
    while True:
        data = input()
        client_socket.sendall(data.encode())


def receive():
    while True:
        data = client_socket.recv(1000)
        print(data.decode())


client_receive = Thread(target=receive)
client_receive.start()
send()