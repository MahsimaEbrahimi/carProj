from CarOwnerInterfaceModel import CarOwnerInterfaceModel
class CarOwnerInterface:
    def __init__(self,session) -> None:
        self.session=session
    def add(self,CarOwnerInterfaceModel):
       self.session.add(CarOwnerInterfaceModel)
       if(self.session.commit()==None):
           return True
    
    def search(self,*args):
        query=self.session.query(CarOwnerInterfaceModel).filter(and_(args)).all()
        