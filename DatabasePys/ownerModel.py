from sqlalchemy import ForeignKey,Unicode,Integer,Column
from sqlalchemy.ext.declarative import declarative_base
from Base import Base

# Base=declarative_base()
class OwnerModelclass(Base):
        __tablename__='OwnerTable'  
        nameLastname=Column(Unicode(50),nullable=False,primary_key=True)  
        nameLastname.description="نام و نام خانوادگی"      
        phone=Column(Unicode(20),nullable=False,primary_key=True)
        phone.description="تلفن"      
       