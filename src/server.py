# -*- coding: utf-8 -*-
"""Open a server and listen for messages from the client."""
import socket
import sys
import email.utils


def server():  # pragma: no cover
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
            try:
                if parse_request(msg) == b"/http-server/src/server.py":
                    conn.sendall(response_ok())
            except ValueError:
                response_error(b"forbidden")
            except IndexError:
                response_error(b"no_support")
            except KeyError:
                response_error(b"bad_request")
            except IOError:
                response_error(b"malformed_request")
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


def response_error(error):
    """Return a HTTP "500 Internal Server Error"."""
    if error == "forbidden":
        return b"403 Forbidden: You don't have permission on this server."
    if error == "no_support":
        return b"505 HTTP Version Not Supported."
    if error == "bad_request":
        return b"The remote server returned an error: (400) Bad Request.\
        No Host."
    if error == b"malformed_request":
        return b"The remote server returned an error: (400) Bad Request.\
        Malformed request."
    # return "The server encountered an internal error or misconfiguration and\
    # was unable to complete your request. Please contact the server admin,\
    # master_of_web@example.com, and inform them of the time the error occured,\
    # and anything you might have done that may have caused the error."


def parse_request(request):
    """Parse request to make sure it is a GET request."""
    if b"GET" not in request:
        raise ValueError("Server currently only accepting GET requests.")
    elif "HTTP/1.1" not in request:
        raise IndexError("Unaccepted HTTP version.")
    elif "HOST: 127.0.0.1:5000" not in request:
        raise KeyError("Bad Request: No Host header.")
    elif "GET /http-server/src/server.py HTTP/1.1\r\n" not in request:
        raise IOError("Malformed request.")
    else:
        return request.split(b" ")[1]

if __name__ is "__main__":  # pragma: no cover
    server()
