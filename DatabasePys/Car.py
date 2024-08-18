from sqlalchemy import and_
from sqlalchemy import select
from CarModel import CarModel

class CarClass:
    def __init__(self,session) -> None:
        self.session=session
    def add(self,carModel):
       self.session.merge(carModel)
       if(self.session.commit()==None):
        #   messagebox.showinfo(title="Add",message="اطلاعات با موفقیت اضافه گردید")
           return True
    
    def get(self,ShasiNum,CarId):
        CarResults=select(CarModel).where(
            and_(
                CarModel.ShasiNum==ShasiNum,
                CarModel.CarId==CarId
            )
        )
        CarResults=self.session.execute(CarResults).fetchall()
        return CarResults[0][0]