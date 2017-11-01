# -*- coding: utf-8 -*-
"""Test functions for echo server."""


def test_send_message():
    """Test that the client sends and receives message."""
    from client import client
    assert client("This is a test") == "This is a test"


def test_response_ok_has_response_header():
    """Will test response ok has correct header."""
    from server import response_ok
    assert b"200 OK" in response_ok()


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
