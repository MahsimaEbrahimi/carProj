from sqlalchemy import select
from CarinfoModel import CarinfoModel
class CarinfoClass:
    def __init__(self,session) -> None:
        self.session=session
    def add(self,carInfoModel):
       self.session.add(carInfoModel)
       if(self.session.commit()==None):
           return True
    
    def select_query(self):
        res=select(CarinfoModel).filter_by()