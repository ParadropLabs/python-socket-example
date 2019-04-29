import os
import socket

PORT = int(os.environ.get("PORT", "8081"))

if __name__ == "__main__":
    server = socket.socket()
    server.bind(("", PORT))
    server.listen(5)
    print("Server listening on port: {}".format(PORT))

    counter = 0
    while True:
        client, addr = server.accept()
        print("Accepted connection from: {}".format(addr))

        counter += 1
        client.send("Hello. You are connection number {}.".format(counter))
        client.close()
