from collections import namedtuple
import os
import tweepy

Tweet = namedtuple('Tweet', 'id text created likes rts')

TWITTER_KEY = os.environ['TWITTER_KEY']
TWITTER_SECRET = os.environ['TWITTER_SECRET']
TWITTER_ACCESS_TOKEN = os.environ['TWITTER_ACCESS_TOKEN']
TWITTER_ACCESS_SECRET = os.environ['TWITTER_ACCESS_SECRET']


class Twitter:
    def __init__(self, account_name):
        self.account_name = account_name
        self.api = None

    def connect(self):
        print("Connecting...")
        auth = tweepy.OAuthHandler(TWITTER_KEY, TWITTER_SECRET)
        auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
        print("Connected to twitter API...")
        self.api = tweepy.API(auth)

    def _get_tweets(self):
        for tw in tweepy.Cursor(
            self.api.user_timeline, screen_name=self.account_name,
            exclude_replies=False, include_rts=True
        ).items():
            yield Tweet(tw.id,
                        tw.text,
                        tw.created_at,
                        tw.favorite_count,
                        tw.retweet_count)

    def get_tweets(self, exclude_retweet=False):
        tweets = self._get_tweets()
        if not exclude_retweet:
            yield from tweets
        else:
            return (tweet for tweet in tweets if not
                    tweet.text.startswith('RT'))

    def sort_by_popularity(self):
        excl_rts = list(self.get_tweets(exclude_retweet=False))
        sorted_tweets = sorted(excl_rts, key=lambda tw: (tw.likes + tw.rts)/2,
                               reverse=True)
        return sorted_tweets