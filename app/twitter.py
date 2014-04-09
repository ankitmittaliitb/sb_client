import datetime
from config import CONSUMER_KEY, CONSUMER_SECRET

from birdy.twitter import AppClient
from app import app
from app import db
from models import TweetInfo 

#Create an instance of appclient for the application
client = AppClient(CONSUMER_KEY, CONSUMER_SECRET)
access_token = client.get_access_token()

#Add the keywords here which need to be searched over Twitter
QUERIES = ['#Vespa', '@Vespa']

#We can also restrict things based on the geo like you mentioned using the longitude and latitude
#parameter -> geo

#A method to fetch all the new entries for statuses regarding the keywords queried that do not have an entry in the DataBase
def get_new_tweets():
	"""Return number of tweets if any and save them in Database"""
	#TODO
	#My gut says that this for loop is an unneccessary overhead and can be significantly cut down 
	#if I do a db call here to get the occured_at of the last entry in the list and then do the twitter 
	#api call for only the statuses that have occured post the last entry as the last entry would anyway be the 
	#latest entry in the app. Will work on this tomorrow.
	#parameter -> until
	statuses = [] 
	for query in QUERIES:			
		response = client.api.search.tweets.get(q = query, count = 100)
		statuses += response.data.statuses
	
	for status in statuses:
		#check whether a tweet is already present in the DataBase
		if not db.session.query(TweetInfo).filter(TweetInfo.domain_id == status.id_str).count():  
			created_at = datetime.datetime.strptime(status.created_at, r"%a %b %d %H:%M:%S +0000 %Y")
			tweet_object = TweetInfo(tweet = status.text,
						posted_by = '{} ({})'.format(status.user.screen_name,
							status.user.followers_count),
						recorded_at = datetime.datetime.now(),
						occured_at = created_at,
						domain_id = status.id_str)
			db.session.add(tweet_object)
	db.session.commit()
	
				





