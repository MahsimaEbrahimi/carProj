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
        # CarColor=Column(Unicode(50),nullable=False)
        model=Column(Unicode(50),nullable=False)
        model.description="مدل"
        # ShasiCond=Column(Unicode,nullable=False)
        # OptionCond=Column(Unicode,nullable=False)
        # MotorGirboxCond=Column(Unicode,nullable=False)
        # ColorCond=Column(Unicode,nullable=False)
        # information=Column(Unicode,nullable=False)
        # Useage=Column(Unicode(50),nullable=False)

