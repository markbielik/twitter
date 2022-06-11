class Twitter(object):
    def __init__(self):
        self.tweets = []

    def single_tweet(self, message):
        if len(message) > 160:
            raise Exception("Message too long")
        self.tweets.append(message)
