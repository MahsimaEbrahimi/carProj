from Base import Base
from sqlalchemy import ForeignKey,Column, Unicode,Integer

class Color_Model(Base):
    __tablename__='Color_Type'
    indeex=Column(Integer,primary_key=True,nullable=False,autoincrement=True)
    color=Column(Unicode(50),nullable=True)
