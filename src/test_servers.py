# -*- coding: utf-8 -*-
"""Test functions for server module."""
import pytest



def test_response_ok_has_response_header():
    """Will test response ok has correct header."""
    from server import response_ok
    assert b"200 OK" in response_ok()

