from sqlalchemy import ForeignKey,String,Integer,Column
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()
class CarOwnerInterfaceModel(Base):
        __tablename__='ROwnerCar'    
        Thekey=Column(Integer,primary_key=False,nullable=False,autoincrement=True)
        ShasiNum=Column(String(10),primary_key=False,nullable=False)        
        CarId=Column(String(20),primary_key=False,nullable=False)
        OwnerId=Column(Integer,primary_key=False,nullable=False,autoincrement=True)
        Date=Column(String(50),primary_key=False,nullable=False)
        Time=Column(String(50),primary_key=False,nullable=False)
        PayType=Column(String(50),primary_key=False,nullable=False)