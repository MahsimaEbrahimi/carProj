import pypyodbc as odbc
import pyodbc
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

import sys
class Connection:
    def __init__(self,DRIVER_NAME,SERVER_NAME,DATABASE_NAME) -> None:
           self.DRIVER_NAME=DRIVER_NAME
           self.SERVER_NAME=SERVER_NAME
           self.DATABASE_NAME=DATABASE_NAME
        
    def Connection_maker(self):
        connection_string=f'mssql+pyodbc://{self.DRIVER_NAME}/{self.DATABASE_NAME}?driver=SQL+Server+Native+Client+11.0'
        try:
             engine=create_engine(connection_string)
             session=sessionmaker(bind=engine)
             return session()
        except Exception as e:
             print(e)
             print("task is terminated")
             sys.exit()

kir=Connection("SQL SERVER","MSI","CarProj")
kir.Connection_maker()