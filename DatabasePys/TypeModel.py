from Base import Base
from sqlalchemy import ForeignKey,Column, Unicode,Integer

class TypeModel(Base):
    __tablename__='TypeCar'
    ind2ex=Column(Integer,primary_key=True,nullable=False,autoincrement=True)
    carType=Column(Unicode(50),nullable=True)
