from sqlalchemy import ForeignKey,String,Integer,Column
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()
class CarinfoModel(Base):
        __tablename__='CarInf'      
        Thekey=Column(Integer,primary_key=True,nullable=False,autoincrement=True)
        CarColor=Column(String(50),nullable=False)
        ShasiCond=Column(String,nullable=False)
        OptionCond=Column(String,nullable=True)
        MotorGirboxCond=Column(String,nullable=True)
        ColorCond=Column(String,nullable=True)
        information=Column(String,nullable=True)
        Useage=Column(String(50),nullable=False)

