import atexit
from sqlalchemy import String, DateTime, Integer, Column, create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


PG_DSN = 'postgresql://app:1234@127.0.0.1:5431/netology'

engine = create_engine(PG_DSN)

Base = declarative_base()
Session = sessionmaker(bind=engine)
atexit.register(engine.dispose)


class Ad(Base):

    __tablename__ = 'app_ads'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    description = Column(String(300), nullable=False)
    creation_time = Column(DateTime, server_default=func.now())
    owner = Column(String(50))

Base.metadata.create_all(bind=engine)
