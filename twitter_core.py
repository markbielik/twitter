import json

import re
from urllib.parse import urljoin

import requests as requests

API_USERS = 'https://api.github.com/users'


class Twitter(object):
    ver = '0.1'

    def __init__(self, backend=None, username=None):
        self.backend = backend
        self._tweets = []
        self.username = username

    @property
    def tweets(self):
        if self.backend and not self._tweets:
            backend_text = self.backend.read()
            if backend_text:
                self._tweets = json.loads(backend_text)
        return self._tweets

    def single_tweet(self, message):
        if len(message) > 160:
            raise Exception("Message too long")
        self.tweets.append({'message': message,
                            'avatar': self.get_user_avatar(),
                            'hashtags': self.find_hashtags(message),
                            })
        if self.backend:
            self.backend.write(json.dumps(self.tweets))

    def find_hashtags(self, message):
        return re.findall("#(\w+)", message)

    # def delete_tweet(self):
    #     if self.backend:
    #         os.remove(self.backend)

    @property
    def tweets_messages(self):
        return [tweet['message'] for tweet in self.tweets]

    def get_user_avatar(self):
        if not self.username:
            return None
        url = urljoin(API_USERS, self.username)
        response = requests.get(url)
        return response.json()['avatar_url']
