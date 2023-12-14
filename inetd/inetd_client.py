import os
import socket
import sys


def run_inetd_client(port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", port))

    while True:
        try:
            number = int(input("Enter a number: "))
        except:
            print("Please enter a number")
            continue
        client_socket.send(str(number).encode())
        response = client_socket.recv(1024).decode()

        service = "square" if port == 5010 else "cube"
        print(f"Response from {service} server: {response}")
        break

    client_socket.close()
    sys.exit()

if __name__ == '__main__':
    try:
        port = int(sys.argv[1])
    except:
        print("Please enter a number")
        sys.exit()
    run_inetd_client(port)
