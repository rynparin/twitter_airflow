import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs

access_key = "ipdaukyAl0Wgni9KONKFCl9Q8"
access_secret = "4Z7m6pkq99FpkFGfTV9LQykcormkJkTeXrsxhaXG0l9cz3md2O"
bearer = "AAAAAAAAAAAAAAAAAAAAAB3FiAEAAAAAIB%2BWub2%2F6XhR%2BLIxYej9eLPjVLs%3Dy5Egj0UtjI2bv06J9zCjP4DHskNLe2HDeDshVnb0FnBW7wxSGt"
consumer_key = "2899995049-6txAK1YwoPbAfPz1g46kjL43tMCpPgI6pMMSdDR"
consumer_secret = "qP93mw46U8R7DePOlNMSWm3aoFy2G0HrksqVjCLArgmKT"

# Twitter authentication
auth = tweepy.OAuthHandler(access_key, access_secret)
auth.set_access_token(consumer_key,consumer_secret)

#  Creating API object
api = tweepy.API(auth)

tweets = api.user_timeline(screen_name='@elonmusk',
                           count=200,
                           include_rts=False,
                           tweet_mode='extended')


tweet_list = []
for tweet in tweets:
    text = tweet._json["full_text"]
    refined_tweet = {
        "user" : tweet.user.screen_name,
        "text" : text,
        "favorite_count" : tweet.favorite_count,
        "retweet_count" : tweet.retweet_count,
        "created_at" : tweet.created_at
    }
    tweet_list.append(refined_tweet)
    
df = pd.DataFrame(tweet_list)
df.to_csv("elonmusk_twitter_data.csv")