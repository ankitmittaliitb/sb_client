import datetime
from config import CONSUMER_KEY, CONSUMER_SECRET, SAVED_ACCESS_TOKEN

from birdy.twitter import AppClient
from app import app
from app import db
from models import TweetInfo 

from utils import check_duplication

#Create an instance of appclient for the application
client = AppClient(CONSUMER_KEY, CONSUMER_SECRET, SAVED_ACCESS_TOKEN)

#Add the keywords here which need to be searched over Twitter
QUERIES = ['#Vespa', '@Vespa']

#We can also restrict things based on the geo like you mentioned using the longitude and latitude
#parameter -> geo

#A method to fetch all the new entries for statuses regarding the keywords queried that do not have an entry in the DataBase
def get_new_tweets():
	"""Return number of tweets if any and save them in Database"""
	#TODO
	#This parameter can be used to fetch tweets based on a given date 
	#parameter -> until
	statuses = [] 
	for query in QUERIES:			
		response = client.api.search.tweets.get(q = query, count = 100)
		statuses += response.data.statuses
	
	for status in statuses:
		#check whether a tweet is already present in the DataBase
		tweet_count = check_duplication(status.id_str)
		if not tweet_count:  
			created_at = datetime.datetime.strptime(status.created_at, r"%a %b %d %H:%M:%S +0000 %Y")
			tweet_object = TweetInfo(tweet = status.text,
						posted_by = '{} ({})'.format(status.user.screen_name,
							status.user.followers_count),
						recorded_at = datetime.datetime.now(),
						occured_at = created_at,
						domain_id = status.id_str,
						profile_image_url = status.user.profile_image_url)
			db.session.add(tweet_object)
	db.session.commit()
	
				





