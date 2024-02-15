from sqlalchemy import ForeignKey,String,Integer,Column
from sqlalchemy.ext.declarative import declarative_base
from Base import Base

# Base=declarative_base()
class OwnerModelclass(Base):
        __tablename__='OwnerTable'  
        OwnerId=Column(Integer,primary_key=True,nullable=False,autoincrement=True)
        nameLastname=Column(String(50),nullable=False)     
        phone=Column(String(20),nullable=False)     
               