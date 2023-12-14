import socket


class Client:
    def __init__(self, port: int, client_id: int):
        self.port = port
        self.client_id = client_id

    def run_client(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("localhost", self.port))

        client_socket.send(str(self.client_id).encode())

        while True:
            try:
                number = int(input("Enter a number (negative to exit): "))
            except:
                print("Please enter a number")
                continue
            self.send_number(client_socket, number)
            if number < 0:
                break

        client_socket.close()

    def send_number(self, client_socket: socket.socket, number: int):
        client_socket.send(str(number).encode())
        response = client_socket.recv(1024).decode()
        print(f"Response from server: {response}")


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Usage: python client.py <client_id>")
        sys.exit(1)
    try:
        client_id = int(sys.argv[1])
    except:
        print("Please give a number for client id")
        sys.exit()
    client = Client(5000, client_id)
    client.run_client()

##Run client with command python3 client.py <client_id>