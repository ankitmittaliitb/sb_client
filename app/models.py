from app import db
import datetime

#I am still apprehensive about the columns in the db as I don't think we need the recorded_at column at 
#present, still thought it might help us in some way if the application grows and we put some additional functionality	
class TweetInfo(db.Model):
	"""Stores information about the tweet which are fetched corresponding to a given Query"""
	id = db.Column(db.Integer, primary_key = True, autoincrement = True)
	domain_id = db.Column(db.String)	
	tweet = db.Column(db.String(140))
	posted_by = db.Column(db.String)
	recorded_at = db.Column(db.DateTime, default = datetime.datetime.now)
	occured_at = db.Column(db.DateTime, default = datetime.datetime.now)

	"""String representation of tweet_info"""
	def __str__(self):
		return '<Tweet %r>' % (self.id)

		

	
