import pytest

from twitter_core import Twitter


def test_twitter_startup():
    twitter_app = Twitter()
    assert twitter_app

