import json
import socket
def client_program():
    host = socket.gethostname()
    port = 6666
    client_socket = socket.socket()
    client_socket.connect((host, port))
    while True:
        message = input(" -> ")
        client_socket.send(message.encode())
        data = client_socket.recv(102400).decode()
        print(data)
if __name__ == '__main__':
    client_program()
