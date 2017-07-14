#!/usr/bin/env python

import os
from markovbot import MarkovBot
import time


# Initialise a MarkovBot instance
tweetbot = MarkovBot()

# Get the current directory's path
dirname = os.path.dirname(os.path.abspath(__file__))
# Construct the path to the book
book = os.path.join(dirname, 'pink_fairy_book.txt')
# Make your bot read the book!
tweetbot.read(book)

warmup = tweetbot.generate_text(20, seedword=['goblin', 'butter'])
# generate_text sl defaults to 20 - if tweet length is > 140 chars, it is sl-1. 
print("warm-up:")
print(warmup)

# get keys
import configure

# Log in to Twitter
tweetbot.twitter_login(configure.cons_key, 
                       configure.cons_secret, 
                       configure.access_token, 
                       configure.access_token_secret
                      )

# Set some parameters
targetstring = 'PinkFairyBook' # my only code word to autoreply
keywords = ['fantasy', 'troll', 'fairy', 'princess', 'goblin'] 
# one keyword is randomly chosen to be the seedword to generate_text function
prefix = None
autoreplysuffix = '#FairyTalesRock' # this is different from the auto-tweet suffix
autotweetsuffix = '#PinkFairyBook'
maxconvdepth = None

# Start auto-responding to tweets
tweetbot.twitter_autoreply_start(targetstring, 
                                 keywords=keywords, 
                                 prefix=prefix, 
                                 suffix=autoreplysuffix, 
                                 maxconvdepth=maxconvdepth)
 
#time.sleep(86400) # one day
time.sleep(300)
tweetbot.twitter_autoreply_stop()


# Start periodically tweeting
tweetbot.twitter_tweeting_start(days=0, hours=2, minutes=30, jitter=2,
                                keywords=keywords, prefix=None, suffix=autotweetsuffix)
 
#time.sleep(86400)
time.sleep(300)
tweetbot.twitter_tweeting_stop()