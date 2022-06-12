import pytest

from twitter_core import Twitter


@pytest.fixture
def twitter_app():
    twitter_app = Twitter()
    yield twitter_app
    twitter_app.delete_tweet()
