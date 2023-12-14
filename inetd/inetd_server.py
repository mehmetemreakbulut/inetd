import socket
import subprocess
from threading import Thread

def handle_client(client_socket, port):
    number = int(client_socket.recv(1024).decode())
    if port == 5010:
        print(f"Connection request to square server")
        result = subprocess.run(['python3', 'square_server.py', str(number)], capture_output=True, text=True).stdout
        print(f"(square) Request={number}")
        print(f"(square) Reply={result}")
        print("Terminating..")
    elif port == 5020:
        print(f"Connection request to cube server")
        result = subprocess.run(['python3', 'cube_server.py', str(number)], capture_output=True, text=True).stdout
        print(f"(cube) Request={number}")
        print(f"(cube) Reply={result}")
        print("Terminating..")
    else:
        print(f"Invalid port number {port}")
        client_socket.close()
        return

    client_socket.sendall(result.encode())
    client_socket.close()

def start_server(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', port))
    server.listen(5)
    while True:
        client_socket, client_address = server.accept()
        thread = Thread(target=handle_client, args=(client_socket, port))
        thread.start()

if __name__ == "__main__":
    Thread(target=start_server, args=(5010,)).start()
    Thread(target=start_server, args=(5020,)).start()
