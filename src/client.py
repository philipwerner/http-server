# -*- coding: utf-8 -*-
"""Will do something. Will updated when it is known what."""
import socket


def client(message):
    """Will do a thing."""
    client = socket.socket(*socket.getaddrinfo("127.0.0.1", 3455)[1][:3])
    client.connect(("127.0.0.1", 3455))
    message = message + "@"
    client.sendall(message.decode("utf-8").encode("utf-8"))
    msg = ''
    timer = True
    while timer:
        port = client.recv(8)
        msg += port.decode("utf-8").encode("utf-8")
        if "@" in msg:
            timer = False
    client.close()
    return msg.replace("@", "")
