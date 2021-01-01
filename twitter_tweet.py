import tweepy



# Create variables for each key, secret, token
#api == consumer

consumer_key = 'Q2JM7p6LX7rEKKmSn1zGh7n69'

consumer_secret = 'z5ogErKPGkdLigMx38tK6OAjPQPkeBex7fjB0Jw9rRoK9cKPlU'

access_token = '1114570402842411008-orSrLk4pc2xAQ47usdvj7pInhJXSW1'

access_token_secret = 'yPIVPnKV4elYA6p7e8hESZHM0IbWivcyDow25TIBBKKdS'








# Set up OAuth and integrate with API

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)



# Write a tweet to your Twitter account

tweet = "" 




api.update_status(status=tweet)

