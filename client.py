import socket
import sys

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: {} <server IP address> <port>".format(sys.argv[0]))
        sys.exit(1)

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((sys.argv[1], int(sys.argv[2])))
    message = client.recv(1024)
    print(message)
