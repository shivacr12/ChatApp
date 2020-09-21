from threading import Thread

import socket

server_socket = socket.socket()

server_socket.bind(('', 2021))
print("server bound")

server_socket.listen()
print("server listening")

clients = {}


def func(addr, conn, name):
    while True:
        message = conn.recv(1000)
        message = name + ":" + message.decode()
        for client in clients:
            if client != name:
                clients[client].sendall(message.encode())


while True:
    conn, addr = server_socket.accept()
    print("Got a connection from addr :", addr)
    name = conn.recv(1000)
    print("name of the client is :", name.decode())
    clients[name.decode()] = conn
    t = Thread(target=func, args=(addr, conn, name.decode()))
    t.start()


