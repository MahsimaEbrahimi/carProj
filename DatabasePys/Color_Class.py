from sqlalchemy import and_
from sqlalchemy import select,delete
from Color_Model import Color_Model
class Color_Class:
    def __init__(self,session) -> None:
        self.session=session
    
    def add(self,Color_Model):
        self.session.add(Color_Model)
        if(self.session.commit()==None):
           return True
    
    def Chk_redundancy(self,Color):
        Results=select(Color_Model).where(
                Color_Model.color==Color,
        )
        Results=self.session.execute(Results).fetchall()
        return Results
    
    def select_options(self):
        color_select_res=select(Color_Model)
        color_select_res=self.session.execute(color_select_res).fetchall()
        # print(color_select_res)
        return color_select_res
    
    def delete_item_color(self,color):
         dele = delete(Color_Model).where(
             Color_Model.color==color
         )
         self.session.execute(dele)
         self.session.commit()