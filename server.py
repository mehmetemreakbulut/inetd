import os
import socket


class Server:
    def __init__(self, port: int, accepting_connections: int):
        self.port = port
        self.accepting_connections = accepting_connections

    def start_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("localhost", self.port))
        server_socket.listen(self.accepting_connections)

        print("Server started. Waiting for connections...")

        while True:
            client_socket, addr = server_socket.accept()
            client_id = client_socket.recv(1024).decode()
            print(f"New client connected: #{client_id}")
            pid = os.fork()
            if pid == 0:
                # Child process
                server_socket.close()
                self.handle_client(client_socket, int(client_id))
            else:
                # Parent process
                client_socket.close()

    @staticmethod
    def handle_client(client_socket: socket.socket, client_id: int):
        while True:
            data = client_socket.recv(1024).decode()
            try:
                if int(data) < 0:
                    print(f'Client #{client_id} terminated')
                    break
            except:
                break
            response = str(int(data) ** 2)
            print(f"Message from client #{client_id}: {data}")
            client_socket.send(response.encode())
        client_socket.close()
        os._exit(0)  # Terminate child process, this code helps us to avoid zombie processes


if __name__ == '__main__':
    server = Server(5000, 10)
    server.start_server()

##Run client with command python3 server.py
