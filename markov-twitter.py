import os   # To access our OS environment variables
import twitter  # To access twitter, which is already installed on lab machines

# import markov

# forgot to put os.environ, we needed commas after each variable, and we are
# using os.environ to access our secrets so we can just use the variable names
# the whole reason we made secrets file is to hide our tokens so we dont want to put them into our program

api = twitter.Api(
    consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
    consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
    access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
    access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])

# this will print info about credentials to make sure that they are correct
print api.VerifyCredentials()

# sends a tweet
status = api.PostUpdate(random_text)

# prints to terminal the tweet you have sent
print status.text
