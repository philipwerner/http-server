"""Will do something. Will updated when it is known what."""
import socket


def client(message):
    """Will do a thing."""
    client_socket = socket.socket(*socket.getaddrinfo("127.0.0.1", 3455)[1][:3])
    client_socket.connect(("127.0.0.1", 3455))
    client_socket.sendall(message.encode("utf8"))
