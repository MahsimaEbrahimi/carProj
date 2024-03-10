from sqlalchemy import and_
from sqlalchemy import select
from Color_Model import Color_Model
class Color_Class:
    def __init__(self,session) -> None:
        self.session=session
    
    def add(self,Color_Model):
        self.session.add(Color_Model)
        if(self.session.commit()==None):
           return True
    
    def Chk_redundancy(self,Color):
        CarResults=select(Color_Model).where(
                Color_Model.color==Color,
        )
        CarResults=self.session.execute(CarResults).fetchall()
        return CarResults