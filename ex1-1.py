import twitter

# XXX: Go to http://dev.twitter.com/apps/new to create an app and get values
# for these credentials, which you'll need to provide in place of these
# empty string values that are defined as placeholders.
# See https://dev.twitter.com/docs/auth/oauth for more information 
# on Twitter's OAuth implementation.


CONSUMER_KEY = 'm5hOt2HnI9DFuQOjx2X1PAVyq'
CONSUMER_SECRET = 'EbT2OBS0hKnud91SMf6M3M0L129NvgTvO2gg6XpJUQnXjNvMjF'
OAUTH_TOKEN = '228126894-rUZXsXAy3Yn1T1w7L2ri5XDgxXZelnjg6mSDglDf'
OAUTH_TOKEN_SECRET = '80GkdVJwu3fFmekYA7hljjDoW1cHrSI02p7Ris1sZNTFT'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

# Nothing to see by displaying twitter_api except that it's now a
# defined variable

print(twitter_api)
