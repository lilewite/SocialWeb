# The Yahoo! Where On Earth ID for the entire world is 1.
# See https://dev.twitter.com/docs/api/1.1/get/trends/place and
# http://developer.yahoo.com/geo/geoplanet/
import twitter
import json


CONSUMER_KEY = 'm5hOt2HnI9DFuQOjx2X1PAVyq'
CONSUMER_SECRET = 'EbT2OBS0hKnud91SMf6M3M0L129NvgTvO2gg6XpJUQnXjNvMjF'
OAUTH_TOKEN = '228126894-rUZXsXAy3Yn1T1w7L2ri5XDgxXZelnjg6mSDglDf'
OAUTH_TOKEN_SECRET = '80GkdVJwu3fFmekYA7hljjDoW1cHrSI02p7Ris1sZNTFT'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

q = '#thfc' 

count = 100

# See https://dev.twitter.com/docs/api/1.1/get/search/tweets

search_results = twitter_api.search.tweets(q=q, count=count)

statuses = search_results['statuses']

print(type(statuses))
print(len(statuses))
print(type(statuses[0]))
print(json.dumps(statuses[0],indent=4))
