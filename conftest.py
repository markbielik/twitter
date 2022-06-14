import pytest

from tests import ResponseGetMock
from twitter_core import Twitter


@pytest.fixture
def backend_file(tmpdir):
    temp_file = tmpdir.join('tests_file.txt')
    temp_file.write('')
    return temp_file


@pytest.fixture(params=['list', 'backend'], name='twitter_app')
def base(backend_file, request, username, monkeypatch):
    if request.param == 'list':
        twitter_app = Twitter(username=username)
    elif request.param == 'backend':
        twitter_app = Twitter(backend=backend_file, username=username)

    def monkey_return(url):
        return ResponseGetMock()

    return twitter_app


@pytest.fixture(params=[None, 'python'])
def username(request):
    return request.param


@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    monkeypatch.delattr('requests.sessions.Session.request')

