from sqlalchemy import create_engine
from sqlalchemy import URL
from sqlalchemy.orm import sessionmaker

class ConnectDb():

    def __init__(self):
        self.host = 'localhost'
        self.user_name = 'admin'
        self.password = 'jessie0320'
        
    # https://docs.sqlalchemy.org/en/20/core/engines.html#mysql
    def get_engine(self):
        url_object = URL.create(
                "mysql+pymysql",
                username=self.user_name,
                password=self.password,  # plain (unescaped) text
                host=self.host,
                database="demo",
        )

        return create_engine(url_object, pool_size=30)
    
    def get_session(self):
        engine = self.get_engine()
        Session = sessionmaker(bind=engine)  # 把 DB engine 與 session 綁在一起
        session = Session()
        return session