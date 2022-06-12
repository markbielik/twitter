import pytest

from twitter_core import Twitter


@pytest.fixture
def twitter_app():
    twitter_app = Twitter()
    return twitter_app
