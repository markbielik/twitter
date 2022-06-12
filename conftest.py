import pytest

from twitter_core import Twitter


@pytest.fixture(params=[None, 'tests_file.txt'])
def twitter_app(request):
    twitter_app = Twitter(backend=request.param)
    yield twitter_app
    twitter_app.delete_tweet()
