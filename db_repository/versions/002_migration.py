from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
tweet_info = Table('tweet_info', pre_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('domain_id', String),
    Column('tweet', String),
    Column('posted_by', String),
    Column('recorded_at', DateTime),
    Column('occurred_at', DateTime),
)

tweet_info = Table('tweet_info', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('domain_id', String),
    Column('tweet', String(length=140)),
    Column('posted_by', String),
    Column('recorded_at', DateTime, default=ColumnDefault(<function <lambda> at 0x37f7e60>)),
    Column('occured_at', DateTime, default=ColumnDefault(<function <lambda> at 0x37f7ed8>)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['tweet_info'].columns['occurred_at'].drop()
    post_meta.tables['tweet_info'].columns['occured_at'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['tweet_info'].columns['occurred_at'].create()
    post_meta.tables['tweet_info'].columns['occured_at'].drop()
