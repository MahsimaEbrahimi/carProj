from sqlalchemy import ForeignKey,Column, Unicode
from sqlalchemy.ext.declarative import declarative_base
from Base import Base


# Base=declarative_base()
class CarModel(Base):
        __tablename__='CarTable'      
        ShasiNum=Column(Unicode(10),primary_key=True,nullable=False)
        ShasiNum.description="شماره شاسی"      
        CarId=Column(Unicode(20),primary_key=True,nullable=False)
        CarId.description="شماره پلاک"
        CarType=Column(Unicode(50),nullable=False)
        CarType.description="نوع خودرو"
        model=Column(Unicode(50),nullable=False)
        model.description="مدل"
