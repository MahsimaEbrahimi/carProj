from sqlalchemy import ForeignKey,Unicode,Integer,Column
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from Base import Base

class CarOwnerInterfaceModel(Base):
        __tablename__='ROwnerCar'    
        RownercarKey=Column(Integer,primary_key=True,nullable=False,autoincrement=True)
        Thekey=Column(Integer,ForeignKey('CarInf.Thekey'),nullable=False)
        CarId=Column(Unicode(20),ForeignKey('CarTable.CarId'),nullable=False)
        CarId.description=""
        
        ShasiNum=Column(Unicode(10),ForeignKey('CarTable.ShasiNum'),nullable=False)
        ShasiNum.description="" 

        nameLastname=Column(Unicode(50),ForeignKey('OwnerTable.nameLastname'),nullable=False)
        nameLastname.description=""      

        Phone=Column(Unicode(20),ForeignKey('OwnerTable.phone'),nullable=False)
        Phone.description=""      

        Date=Column(Unicode(50),nullable=False)
        Date.description="تاریخ"      

    
