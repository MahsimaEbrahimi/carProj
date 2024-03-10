from sqlalchemy import and_
from sqlalchemy import select
from Type_Model import Type_Model
class Type_Class:
    def __init__(self,session) -> None:
        self.session=session
    
    def add(self,Type_model):
        self.session.add(Type_model)
        if(self.session.commit()==None):
           return True
    
    def Chk_redundancy(self,carType):
        Results=select(Type_Model).where(
                Type_Model.carType==carType,
        )
        Results=self.session.execute(Results).fetchall()
        return Results