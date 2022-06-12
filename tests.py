import pytest

from twitter_core import Twitter


def test_twitter_startup():
    twitter_app = Twitter()
    assert twitter_app


def test_single_tweet():
    twitter_app = Twitter()
    twitter_app.single_tweet('Test message')
    assert twitter_app.tweets == ['Test message']


def test_length_single_tweet():
    twitter_app = Twitter()
    with pytest.raises(Exception):
        twitter_app.single_tweet('Lorem ipsum'*35)
    assert twitter_app.tweets == []

