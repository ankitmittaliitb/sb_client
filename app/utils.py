from app import db
from models import TweetInfo, TWEET_PUBLISHED, TWEET_UNPUBLISHED

def get_max_id():	
	"""Returns the current max id of the tweets in the db"""
	query = db.session.query(db.func.max(TweetInfo.id).label("max_id"))
	result = query.first()
	max = result.max_id
	return max
	
def fetch_tweets():
	"""Method to fetch the tweets and update the counters"""
	query = db.session.query(TweetInfo).filter(TweetInfo.published == TWEET_UNPUBLISHED).order_by(db.desc(TweetInfo.id))
	result = query.first()     
	result.published = TWEET_PUBLISHED 
	db.session.commit()
	return result	

def clear_publishing_history():
	"""Method to unpublish all the existing tweets in the user DataBase"""
	query = db.session.query(TweetInfo).filter(TweetInfo.published == TWEET_PUBLISHED).order_by(db.desc(TweetInfo.id))
	result = query.all()
	for tweet in result:
		tweet.published = TWEET_UNPUBLISHED

	db.session.commit()

def check_duplication(tweet_id):
	"""Method that returns if the current tweet is already present in DataBase or not"""
	tweet_count = db.session.query(TweetInfo).filter(TweetInfo.domain_id == tweet_id).count()
	return tweet_count







	
	
	




