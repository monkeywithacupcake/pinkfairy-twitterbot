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

my_first_text = tweetbot.generate_text(25, seedword=['goblin', 'butter'])
print("tweetbot says:")
print(my_first_text)

# get keys
import configure

# Log in to Twitter
tweetbot.twitter_login(configure.cons_key, 
                       configure.cons_secret, 
                       configure.access_token, 
                       configure.access_token_secret
                      )

# Set some parameters for your bot
targetstring = 'askPinkFairy' # my only hashtag
keywords = ['fantasy', 'troll', 'fairy', 'princess', 'goblin']
prefix = None
suffix = '#FairyTalesRock'
maxconvdepth = None

# Start auto-responding to tweets
tweetbot.twitter_autoreply_start(targetstring, 
                                 keywords=keywords, 
                                 prefix=prefix, 
                                 suffix=suffix, 
                                 maxconvdepth=maxconvdepth)
 
# Use the following to stop auto-responding
# (Don't do this directly after starting it, or your bot will do nothing!)
time.sleep(86400)
tweetbot.twitter_autoreply_stop()


# Start periodically tweeting
tweetbot.twitter_tweeting_start(days=0, hours=19, minutes=30, keywords=None, prefix=None, suffix='#PinkFairyBook')
 
# Use the following to stop periodically tweeting
# (Don't do this directly after starting it, or your bot will do nothing!)
time.sleep(86400)
tweetbot.twitter_tweeting_stop()