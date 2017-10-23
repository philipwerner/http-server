from server import server

def test_send_message():
    from client import client
    server()
    assert client("This is a test") == msg
