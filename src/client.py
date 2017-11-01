# -*- coding: utf-8 -*-
"""Create a client socket to send messages to the server."""
import socket
import sys


def client(message):
    """Open a client to send messages."""
    client = socket.socket(*socket.getaddrinfo("127.0.0.1", 5001)[1][:3])
    client.connect(("127.0.0.1", 5001))
    request_header = "GET /http-server/src/server.py HTTP/1.1\r\n\
    HOST: 127.0.0.1:5001"
    message = request_header + message + "@@@"
    if sys.version_info.major == 3:
        client.sendall(message.encode("utf-8"))
    else:
        client.sendall(message)
    msg = b''
    message_incomplete = True
    while message_incomplete:
        part = client.recv(15)
        msg += part
        if b"@@@" in msg:
            message_incomplete = False
    client.close()
    return msg.decode("utf-8").replace("@@@", "")

if __name__ == "__main__":  # pragma: no cover
    msg = sys.argv[1]
    print(client(msg))
