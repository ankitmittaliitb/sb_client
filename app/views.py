import datetime

from app import app	
from app import db
from flask import render_template  

from twitter import get_new_tweets
from utils import get_max_id, fetch_tweets

@app.route('/')
def index():
	latest_tweets = get_new_tweets()
	max_id = get_max_id()
	
	tweets = fetch_tweets(max_id)  

	for tweet in tweets:					#Create a list of dictionary.
		data = {}
		data['tweet'] = tweet.tweet 
		data['posted_by'] = tweet.posted_by
		data['occured_at'] = tweet.occured_at
	
	return render_template("index.html", data = data)
	
	