"""Will do something. Will updated when it is known what."""
import socket


def client(message):
    """Will do a thing."""
    client = socket.socket(*socket.getaddrinfo("127.0.0.1", 3455)[1][:3])
    client.connect(("127.0.0.1", 3455))
    client.sendall(message.encode("utf8"))
    msg = ''
    while True:
        port = client.recv(8)
        msg += port.decode("utf8")
        if len(port) < 8:
            break
    return msg
    client.close()
