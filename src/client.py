# -*- coding: utf-8 -*-
"""Create a client socket to send messages to the server."""
import socket
import sys


def client(message):
    """Open a client to send messages."""
    client = socket.socket(*socket.getaddrinfo("127.0.0.1", 5000)[1][:3])
    client.connect(("127.0.0.1", 5000))
    message = message + "@@@"
    if sys.version_info.major == 3:
        client.sendall(message.encode("utf-8"))
    else:
        client.sendall(message)
    msg = b''
    timer = True
    try:
        while timer:
            part = client.recv(15)
            msg += part
            if b"@@@" in msg:
                timer = False
        client.close()
        return msg.decode("utf-8").replace("@@@", "")
    except KeyboardInterrupt:
        client.close()
        print("Bye bye client connection.")

if __name__ is "__main__":
    msg = sys.argv[1]
    print(client(msg))
