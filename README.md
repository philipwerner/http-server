# HTTP Servers

**Authors**: Cody Dibble and Philip Werner
**Version**: 1.0.0

## Overview
In this application we are attempting to build a server from scratch that will be able to handle client requests to it and respond in a correct manner. We are doing this so we can get more practice on HOW to build a server and also more hands-on knowledge of how a server and sockets actually work.

## Getting Started
Clone down this repository and set up a virtual environment by type ```python3 -m venv ENV```. After your environment is set you just need to activate it by type ```source ENV/bin/activate```. Once activate you can install all our fun testing goodies by typing ```pip install httpserver[tests]```.

## Architecture
Other than using good old fashion try/fail to learn how this all works we are also using [Python2.7](https://www.python.org/) and [Python3.6](https://www.python.org/) (sometimes to much frustration), [pytest](https://docs.pytest.org/en/latest/) and [pytest-cov](https://pypi.python.org/pypi/pytest-cov) to make sure our code is doing what we actually want them to do and [tox](https://tox.readthedocs.io/en/latest/) to make sure our code is doing what we want in both versions of Python. We are also making use of [gevent](https://pypi.python.org/pypi/gevent) to keep our serving going and firing back responses without a silly while True loop.
