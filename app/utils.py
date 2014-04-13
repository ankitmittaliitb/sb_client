from app import db
from models import TweetInfo, TWEET_PUBLISHED, TWEET_UNPUBLISHED

def get_max_id(object_name):	
	"""Returns the current max id of the tweets in the db"""
	query = db.session.query(db.func.max(object_name.id).label("max_id"))
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

def check_duplication(object_id, object_name):
	"""Method that returns if the current object is already present in DataBase or not"""
	object_count = db.session.query(object_name).filter(object_name.domain_id == object_id).count()
	return object_count







	
	
	




