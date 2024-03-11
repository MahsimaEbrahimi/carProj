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
from Color_Model import Color_Model
from Color_Class import Color_Class
from Type_Model import Type_Model
from Type_Class import Type_Class
from functools import wraps
from persiantools.jdatetime import JalaliDateTime
import messagebox
from Type_Class import Type_Class
from Color_Class import Color_Class
from Type_Model import Type_Model
from Color_Model import Color_Model
from PyQt5.QtWidgets import QMessageBox
class FormMethod:
    def __init__(self,Mainobj) -> None:
        self.Mainobj=Mainobj
        self.error=''        
        self.res=connectionMaker.classConnection
        self.type_instance=Type_Class(self.res)


    def SaveMethod(self):

        FormsMethodCarclass_Obj=FormsMethodCarclass()
        CarModelInstance=CarModel(ShasiNum=self.Mainobj.ShasiTxt.toPlainText(),
                                  CarId=self.Mainobj.CarIdTxt.toPlainText(),
                                  CarType=self.Mainobj.CarTypeComb.currentText(),
                                  model=self.Mainobj.TypeTxt.toPlainText()
                                  )
        CarClassObj=CarClass(self.res)
        self.error=FormsMethodCarclass_Obj.sendToClass(CarModelInstance,CarClassObj)  
        if self.error==True:      
                    ownerModelInstance=OwnerModelclass(
                    nameLastname=self.Mainobj.CarOwnerTxt.toPlainText(),
                    phone=self.Mainobj.PhoneTxt.toPlainText())
                    OwnerClassObj=OwnerClass(self.res)       
                    self.error=FormsMethodCarclass_Obj.sendToClass(ownerModelInstance,OwnerClassObj) 
                    if self.error==True:  
                        CarInfoModelInstance=CarinfoModel(            
                            CarColor=self.Mainobj.CarColorComb.currentText(),
                            ShasiCond=self.Mainobj.ShasiCondTxt.toPlainText(),
                            OptionCond=self.Mainobj.OptionTxt.toPlainText(),
                            MotorGirboxCond=self.Mainobj.GirboxCondTxt.toPlainText(),
                            ColorCond=self.Mainobj.CarColorCondTxt.toPlainText(),
                            information =self.Mainobj.InfTxt.toPlainText(),
                            Useage=self.Mainobj.UseTxt.toPlainText() 
                            )
                        
                        CarinfoClassInstance=CarinfoClass(self.res)
                        result=CarinfoClassInstance.select_query(CarInfoModelInstance)
                        if(result==None):
                            self.error=FormsMethodCarclass_Obj.sendToClass(CarInfoModelInstance,CarinfoClassInstance)
                            result=CarInfoModelInstance.Thekey
                        if self.error==True:
                            CarOwnerInterfaceModelInstance=CarOwnerInterfaceModel(
                                Thekey=result,
                                ShasiNum=self.Mainobj.ShasiTxt.toPlainText(),
                                CarId=self.Mainobj.CarIdTxt.toPlainText(),     
                                Date= str(JalaliDateTime.now().strftime("%Y/%m/%d")),
                                nameLastname=self.Mainobj.CarOwnerTxt.toPlainText(),
                                Phone=self.Mainobj.PhoneTxt.toPlainText(),      
                                )
                            CarOwnerInterfaceClassInstance=CarOwnerInterface(self.res)
                            self.error=FormsMethodCarclass_Obj.sendToClass(CarOwnerInterfaceModelInstance,CarOwnerInterfaceClassInstance)
                            if self.error==True:
                                messagebox.showinfo(title="موفقیت", message="تمام اطلاعات با موفقیت ثبت شد")
                            else:
                                messagebox.showerror(title="خطا در ورودی", message=self.error)
                        else:
                            messagebox.showerror(title="خطا در ورودی", message=self.error)
                    else:
                      messagebox.showerror(title="خطا در ورودی", message=self.error)
        else:
            messagebox.showerror(title="خطا در ورودی", message=self.error)

    def save_Car_Type(self, form):
         result = form.SendToAddCarType()
         if result != None:
            Type_Model_obj=Type_Model(carType=result)
            Type_Class_obj=Type_Class(self.res)
            if len(Type_Class_obj.Chk_redundancy(result))==0:
                 Type_Class_obj.add(Type_Model_obj)
                 self.Mainobj.CarTypeComb.addItem(result)
                 messagebox.showinfo(title="موفقیت",message="نوع خودرو مورد نظر با موفقیت اضافه گردید")
            else:
                  messagebox.showerror(title="خطا",message="مقدار مورد نظر قبلا در ديتابيس ثبت گرديده است")
                    
    def save_color(self,form):
         result=form.SendToAddCarColor()
         if result != None:
            Color_Model_obj=Color_Model(color=result)
            Color_Class_obj=Color_Class(self.res)
            if len(Color_Class_obj.Chk_redundancy(result))==0:
                 Color_Class_obj.add(Color_Model_obj)
                 self.Mainobj.CarColorComb.addItem(result)
                 messagebox.showinfo(title="موفقیت",message="نوع خودرو مورد نظر با موفقیت اضافه گردید")
            else:
                  messagebox.showerror(title="خطا",message="مقدار مورد نظر قبلا در ديتابيس ثبت گرديده است")         

    def select_color_type(self):
        #   type_instance=Type_Class(self.res)
          color_instance=Color_Class(self.res)
          res_type=self.type_instance.select_options()
          res_color=color_instance.select_options()
          for i in res_type:
               self.Mainobj.CarTypeComb.addItem(i[0].carType)
          for j in res_color:
               self.Mainobj.CarColorComb.addItem(j[0].color)
               
    def delete_item_type(self,item):
         self.type_instance.delete_item(item)
           