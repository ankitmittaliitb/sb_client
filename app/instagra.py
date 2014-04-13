import datetime
from instagram.client import InstagramAPI
from config import IG_CONSUMER_KEY, IG_CONSUMER_SECRET, CLIENT_LAT, CLIENT_LNG, CLIENT_DIS

from app import app
from app import db
from models import InstagramInfo

from utils import check_duplication 


api = InstagramAPI(client_id=IG_CONSUMER_KEY, client_secret=IG_CONSUMER_SECRET)

def get_new_images():
	searched_media = api.media_search(lat = CLIENT_LAT, lng = CLIENT_LNG, DISTANCE = CLIENT_DIS, count=20)

	for media in searched_media:
		image_count = check_duplication(media.id, object_name = InstagramInfo)

		if not image_count:  
			instagram_object = InstagramInfo(instagram_image_url = media.images['standard_resolution'].url,
											posted_by = media.user.username,
											recorded_at = datetime.datetime.now(),
											occured_at = media.created_time,
											domain_id = media.id,
											profile_image_url = media.user.profile_picture)
			db.session.add(instagram_object)
	db.session.commit()


    	