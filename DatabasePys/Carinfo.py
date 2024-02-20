from sqlalchemy import select
from CarinfoModel import CarinfoModel
from sqlalchemy import and_


class CarinfoClass:
    def __init__(self,session) -> None:
        self.session=session
    def add(self,carInfoModel):
       self.session.add(carInfoModel)
       if(self.session.commit()==None):
           return True
    
    def select_query(self,carInfoModel_instance):
        stmt = select(CarinfoModel).where(
                and_(
                    CarinfoModel.CarColor == carInfoModel_instance.CarColor.strip(),
                    CarinfoModel.ShasiCond == carInfoModel_instance.ShasiCond.strip(),
                    CarinfoModel.OptionCond == carInfoModel_instance.OptionCond.strip(),
                    CarinfoModel.MotorGirboxCond == carInfoModel_instance.MotorGirboxCond.strip(),
                    CarinfoModel.ColorCond == carInfoModel_instance.ColorCond.strip(),
                    CarinfoModel.information == carInfoModel_instance.information.strip(),
                    CarinfoModel.Useage == carInfoModel_instance.Useage.strip()
                    ))
        stmt=self.session.execute(stmt).all()
        print(stmt)
        if(stmt!=[]):
            print(stmt)
            return False
        else:
            return True
