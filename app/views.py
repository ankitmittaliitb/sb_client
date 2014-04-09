import datetime

from app import app	
from app import db
from flask import render_template  

from twitter import get_new_tweets
from utils import fetch_tweets, clear_publishing_history

@app.before_first_request
def before_first_request():
	clear_publishing_history()

@app.route('/')
def index():
	get_new_tweets()	#logic moved to cron 
	tweets = fetch_tweets()  
	#data = create_dictionary(tweets)
	data = {}
	data['tweet'] = tweets.tweet 
	data['posted_by'] = tweets.posted_by
	data['occured_at'] = tweets.occured_at

	return render_template("index.html", data = data)
	
	