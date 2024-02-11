import sys, os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'DatabasePys'))
from Connections import Connection
from CarModel import CarModel
from Car import CarClass
from FormsMethodCar import FormsMethodCarclass
from ownerModel import OwnerModelclass
from Owner import OwnerClass
from functools import wraps

class FormMethod:
    def __init__(self,Mainobj) -> None:
        self.Mainobj=Mainobj

    def Stable_connection(self):    
        ConnectionObj=Connection("MSI","CarProj")
        session=ConnectionObj.Connection_maker()
        return session

    def SaveMethod(self):
        FormsMethodCarclassO_bj=FormsMethodCarclass()
        CarModelInstance=CarModel(ShasiNum=self.Mainobj.ShasiTxt.toPlainText(),
                                  CarId=self.Mainobj.CarIdTxt.toPlainText(),
                                  CarType=self.Mainobj.CarTypeComb.currentText(),
                                #   CarColor=self.Mainobj.comboBox_2.currentText(),
                                  model=self.Mainobj.TypeTxt.toPlainText(),
                                #   ShasiCond=self.Mainobj.ShasiCondTxt.toPlainText(),                                 
                                #   OptionCond=self.Mainobj.OptionTxt.toPlainText(),                                 
                                #   MotorGirboxCond=self.Mainobj.GirboxCondTxt.toPlainText(),
                                #   ColorCond=self.Mainobj.CarColorCondTxt.toPlainText(),
                                #  information =self.Mainobj.InfTxt.toPlainText(),
                                #   Useage=self.Mainobj.UseTxt.toPlainText(),
                                  )
        ownerModelInstance=OwnerModelclass(
            nameLastname=self.Mainobj.CarOwnerTxt.toPlainText(),
            phone=self.Mainobj.PhoneTxt.toPlainText())
        
        res=self.Stable_connection()
        CarClassObj=CarClass(res)
        FormsMethodCarclassO_bj.sendToCar(CarModelInstance,CarClassObj)
        OwnerClassObj=OwnerClass(res)
        