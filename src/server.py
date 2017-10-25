# -*- coding: utf-8 -*-
"""Open a server and listen for messages from the client."""
import socket
import sys
import email.utils


def server():
    """Open a server to echo back a message."""
    server = socket.socket(socket.AF_INET,
                           socket.SOCK_STREAM, socket.IPPROTO_TCP)
    server.bind(('127.0.0.1', 5000))
    server.listen(1)
    try:
        while True:
            conn, addr = server.accept()
            msg = b''
            timer = True
            while timer:
                part = conn.recv(15)
                msg += part
                if b"@@@" in msg:
                    timer = False
            print(msg)
            conn.sendall(response_ok() + b"@@@")
            conn.close()
    except KeyboardInterrupt:
        conn.close()
        server.close()
        print("\nClosing the server!")
        sys.exit(1)


def response_ok():
    """Return a HTTP "200 OK" response."""
    date = email.utils.formatdate(usegmt=True).encode("utf-8")
    response_header = b"HTTP/1.1 200 OK\r\nDate:" + date + b"\r\nContent-Type: text/plain\r\n\r\nHere is the response you asked for!"
    return response_header


def response_error():
    """Return a HTTP "500 Internal Server Error"."""
    pass

if __name__ is "__main__":
    server()
