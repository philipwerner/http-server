# -*- coding: utf-8 -*-
"""."""
import socket


def server():
    """Will do stuff."""
    server = socket.socket(socket.AF_INET,
                           socket.SOCK_STREAM, socket.IPPROTO_TCP)
    server.bind(('127.0.0.1', 3455))
    server.listen(1)
    while True:
        conn, addr = server.accept()
        msg = ''
        timer = True
        while timer:
            port = conn.recv(8)
            msg += port.decode("utf-8").encode("utf-8")
            if "@" in msg:
                timer = False
        conn.sendall(msg.decode("utf-8").encode("utf-8"))
        conn.close()
    if KeyboardInterrupt:
        server.close()
