"""Import."""
import os
import sys
from ConfigParser import ConfigParser
from datetime import datetime

from sqlalchemy import (Column, DateTime, ForeignKey, Integer, MetaData,
                        String, Table, Text, create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func


# file location
def _Loc(loc = True):
    """return dir path or full path."""
    dir_path = os.path.dirname(os.path.realpath(__file__))
    full_path = os.path.realpath(__file__)

    if loc != False:
        # return dir path
        return dir_path
    else:
        # returns abs path
        return full_path

# config
config = ConfigParser() 
config.read(_Loc() + '/bck.cfg')
db = create_engine(config.get("DATABASE", "SQLALCHEMY_DATABASE_URI"))
config.get("DATABASE", "SQLALCHEMY_TRACK_MODIFICATIONS")

# database
# create all:
# execute python term
# from database import Base
# Base.metadata.create_all()
#
mymetadata = MetaData(db)
Base =  declarative_base(metadata = mymetadata)

class Backup(Base):
    """Create a sqlite table backup."""

    __tablename__ = 'backup'
    id = Column('id', Integer, primary_key = True)
    date = Column('date', DateTime, default = datetime.now)
    name = Column('name', Text)
    md5 = Column('md5', Text)

    def __init__(self, id = '', date = datetime.now, name = '', md5 = ''):
        """Constructor."""
        self.id = id
        self.date = date
        self.name = name
        self.md5 = md5

    def __repr__(self):
        """Dummy."""
        return self.name
