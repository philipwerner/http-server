# -*- coding: utf-8 -*-
"""Open a server and listen for messages from the client."""
import socket
import email.utils


def server():  # pragma: no cover
    """Open a server to echo back a message."""
    server = socket.socket(socket.AF_INET,
                           socket.SOCK_STREAM, socket.IPPROTO_TCP)
    server.bind(('127.0.0.1', 5001))
    server.listen(1)
    try:
        while True:
            conn, addr = server.accept()
            msg = b''
            message_incomplete = True
            while message_incomplete:
                part = conn.recv(8)
                msg += part
                if b"@@@" in msg:
                    message_incomplete = False
            print(msg.decode("utf-8").replace("@@@", ""))
            conn.sendall(response_ok() + msg)
            conn.close()
    except KeyboardInterrupt:
        conn.close()
        server.close()
        print("\nClosing the server!")


def response_ok():
    """Return a HTTP "200 OK" response."""
    date = email.utils.formatdate(usegmt=True).encode("utf-8")
    response_header = b"HTTP/1.1 200 OK\r\nDate:" + date + b"\r\nContent-Type:\
    text/plain\r\n\r\n"
    return response_header


def response_error():
    """Return a HTTP "500 Internal Server Error"."""
    return "HTTP/1.1 500 Internal Server Error: The server encountered an internal error\
    or misconfiguration and was unable to complete your request.\
    Please contact the server admin, master_of_web@example.com, and inform\
    them of the time the error occured, and anything you might have done that\
    may have caused the error."

if __name__ == "__main__":  # pragma: no cover
    server()
