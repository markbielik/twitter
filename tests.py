import pytest

from twitter_core import Twitter


def test_twitter_startup(twitter_app):
    assert twitter_app


def test_single_tweet(twitter_app):
    twitter_app.single_tweet('Test message')
    assert twitter_app.tweets_messages == ['Test message']


def test_length_single_tweet(twitter_app):
    with pytest.raises(Exception):
        twitter_app.single_tweet('Lorem ipsum'*35)
    assert twitter_app.tweets_messages == []


def test_tweet_with_hashtag(twitter_app):
    message = "#Lorem ipsum"
    twitter_app.single_tweet(message)
    assert 'Lorem' in twitter_app.find_hashtags(message)


@pytest.mark.parametrize("message, expected", (
        ('First #lorem ipsum', ['lorem']),
        ('#Second lorem ipsum', ['Second']),
        ('Third #LOREM ipsum', ['LOREM']),
        ('Four lorem #ipsum', ['ipsum']),
        ('Five lorem #ipsum #omega', ['ipsum', 'omega']),
))
def test_tweet_with_hashtag_v2(twitter_app, message, expected):
    assert twitter_app.find_hashtags(message) == expected


def test_initialize_twitter_classes(backend_file):
    value1 = Twitter(backend=backend_file)
    value2 = Twitter(backend=backend_file)

    value1.single_tweet('Test 1')
    value1.single_tweet('Test 2')

    assert value2.tweets_messages == ['Test 1', 'Test 2']
