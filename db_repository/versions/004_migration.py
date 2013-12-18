from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
value = Table('value', pre_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('value', String),
)

variable = Table('variable', pre_meta,
    Column('server_id', Integer, primary_key=True, nullable=False),
    Column('value_id', Integer, primary_key=True, nullable=False),
    Column('key', String),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['value'].drop()
    pre_meta.tables['variable'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['value'].create()
    pre_meta.tables['variable'].create()
