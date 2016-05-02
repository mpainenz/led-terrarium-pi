import config
from sqlalchemy import create_engine, Column, DateTime, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

if not config.DEMO_MODE and config.ENABLE_DB:

    print "Initializing Database"

    # SQL Alchemy Engine
    print "Connecting to SQL Database: " + config.db_name

    connection_url = "%s://%s:%s@%s/%s" % (config.db_dialect_driver, config.db_user, config.db_pass, config.db_address, config.db_name)
    #print connection_url
    engine = create_engine(connection_url, echo=False)
    engine.connect()

    # SQL Alchemy Engine
    Session = sessionmaker(bind=engine)
    session = Session()

    Base = declarative_base()
    class SensorReading(Base):
        __tablename__ = 'SensorReading'
        # Primary Key(s)
        snapshotDate = Column(DateTime, primary_key=True)
        # Fields
        temperature = Column(Float)
        humidity = Column(Float)

    def build_tables():
        try:
            Base.metadata.create_all(engine)
        except Exception as e:
            print "Error: ", e.message

    def destroy_tables():
        Base.metadata.drop_all(engine)

