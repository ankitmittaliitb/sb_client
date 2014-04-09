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
	update_published_status(result)
	return result					

def update_published_status(published_tweet):
	"""Method that marks the tweet as dirty, once it is published in a current session"""
	target_id = published_tweet['id']
	db.session.query(TweetInfo).update(TweetInfo).where(TweetInfo.id == target_id).values(published = TWEET_UNPUBLISHED)
	db.session.commit()


	#query = update(TweetInfo).where(TweetInfo.id==id).values(published = TWEET_PUBLISHED)


# def create_dictionary(tweets):
# 	"""Method that returns a dictionary object from the query"""
# 	for tweet in tweets:					#Create a list of dictionary.
# 		data = {}
# 		data['id'] = tweet.id
# 		data['tweet'] = tweet.tweet 
# 		data['posted_by'] = tweet.posted_by
# 		data['occured_at'] = tweet.occured_at
# 		data['published'] = tweet.published
# 	return data

def clear_publishing_history():
	"""Method to unpublish all the existing tweets in the user DataBase"""
	target_id = get_max_id()
	query =  db.session.query(TweetInfo).update().where(TweetInfo.id <= target_id).values(published = TWEET_UNPUBLISHED)
	db.session.commit()




	
	
	




