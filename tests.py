from unittest.mock import patch, Mock, MagicMock

import pytest

from twitter_core import Twitter


class ResponseGetMock(object):
    def json(self):
        return {'avatar_url': 'test'}


def test_twitter_startup(twitter_app):
    assert twitter_app


def test_single_tweet(twitter_app):
    with patch.object(twitter_app, 'get_user_avatar', return_value='test'):
        twitter_app.single_tweet('Test message')
        assert twitter_app.tweets_messages == ['Test message']


def test_length_single_tweet(twitter_app):
    with pytest.raises(Exception):
        twitter_app.single_tweet('Lorem ipsum'*35)
    assert twitter_app.tweets_messages == []


def test_tweet_with_hashtag(twitter_app):
    message = "#Lorem ipsum"
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


@patch.object(Twitter, 'get_user_avatar', return_value='test')
def test_twitter_with_username(avatar_mock, twitter_app):
    if not twitter_app.username:
        pytest.skip()

    twitter_app.single_tweet('Lorem ipsum')
    assert twitter_app.tweets == [{'message': 'Lorem ipsum',
                                   'avatar': 'test',
                                   'hashtags': []
                                   }]
    avatar_mock.assert_called()


@patch.object(Twitter, 'get_user_avatar', return_value='test')
def test_tweet_with_hashtags_mock(avatar_mock, twitter_app):
    twitter_app.find_hashtags = Mock()
    twitter_app.find_hashtags.return_value = ['lorem']
    twitter_app.single_tweet('Test #ipsum')
    assert twitter_app.tweets[0]['hashtags'] == ['lorem']
    twitter_app.find_hashtags.assert_called_with('Test #ipsum')


def test_version_app(twitter_app):
    twitter_app.ver = MagicMock()
    twitter_app.ver.__eq__.return_value = '1.0'
    assert twitter_app.ver == '1.0'

