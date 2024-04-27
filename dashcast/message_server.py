import socket
import threading

class Server:
    def __init__(self, host = '127.0.0.1', port = 55555):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()

    def broadcast(self, message, client):
        for c in clients:
            if c != client:
                c.send(message)

    def handle(self, client):
        while True:
            try:
                message = client.recv(1024)
                self.broadcast(message, client)
            except:
                index = clients.index(client)
                clients.remove(client)
                client.close()
                break

    def receive(self):
        while True:
            client, address = self.server.accept()
            clients.append(client)
            thread = threading.Thread(target=self.handle, args=(client,))
            thread.start()

clients = []
server = Server()
server.receive()
