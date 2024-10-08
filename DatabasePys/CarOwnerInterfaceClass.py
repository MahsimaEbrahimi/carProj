from CarOwnerInterfaceModel import CarOwnerInterfaceModel
from sqlalchemy import and_,desc,asc

class CarOwnerInterface:
    def __init__(self,session) -> None:
        self.session=session
    def add(self,CarOwnerInterfaceModel):
       self.session.add(CarOwnerInterfaceModel)
       if(self.session.commit()==None):
           return True
    
    def search(self,sth):
        query=self.session.query(CarOwnerInterfaceModel).filter(and_(*sth)).order_by(desc(CarOwnerInterfaceModel.Date), 
                                                                                     desc(CarOwnerInterfaceModel.RownercarKey)).all()
        if (query!=[]):
            return query
        else:
            return False