from CarOwnerInterfaceModel import CarOwnerInterfaceModel
from sqlalchemy import and_, or_
import messagebox
class CarOwnerInterface:
    def __init__(self,session) -> None:
        self.session=session
    def add(self,CarOwnerInterfaceModel):
       self.session.add(CarOwnerInterfaceModel)
       if(self.session.commit()==None):
           return True
    
    def search(self,sth):
        query=self.session.query(CarOwnerInterfaceModel).filter(and_(*sth)).all()
        if (query!=[]):
            print(query)
        else:
            messagebox.showerror(title="خطا", message="اطلاعات مورد نظر شما وجود ندارد")