from sqlalchemy import ForeignKey,String,Integer,Column
from sqlalchemy.ext.declarative import declarative_base
from Base import Base

# Base=declarative_base()
class OwnerModelclass(Base):
        __tablename__='OwnerTable'  
        nameLastname=Column(String(50),nullable=False,primary_key=True)     
        phone=Column(String(20),nullable=False,primary_key=True)