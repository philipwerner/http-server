"""Module to hold concurrent server."""
from server import server


def concurrent_server():
    """Start up concurrent server."""
    from gevent.server import StreamServer
    connect_server = StreamServer(('127.0.0.1', 5000), server)
    connect_server.serve_forever()
