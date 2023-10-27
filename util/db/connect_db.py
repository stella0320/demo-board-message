from sqlalchemy import create_engine
from sqlalchemy import URL
from sqlalchemy.orm import sessionmaker
import os
import logging

logger = logging.getLogger(__name__)
class ConnectDb():

    def __init__(self):
        # self.host = 'demo-jc-db.cqcgkzzgqsjc.us-west-2.rds.amazonaws.com'
        # self.user_name = 'admin'
        # self.password = 'jessie0320'
        self.host = os.getenv('DB_HOST')
        self.user_name = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD')
        
    # https://docs.sqlalchemy.org/en/20/core/engines.html#mysql
    def get_engine(self):
        try:
            url_object = URL.create(
                    "mysql+pymysql",
                    username=self.user_name,
                    password=self.password,  # plain (unescaped) text
                    host=self.host,
                    database=os.getenv('DB_DATABASE'),
            )
            engine = create_engine(url_object, pool_size=30)
        except Exception as e:
            logger.debug(msg=str(e), exc_info=True)
        return engine
    
    def get_session(self):
        engine = self.get_engine()
        Session = sessionmaker(bind=engine)  # 把 DB engine 與 session 綁在一起
        session = Session()
        return session