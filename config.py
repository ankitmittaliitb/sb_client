import os
basedir = os.path.abspath(os.path.dirname(__file__))

#The Datbase file and the Migration repo for the App
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

#Twitter Credentials for the application
TW_CONSUMER_KEY = 'mj0yYgt80jiUQHShwdhpR0snT'
TW_CONSUMER_SECRET = 'TwjxzYXi0butJ0dfICJdVqnlh5e32w5j3iyfH2C1QboDV8EA19'
TW_SAVED_ACCESS_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAMOdWwAAAAAAlrE122IISFEuMiHEGJmqcL%2BWbro%3DFI1Y5XO8Q7Tx6Xtgq3dzqmLCUS6yqAhJUq9JyqEu8ePMb96Zs0'

#Instagram Credentials for the application
IG_CONSUMER_KEY = '015e7dface3247bfaa08b1b8e0b59ba6 '
IG_CONSUMER_SECRET = 'ba5b7eb6af2f46208bf0e535f23b87e1'

#Add the keywords here which need to be searched over Twitter
QUERIES = ['#Vespa', '@Vespa']

#The general information about the client used to fetch images.
CLIENT_LAT = '27.175015'
CLIENT_LNG = '78.042155'
CLIENT_DIS =  100
