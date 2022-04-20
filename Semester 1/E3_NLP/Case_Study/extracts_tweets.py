# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 11:24:41 2022

@author: Manav Patadia
"""
#import twitter_info
import tweepy
import pandas as pd
API_Key = "G3nsN4GsxP3C0QuZApQnXLhnD"
API_Key_Secret = "rfc4JSKwnqJRTCXpm275u68WFVB0ranmDRNZVLHzKhgyZFxcAB"
Bearer_Token = "AAAAAAAAAAAAAAAAAAAAAK9XaQEAAAAA6v5Jy8xCol%2Bt0HvOsER88q9DBS4%3DsIsfCMJ2U3afBA9DF8sbI0lA8YaV2Xhtlq2QuhwDIHEdTlgxMM"
Access_Token = "1504467425227513861-DITkQqD2EtNfbpJRdDRXldxzrSL1D9"
Access_Token_Secret = "uoLBqN6X2RW3HlK6UpL4DHCck7dS0MV9xuTuSg90WtFJe"

consumer_key = API_Key
consumer_secret = API_Key_Secret
access_token = Access_Token
access_token_secret = Access_Token_Secret
bearer_token = Bearer_Token

client = tweepy.Client(bearer_token = bearer_token)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
API = tweepy.API(auth, wait_on_rate_limit=True)

query_list = ["AI", "Robotic Process Automation", "Cloud Computing", "Digital Marketing", "Computer Vision"]
tweets_response_list = []
for q in query_list:
    for page in tweepy.Cursor(API.search_tweets, q=q + " lang:en -filter:retweets", count=100, tweet_mode='extended').pages(50):
        for response in page:
            tweets_response_list.append([response.id_str, response.full_text, q])
    df = pd.DataFrame(tweets_response_list, columns = ['id_str', 'full_text', 'label'])
    df.to_csv("C:\spark\MCA\Semester1\E3_NLP\tweets.csv", index=False)
    
df.to_csv("C:\spark\MCA\Semester1\E3_NLP\tweets.csv", index=False)
