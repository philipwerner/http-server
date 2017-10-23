"""."""
import socket


def server():
    """Will do stuff."""
    server = socket.socket(socket.AF_INET,
                           socket.SOCK_STREAM, socket.IPPROTO_TCP)
    server.bind(('127.0.0.1', 3455))
    server.listen(1)
    conn, addr = server.accept()
    msg = ''
    while True:
        port = conn.recv(8)
        msg += port.decode("utf8")
        if len(port) < 8:
            break
    conn.sendall(msg.encode("utf8"))
    conn.close()
    server.close()
