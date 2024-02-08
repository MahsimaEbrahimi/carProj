import sys, os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'DatabasePys'))
from Connections import Connection
from CarModel import CarModel
from Car import CarClass

class FormMethod:
    def __init__(self,Mainobj) -> None:
        self.Mainobj=Mainobj

    def Stable_connection(self):    
        ConnectionObj=Connection("MSI","CarProj")
        session=ConnectionObj.Connection_maker()
        return session


    def SaveMethod(self):
        CarModelInstance=CarModel(ShasiNum=self.Mainobj.ShasiTxt.toPlainText(),
                                  CarId=self.Mainobj.CarIdTxt.toPlainText(),
                                  CarType=self.Mainobj.CarTypeComb.currentText(),
                                  CarColor=self.Mainobj.comboBox_2.currentText(),
                                  model=self.Mainobj.TypeTxt.toPlainText(),
                                  ShasiCond=self.Mainobj.ShasiCondTxt.toPlainText(),                                 
                                  OptionCond=self.Mainobj.OptionTxt.toPlainText(),                                 
                                  MotorGirboxCond=self.Mainobj.GirboxCondTxt.toPlainText(),
                                  ColorCond=self.Mainobj.CarColorCondTxt.toPlainText(),
                                 information =self.Mainobj.InfTxt.toPlainText(),
                                  Useage=self.Mainobj.UseTxt.toPlainText(),
                                  )
        
        CarClassObj=CarClass(self.Stable_connection())
        CarClassObj.add(CarModelInstance)

