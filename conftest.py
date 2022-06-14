import pytest

from twitter_core import Twitter


@pytest.fixture
def backend_file(tmpdir):
    temp_file = tmpdir.join('tests_file.txt')
    temp_file.write('')
    return temp_file


@pytest.fixture(params=['list', 'backend'],
                name='twitter_app')
def base(backend_file, request):
    if request.param == 'list':
        twitter_app = Twitter()
        return twitter_app
    elif request.param == 'backend':
        twitter_app = Twitter(backend=backend_file)
        return twitter_app

