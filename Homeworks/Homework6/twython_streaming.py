import twython
from twython import TwythonStreamer

OAUTH_TOKEN = "925147250350854144-GnFORz7Z7E5EmsEyFvMEVJxocfzLDNj"
OAUTH_TOKEN_SECRET = "PlCOVjUK0EpM9fQ9C4FiNFXI3vIGsICJDlQCiKKtVkYTT"
APP_KEY = "cRPqloj4il7LVOyULvn3GLEKb"
APP_SECRET = "0QHOZY5fdMwJGVLBf9HNjYKn0SbZyFaLJddY1SaHbi7ICO2Zyn"

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print data['text'].encode('utf-8')

    def on_error(self, status_code, data):
        print status_code

        # Want to stop trying to get data because of the error?
        # Uncomment the next line!
        self.disconnect()

if __name__ == "__main__":
    stream = MyStreamer(APP_KEY, APP_SECRET,
                    OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    stream.statuses.filter(track=['iphone', 'pixel', 'samsung'])