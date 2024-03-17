from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

import sys
class Connection:
    def __init__(self,DATABASE_NAME) -> None:
           self.DATABASE_NAME=DATABASE_NAME
        
    def Connection_maker(self):
        connection_string = f'sqlite:///{self.DATABASE_NAME}.db'
        try:
             engine=create_engine(connection_string)
             session=sessionmaker(bind=engine)
             return session()
        except Exception as e:
             print(e)
             print("task is terminated")
             sys.exit()

