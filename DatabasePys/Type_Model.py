from Base import Base
from sqlalchemy import ForeignKey,Column, Unicode,Integer

class Type_Model(Base):
    __tablename__='TypeCar'
    index2=Column(Integer,primary_key=True,nullable=False,autoincrement=True)
    carType=Column(Unicode(50),nullable=True)
