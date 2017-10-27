# -*- coding: utf-8 -*-
"""Test functions for server module."""
import pytest


def test_response_ok_has_response_header():
    """Will test response ok has correct header."""
    from server import response_ok
    assert b"200 OK" in response_ok()


def test_response_error_sends_500_error():
    """Test that response error sends back 500 Error as string."""
    from server import response_error
    assert "500 Internal Server" in response_error()
