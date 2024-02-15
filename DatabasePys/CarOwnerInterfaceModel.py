from sqlalchemy import ForeignKey,String,Integer,Column
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from Base import Base


# Base=declarative_base()
class CarOwnerInterfaceModel(Base):
        __tablename__='ROwnerCar'    
        RownercarKey=Column(Integer,primary_key=True,nullable=False,autoincrement=True)
        Thekey=Column(Integer,ForeignKey('CarInf.Thekey'),nullable=False)
        OwnerId=Column(Integer,ForeignKey('OwnerTable.OwnerId'),nullable=False)
        CarId=Column(String(20),ForeignKey('CarTable.CarId'),nullable=False)
        ShasiNum=Column(String(10),ForeignKey('CarTable.ShasiNum'),nullable=False)
        # CarTable = relationship('CarTable', foreign_keys=[ShasiNum, CarId])
        Date=Column(String(50),nullable=False)
        Time=Column(String(50),nullable=False)
        PayType=Column(String(50),nullable=False)