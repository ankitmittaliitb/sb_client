from app import db
from models import TweetInfo
from flask import request

def get_max_id():	
	"""Returns the current max id of the tweets in the db"""
	query = db.session.query(db.func.max(TweetInfo.id).label("max_id"))
	result = query.first()
	max = result.max_id
	return max

def fetch_tweets(upper, delta):
	"""Method to fetch the tweets and update the counters"""
	lower = upper - delta
	if lower <= 0:    			#Condition to check whether or not the value we are iterating over has reduced to 0.
		upper = get_max_id()	#This plays a role when we will be mantaining the session variable to continuesly 
	 	lower = upper - delta	#show older tweets if no new tweets are coming.

	query = db.session.query(TweetInfo).filter(TweetInfo.id.between(lower+1, upper)).order_by(db.desc(TweetInfo.id))
	result = query.all()     
	data = result	 			#<- TODO after the tweets are all collected this is a good place to update the session variable 
	return data					#Since this is the last method to be executed in the app and we also have access to the id's(lower).	

	
	




