# -*- coding: utf-8 -*-
"""Test functions for echo server."""


def test_send_message():
    """Test that the client sends and receives message."""
    from client import client
    assert client("This is a test") == "This is a test"


def test_buff_short_message():
    """Test that whole message comes when less than buffer."""
    from client import client
    assert len(client("anothe")) == 6


def test_buff_long_message():
    """Test that whole message comes when greater than buffer."""
    from client import client
    assert len(client("Caticus cuteicus throwup on")) == 27


def test_non_ascii_message():
    """Test that messages comes back un-garbled even with non-ascii."""
    from client import client
    assert client("éclairs") == "éclairs"


def test_buffer_length_exact_multiple():
    """Test that whole message comes back even if multiple of buffer."""
    from client import client
    assert len(client("This is 8 awesum")) % 8 == 0
