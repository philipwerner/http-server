# -*- coding: utf-8 -*-
"""Test functions for server module."""
import pytest


def test_response_ok_has_response_header():
    """Will test response ok has correct header."""
    from server import response_ok
    assert b"200 OK" in response_ok()


def test_parse_request_raises_value_error():
    """Test that value error gets raised."""
    from server import parse_request
    with pytest.raises(ValueError):
        parse_request("PUT /http-server/src/server.py HTTP/1.1\r\n\
    HOST: 127.0.0.1:5000")


def test_parse_request_raises_index_error():
    """Test that value error gets raised."""
    from server import parse_request
    with pytest.raises(IndexError):
        parse_request("GET /http-server/src/server.py HTTP/1.0\r\n\
    HOST: 127.0.0.1:5000")


def test_parse_request_raises_key_error():
    """Test that value error gets raised."""
    from server import parse_request
    with pytest.raises(KeyError):
        parse_request("GET /http-server/src/server.py HTTP/1.1\r\n")


def test_parse_request_raises_io_error():
    """Test that value error gets raised."""
    from server import parse_request
    with pytest.raises(IOError):
        parse_request("GET /htp-server/src/server.py HTTP/1.1\r\n\
    HOST: 127.0.0.1:5000")


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
    assert b"request" in response_error("malformed_request")
