import os
basedir = os.path.abspath(os.path.dirname(__file__))

#The Datbase file and the Migration repo for the App
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

#CONSUMER_KEY and CONSUMER_SECRET for the application
CONSUMER_KEY = 'mj0yYgt80jiUQHShwdhpR0snT'
CONSUMER_SECRET = 'TwjxzYXi0butJ0dfICJdVqnlh5e32w5j3iyfH2C1QboDV8EA19'
SAVED_ACCESS_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAMOdWwAAAAAAlrE122IISFEuMiHEGJmqcL%2BWbro%3DFI1Y5XO8Q7Tx6Xtgq3dzqmLCUS6yqAhJUq9JyqEu8ePMb96Zs0'
