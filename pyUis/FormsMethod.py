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
import messagebox

class FormMethod:
    def __init__(self,Mainobj) -> None:
        self.Mainobj=Mainobj
        self.error=''

    def SaveMethod(self):
        res=connectionMaker.classConnection

        FormsMethodCarclass_Obj=FormsMethodCarclass()
        CarModelInstance=CarModel(ShasiNum=self.Mainobj.ShasiTxt.toPlainText(),
                                  CarId=self.Mainobj.CarIdTxt.toPlainText(),
                                  CarType=self.Mainobj.CarTypeComb.currentText(),
                                  model=self.Mainobj.TypeTxt.toPlainText()
                                  )
        CarClassObj=CarClass(res)
        self.error=FormsMethodCarclass_Obj.sendToClass(CarModelInstance,CarClassObj)  
        if self.error==True:      
                    ownerModelInstance=OwnerModelclass(
                    nameLastname=self.Mainobj.CarOwnerTxt.toPlainText(),
                    phone=self.Mainobj.PhoneTxt.toPlainText())
                    OwnerClassObj=OwnerClass(res)       
                    self.error=FormsMethodCarclass_Obj.sendToClass(ownerModelInstance,OwnerClassObj) 
                    if self.error==True:  
                        CarInfoModelInstance=CarinfoModel(            
                            CarColor=self.Mainobj.comboBox_2.currentText(),
                            ShasiCond=self.Mainobj.ShasiCondTxt.toPlainText(),
                            OptionCond=self.Mainobj.OptionTxt.toPlainText(),
                            MotorGirboxCond=self.Mainobj.GirboxCondTxt.toPlainText(),
                            ColorCond=self.Mainobj.CarColorCondTxt.toPlainText(),
                            information =self.Mainobj.InfTxt.toPlainText(),
                            Useage=self.Mainobj.UseTxt.toPlainText() 
                            )
                        
                        CarinfoClassInstance=CarinfoClass(res)
                        result=CarinfoClassInstance.select_query(CarInfoModelInstance)
                        if(result==None):
                            FormsMethodCarclass_Obj.sendToClass(CarInfoModelInstance,CarinfoClassInstance)
                            result=CarInfoModelInstance.Thekey


                        CarOwnerInterfaceModelInstance=CarOwnerInterfaceModel(
                            Thekey=result,
                            ShasiNum=self.Mainobj.ShasiTxt.toPlainText(),
                            CarId=self.Mainobj.CarIdTxt.toPlainText(),     
                            Date="222",
                            Time="222",
                            PayType=self.Mainobj.PayTypeComb.currentText(), 
                            nameLastname=self.Mainobj.CarOwnerTxt.toPlainText(),
                            Phone=self.Mainobj.PhoneTxt.toPlainText(),      
                            )
                        CarOwnerInterfaceClassInstance=CarOwnerInterface(res)
                        FormsMethodCarclass_Obj.sendToClass(CarOwnerInterfaceModelInstance,CarOwnerInterfaceClassInstance)
                        messagebox.showinfo(title="موفقیت", message="تمام اظلاعات با موفقیت ثبت شد")

       
                    else:  
                       messagebox.showerror(title="خطا در ورودی", message="خطا در اطلاعات مالک ")
        else:
            messagebox.showerror(title="خطا در ورودی", message="خطا در اطلاعات ماشین ")
              
        # if self.error == "":
        #     messagebox.showinfo(title="موفقیت", message="فیلد با موفقیت اضافه گردید")
        # if self.error != "":
        #     messagebox.showerror(title="خطا در ورودی", message=self.error)
        #     self.error=""
        