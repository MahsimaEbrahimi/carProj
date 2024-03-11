from sqlalchemy import and_
from sqlalchemy import select,delete
from Type_Model import Type_Model
from Color_Model import Color_Model
class Type_Class:
    def __init__(self,session) -> None:
        self.session=session
    
    def add(self,Type_model):
        self.session.add(Type_model)
        if(self.session.commit()==None):
           return True
    
    def Chk_redundancy(self,item):
        Results=select(Type_Model).where(
                Type_Model.carType==item,
        )
        Results=self.session.execute(Results).fetchall()
        return Results
    
    def select_options(self):
        Type_select_res=select(Type_Model)
        Type_select_res=self.session.execute(Type_select_res).fetchall()
        return Type_select_res
    
    def delete_item_type(self,cartype):
         dele = delete(Type_Model).where(
             Type_Model.carType==cartype
         )
         self.session.execute(dele)
         self.session.commit()
