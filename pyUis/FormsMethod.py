import sys, os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'DatabasePys'))
from connection_Maker import connectionMaker
from CarModel import CarModel
from Car import CarClass
from FormsMethodCar import FormsMethodCarclass
from ownerModel import OwnerModelclass
from Owner import OwnerClass
from CarinfoModel import CarinfoModel
from Carinfo import CarinfoClass
from CarOwnerInterfaceModel import CarOwnerInterfaceModel
from CarOwnerInterfaceClass import CarOwnerInterface
from functools import wraps

class FormMethod:
    def __init__(self,Mainobj) -> None:
        self.Mainobj=Mainobj

    def SaveMethod(self):
        FormsMethodCarclass_Obj=FormsMethodCarclass()
        CarModelInstance=CarModel(ShasiNum=self.Mainobj.ShasiTxt.toPlainText(),
                                  CarId=self.Mainobj.CarIdTxt.toPlainText(),
                                  CarType=self.Mainobj.CarTypeComb.currentText(),
                                  model=self.Mainobj.TypeTxt.toPlainText()
                                  )
        CarInfoModelInstance=CarinfoModel(            
            CarColor=self.Mainobj.comboBox_2.currentText(),
            ShasiCond=self.Mainobj.ShasiCondTxt.toPlainText(),
            OptionCond=self.Mainobj.OptionTxt.toPlainText(),
            MotorGirboxCond=self.Mainobj.GirboxCondTxt.toPlainText(),
             ColorCond=self.Mainobj.CarColorCondTxt.toPlainText(),
              information =self.Mainobj.InfTxt.toPlainText(),
               Useage=self.Mainobj.UseTxt.toPlainText() 
               )

        
        ownerModelInstance=OwnerModelclass(
            nameLastname=self.Mainobj.CarOwnerTxt.toPlainText(),
            phone=self.Mainobj.PhoneTxt.toPlainText())
        


        res=connectionMaker.classConnection

        CarClassObj=CarClass(res)
        FormsMethodCarclass_Obj.sendToClass(CarModelInstance,CarClassObj)

        OwnerClassObj=OwnerClass(res)
        
        FormsMethodCarclass_Obj.sendToClass(ownerModelInstance,OwnerClassObj)
        CarinfoClassInstance=CarinfoClass(res)
        FormsMethodCarclass_Obj.sendToClass(CarInfoModelInstance,CarinfoClassInstance)


        CarOwnerInterfaceModelInstance=CarOwnerInterfaceModel(            
            Thekey = CarInfoModelInstance.Thekey,
            ShasiNum=self.Mainobj.ShasiTxt.toPlainText(),
            CarId=self.Mainobj.CarIdTxt.toPlainText(),     
            Date="",
            Time="",
            PayType=self.Mainobj.PayTypeComb.currentText(), 
            nameLastname=self.Mainobj.CarOwnerTxt.toPlainText(),
            phone=self.Mainobj.PhoneTxt.toPlainText(),      
            )
        
        CarOwnerInterfaceClassInstance=CarOwnerInterface(res)
        FormsMethodCarclass_Obj.sendToClass(CarOwnerInterfaceModelInstance,CarOwnerInterfaceClassInstance)
