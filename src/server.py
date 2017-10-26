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
                part = conn.recv(8)
                msg += part
                if b"@@@" in msg:
                    timer = False
            print(msg.decode("utf-8"))
            conn.sendall()
            conn.close()
    except KeyboardInterrupt:
        conn.close()
        server.close()
        print("\nClosing the server!")
        sys.exit(1)


def response_ok():
    """Return a HTTP "200 OK" response."""
    date = email.utils.formatdate(usegmt=True).encode("utf-8")
    response_header = b"HTTP/1.1 200 OK\r\nDate:" + date + b"\r\nContent-Type:\
    text/plain\r\n\r\n"
    return response_header


def response_error(error_code, reason_phrase):
    """Return a HTTP "500 Internal Server Error"."""
    return "The server encountered an internal error or misconfiguration and\
    was unable to complete your request. Please contact the server admin,\
    master_of_web@example.com, and inform them of the time the error occured,\
    and anything you might have done that may have caused the error."


def parse_request(request):
    """Parse request to make sure it is a GET request."""
    if "GET" not in request:
        raise ValueError("Server currently only accepting GET requests.")
        return "405 Method Not Allowed"
    elif "HTTP/1.1" not in request:
        raise 
    elif "HOST: 127.0.0.1:5000" not in request:
        raise ValueError("Bad Request: No Host header.")
    elif "GET /http-server/src/server.py HTTP/1.1\r\n" not in request:
        raise ValueError("Malformed request.")
    else:
        return request.split(" ")[1]

if __name__ is "__main__":
    server()
