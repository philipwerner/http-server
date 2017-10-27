# -*- coding: utf-8 -*-
"""Test functions for echo server."""


def test_response_ok_has_response_header():
    """Will test response ok has correct header."""
    from server import response_ok
    assert b"200 OK" in response_ok()


def test_parse_request_raises_value_error():
    """Test that value error gets raised."""
    from server import parse_request
    with pytest.raises(ValueError):
        parse_request(b"PUT /http-server/src/server.py HTTP/1.1\r\n\
    HOST: 127.0.0.1:5000")


def test_parse_request_raises_index_error():
    """Test that value error gets raised."""
    from server import parse_request
    with pytest.raises(IndexError):
        parse_request(b"GET /http-server/src/server.py HTTP/1.0\r\n\
    HOST: 127.0.0.1:5000")


def test_parse_request_raises_key_error():
    """Test that value error gets raised."""
    from server import parse_request
    with pytest.raises(KeyError):
        parse_request(b"GET /http-server/src/server.py HTTP/1.1\r\n")


def test_parse_request_raises_io_error():
    """Test that value error gets raised."""
    from server import parse_request
    with pytest.raises(IOError):
        parse_request(b"GET /htp-server/src/server.py HTTP/1.1\r\n\
    HOST: 127.0.0.1:5000")


def test_parse_request_returns_uri_if_everything_is_cool():
    """Test that parse request returns request URI."""
    from server import parse_request
    assert parse_request(b"GET /http-server/src/server.py HTTP/1.1\r\n\
    HOST: 127.0.0.1:5000") == b"/http-server/src/server.py"


def test_response_error_forbidden_returns_403_error():
    """Test that forbidden error returns 403 Error."""
    from server import response_error
    assert b"permission" in response_error("forbidden")


def test_response_error_no_support_returns_505_error():
    """Test that no_support error returns 505 Error."""
    from server import response_error
    assert b"HTTP" in response_error("no_support")


def test_response_error_bad_request_returns_400_error():
    """Test that bad_request error returns 400 Error."""
    from server import response_error
    assert b"No" in response_error("bad_request")


def test_response_error_malformed_request_returns_400_error():
    """Test that malformed_request error returns 400 Error."""
    from server import response_error
    assert b"server" in response_error("malformed_request")


def test_client_recieves_ok_response():
    """Test that server will recieve ok response after sending proper header."""
    from client import client
    message = 'GET /http-server/src/server.py HTTP/1.1\r\nHOST: 127.0.0.1:5000'
    assert "200 OK" in client(message)


def test_client_recieves_forbidden_error():
    """Test that server sends forbidden error and client recieves it."""
    from client import client
    message = 'PUT /http-server/src/server.py HTTP/1.1\r\nHOST: 127.0.0.1:5000'
    assert "403 Forbidden" in client(message)


def test_client_recieves_http_version_error():
    """Test that server sends forbidden error and client recieves it."""
    from client import client
    message = 'GET /http-server/src/server.py HTTP/1.0\r\nHOST: 127.0.0.1:5000'
    assert "505 HTTP" in client(message)


def test_client_recieves_no_host_error():
    """Test that server sends forbidden error and client recieves it."""
    from client import client
    message = 'GET /http-server/src/server.py HTTP/1.1\r\n 127.0.0.1:5000'
    assert "400" in client(message)


def test_client_recieves_malformed_request_error():
    """Test that server sends forbidden error and client recieves it."""
    from client import client
    message = 'GET /htp-server/src/server.py HTTP/1.1\r\nHOST: 127.0.0.1:5000'
    assert "400" in client(message)

def test_response_error_sends_500_error():
    """Test that response error sends back 500 Error as string."""
    from server import response_error
    assert "500 Internal Server" in response_error()
    
    
# def test_buff_short_message():
#     """Test that whole message comes when less than buffer."""
#     from client import client
#     assert len(client("anothe")) == 6


# def test_buff_long_message():
#     """Test that whole message comes when greater than buffer."""
#     from client import client
#     assert len(client("Caticus cuteicus throwup on")) == 27


# def test_non_ascii_message():
#     """Test that messages comes back un-garbled even with non-ascii."""
#     from client import client
#     assert client("éclairs") == "éclairs"


# def test_buffer_length_exact_multiple():
#     """Test that whole message comes back even if multiple of buffer."""
#     from client import client
#     assert len(client("This is 8 awesum")) % 8 == 0

