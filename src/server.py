# -*- coding: utf-8 -*-
"""Open a server and listen for messages from the client."""
import email.utils
import mimetypes
import os


def server(server, port):  # pragma: no cover
    """Open a server to echo back a message."""
    server = server
    msg = b''
    timer = True
    while timer:
        part = server.recv(8)
        msg += part
        if b"@@@" in msg:
            timer = False
    print(msg.decode("utf-8").replace("@@@", ""))

    try:
        server.sendall(parse_request(msg))
    except ValueError:
        server.sendall(response_error("forbidden"))
    except IndexError:
        server.sendall(response_error("no_support"))
    except KeyError:
        server.sendall(response_error("bad_request"))
    except AttributeError:
        server.sendall(response_error("malformed_request"))


def response_ok(content, content_type):
    """Return a HTTP "200 OK" response."""
    date = email.utils.formatdate(usegmt=True)
    response_header = "HTTP/1.1 200 OK\r\nDate:" + date + "\r\n\
Content-Type: {}\r\n{}@@@".format(content_type, content)
    return response_header.encode("utf-8")


def response_error(error):
    """Return a HTTP "500 Internal Server Error"."""
    if error == "forbidden":
        return b"HTTP/1.1 403 Forbidden: You don't have permission on\
 this server.@@@"
    elif error == "no_support":
        return b"505 HTTP Version Not Supported.@@@"
    elif error == "bad_request":
        return b"HTTP/1.1 The remote server returned an error: (400) Bad Request.\
 No Host.@@@"
    elif error == "malformed_request":
        return b"HTTP/1.1 The remote server returned an error: (400) Bad Request.\
 Malformed request.@@@"
    else:
        return b"The server encountered an internal error or misconfiguration and\
        was unable to complete your request. Please contact the server admin,\
        master_of_web@example.com, and inform them of the time the error occured,\
        and anything you might have done that may have caused the error.@@@"


def parse_request(request):
    """Parse request to make sure it is a GET request."""
    req_uri = request.split(b" ")[1]
    if b"GET" not in request:
        raise ValueError("Server currently only accepting GET requests.")
    elif b"HTTP/1.1" not in request:
        raise IndexError("Unaccepted HTTP version.")
    elif b"HOST: 127.0.0.1:5000" not in request:
        raise KeyError("Bad Request: No Host header.")
    elif b"www." not in request:
        raise AttributeError("Malformed request.")
    else:
        content, content_type = resolve_uri(req_uri)
        return response_ok(content, content_type)


def resolve_uri(uri):
    """Will return a body for a response and an indication of the type of content contained in the body."""
    uri = uri.decode("utf-8")
    if uri.split("/")[-1] == "":
        req_file = uri.split("/")[-2]
    else:
        req_file = uri.split("/")[-1]
    abs_path = os.path.abspath(__file__).rstrip('server.py')
    try:
        if uri[-1] == '/':
            content = ""
            content_type = "directory"
            for file in os.listdir(abs_path + req_file + "/"):
                content += file + "\n"
            return content, content_type
        else:
            img_extensions = ['jpg', 'png', 'jpeg', 'gif']
            content_type = mimetypes.guess_type(uri)
            print(req_file)
            print(abs_path + "webroot/images/" + req_file)
            if req_file.split(".")[1] in img_extensions:
                with open(abs_path + "/images/" + req_file, "rb") as file:
                    content = file.read()
            else:
                with open(abs_path + "webroot/" + req_file) as file:
                    content = file.read()
            return content, content_type[0]
    except IOError:
        return "No file or directory of that name exists"


if __name__ is "__main__":  # pragma: no cover
    server()
