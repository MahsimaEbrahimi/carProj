import CarModel
class CarClass:
    def __init__(self,session) -> None:
        self.session=session
    def add(self,carModel):
        self.session.add(carModel)
        self.session.commit()
