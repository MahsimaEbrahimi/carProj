from sqlalchemy import ForeignKey,String,Integer,Column
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()
class CarModel(Base):
        __tablename__='CarTable'
        ShasiNum=Column(String(10),primary_key=True,nullable=False)
        CarId=Column(String(20),nullable=False)
        CarType=Column(String(50),nullable=False)
        CarColor=Column(String(50),nullable=False)
        model=Column(String(50),nullable=False)
        ShasiCond=Column(String,nullable=False)
        OptionCond=Column(String,nullable=False)
        MotorGirboxCond=Column(String,nullable=False)
        ColorCond=Column(String,nullable=False)
        information=Column(String,nullable=False)
        Useage=Column(String(50),nullable=False)

