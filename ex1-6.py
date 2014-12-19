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

# Iterate through 5 more batches of results by following the cursor

for _ in range(5):
    try:
        next_results = search_results['search_metadata']['next_results']
    except KeyError: # No more results when next_results doesn't exist
        break
        
    # Create a dictionary from next_results, which has the following form:
    # ?max_id=313519052523986943&q=NCAA&include_entities=1
    kwargs = dict([ kv.split('=') for kv in next_results[1:].split("&") ])
    
    search_results = twitter_api.search.tweets(**kwargs)
    statuses += search_results['statuses']

status_texts = [ status['text'] 
                 for status in statuses ]

screen_names = [ user_mention['screen_name'] 
                 for status in statuses
                     for user_mention in status['entities']['user_mentions'] ]

hashtags = [ hashtag['text'] 
             for status in statuses
                 for hashtag in status['entities']['hashtags'] ]

# Compute a collection of all words from all tweets
words = [ w 
          for t in status_texts 
              for w in t.split() ]

# Explore the first 5 items for each...

print(json.dumps(status_texts[0:5], indent=4))
print(json.dumps(screen_names[0:5], indent=4))
print(json.dumps(hashtags[0:5], indent=4))
print(json.dumps(words[0:5], indent=4))
