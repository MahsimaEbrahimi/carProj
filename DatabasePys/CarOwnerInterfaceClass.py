class CarOwnerInterface:
    def __init__(self,session) -> None:
        self.session=session
    def add(self,CarOwnerInterfaceModel):
       self.session.add(CarOwnerInterfaceModel)
       if(self.session.commit()==None):
           return True