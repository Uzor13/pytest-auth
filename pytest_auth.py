# -*- coding: utf-8 -*-
from firstuseauthenticator import FirstUseAuthenticator
import pytest


def pytest_addoption(parser):
    group = parser.getgroup('auth')
    group.addoption(
        '--foo',
        action='store',
        dest='dest_foo',
        default='2022',
        help='Set the value for the fixture "bar".'
    )

    parser.addini('HELLO', 'Dummy pytest.ini setting')


@pytest.fixture
def bar(request):
    return request.config.option.dest_foo

@pytest.fixture
def test_firstauthenticator():
    auth = FirstUseAuthenticator()

    # allow passwords with any length
    auth.min_password_length = 10
    return auth
