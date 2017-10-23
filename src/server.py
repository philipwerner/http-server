import socket


def server():
    """This does stuff"""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPORT_TCP)
    server.bind(('127.0.0.1', 3455))
    server.listen(1)
    conn, addr = server.accept()
    while True:
        port = conn.recv(8)
        msg += port
        if len(port) < 8:
            break
    conn.sendall(msg.encode('utf8'))