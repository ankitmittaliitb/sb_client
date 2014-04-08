import datetime

from app import app	
from app import db
from flask import render_template  #, session

from twitter import get_new_tweets
from utils import get_max_id, fetch_tweets

@app.route('/')
def index():
	latest_tweets = get_new_tweets()
	max_id = get_max_id()
	default_buffer = 6

	tweets = []	
	tweet_list = []
	# TODO :This is the logic to determine which tweets are going to be returned 
	# 		on the basis of the following code. 
	# if latest_tweets:
	# 	#default_buffer = latest_tweets
	# 	tweets = fetch_tweets(max_id, default_buffer)
	# else:
	# 	tweets = fetch_tweets(SESSION_VARIABLE, default_buffer)

	tweets = fetch_tweets(max_id, default_buffer)  

	for tweet in tweets:						#Create a list of dictionary.
		data = {}
		data['tweet'] = tweet.tweet 
		data['posted_by'] = tweet.posted_by
		data['occured_at'] = tweet.occured_at
		tweet_list.append(data) 

	return render_template("index.html", tweet_list = tweet_list)
	
	