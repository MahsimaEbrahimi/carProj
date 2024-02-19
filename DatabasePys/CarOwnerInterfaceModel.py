from sqlalchemy import ForeignKey,String,Integer,Column
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from Base import Base

class CarOwnerInterfaceModel(Base):
        __tablename__='ROwnerCar'    
        RownercarKey=Column(Integer,primary_key=True,nullable=False,autoincrement=True)
        Thekey=Column(Integer,ForeignKey('CarInf.Thekey'),nullable=False)
        CarId=Column(String(20),ForeignKey('CarTable.CarId'),nullable=False)
        ShasiNum=Column(String(10),ForeignKey('CarTable.ShasiNum'),nullable=False)
        nameLastname=Column(String(50),ForeignKey('OwnerTable.nameLastname'),nullable=False)
        Phone=Column(String(20),ForeignKey('OwnerTable.phone'),nullable=False)

        Date=Column(String(50),nullable=False)
        Time=Column(String(50),nullable=False)
        PayType=Column(String(50),nullable=False)