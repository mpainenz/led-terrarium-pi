from sqlalchemy import Column, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SensorReading(Base):
    __tablename__ = 'SensorReading'
    # Primary Key(s)
    snapshotDate = Column(DateTime, primary=True)
    # Fields
    temperature = Column(Float)
    humidity = Column(Float)

def rebuild_tables(engine):
    print 'Dropping Tables'
    Base.metadata_drop_all(engine)
    print 'Creating Tables'
    Base.metadata_create_all(engine)