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
from messagebox import _win32
from Type_Class import Type_Class
from Color_Class import Color_Class
from Type_Model import Type_Model
from Color_Model import Color_Model
import BaseUi

class FormMethod:
    def __init__(self,Mainobj) -> None:
        self.Mainobj=Mainobj
        self.error=''        
        self.res=connectionMaker.classConnection
        self.type_instance=Type_Class(self.res)

    def SaveMethod(self):
        firstp = self.Mainobj.firstPart_id.toPlainText().strip()
        secondp = self.Mainobj.secoundPart_id.toPlainText().strip()
        thirdp = self.Mainobj.ThirdPart_id_2.toPlainText().strip()
        fourthp = self.Mainobj.FourthPart_id.toPlainText().strip()
        if (firstp == '' or secondp == '' or thirdp == '' or fourthp == ''):
            carId = ''
        else:
            carId = BaseUi.format_car_id(firstp+secondp+thirdp+"-"+fourthp)
        
        FormsMethodCarclass_Obj=FormsMethodCarclass()
        CarModelInstance=CarModel(ShasiNum=self.Mainobj.ShasiTxt.toPlainText(),
                                  CarId=carId)
        CarClassObj=CarClass(self.res)
        self.error=FormsMethodCarclass_Obj.sendToClass(CarModelInstance,CarClassObj)  
        if self.error==True:  
                phone_res= self.Mainobj.PhoneTxt.toPlainText()
                if phone_res.isnumeric():
                            
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
                            Useage=self.Mainobj.UseTxt.toPlainText(), 
                            CarType=self.Mainobj.CarTypeComb.currentText(),
                            model=self.Mainobj.TypeTxt.toPlainText()                            
                            )                            
                        

                        
                        CarinfoClassInstance=CarinfoClass(self.res)
                        result=CarinfoClassInstance.select_query(CarInfoModelInstance)
                        if(result==None):
                            self.error=FormsMethodCarclass_Obj.sendToClass(CarInfoModelInstance,CarinfoClassInstance)
                            result=CarInfoModelInstance.Thekey
                        if self.error==True:
                            CarOwnerInterfaceModelInstance=CarOwnerInterfaceModel(
                                Thekey=result,
                                ShasiNum=self.Mainobj.ShasiTxt.toPlainText().strip(),
                                  CarId=carId,

                                Date= str(JalaliDateTime.now().strftime("%Y/%m/%d")),
                                nameLastname=self.Mainobj.CarOwnerTxt.toPlainText().strip(),
                                Phone=self.Mainobj.PhoneTxt.toPlainText().strip(),      
                                )
                            CarOwnerInterfaceClassInstance=CarOwnerInterface(self.res)
                            self.error=FormsMethodCarclass_Obj.sendToClass(CarOwnerInterfaceModelInstance,CarOwnerInterfaceClassInstance)
                            if self.error==True:
                                _win32.showinfo(title="موفقیت", message="تمام اطلاعات با موفقیت ثبت شد")
                            else:
                                _win32.showerror(title="خطا در ورودی", message=self.error)
                        else:
                            _win32.showerror(title="خطا در ورودی", message=self.error)
                    else:
                      _win32.showerror(title="خطا در ورودی", message=self.error)
                else:
                     _win32.showerror(title="خطا در ورودی",message="تلفن را اشتباه وارد کرده اید")
        else:
            _win32.showerror(title="خطا در ورودی", message=self.error)

    def save_Car_Type(self, form):
         result = form.SendToAddCarType()
         if result != None:
            Type_Model_obj=Type_Model(carType=result)
            Type_Class_obj=Type_Class(self.res)
            if len(Type_Class_obj.Chk_redundancy(result))==0:
                 Type_Class_obj.add(Type_Model_obj)
                 self.Mainobj.CarTypeComb.addItem(result)
                 _win32.showinfo(title="موفقیت",message="نوع خودرو مورد نظر با موفقیت اضافه گردید")
            else:
                  _win32.showerror(title="خطا",message="مقدار مورد نظر قبلا در ديتابيس ثبت گرديده است")
                    
    def save_color(self,form):
         result=form.SendToAddCarColor()
         if result != None:
            Color_Model_obj=Color_Model(color=result)
            Color_Class_obj=Color_Class(self.res)
            if len(Color_Class_obj.Chk_redundancy(result))==0:
                 Color_Class_obj.add(Color_Model_obj)
                 self.Mainobj.CarColorComb.addItem(result)
                 _win32.showinfo(title="موفقیت",message="رنگ خودرو مورد نظر با موفقیت اضافه گردید")
            else:
                  _win32.showerror(title="خطا",message="مقدار مورد نظر قبلا در ديتابيس ثبت گرديده است")         

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
         self.type_instance.delete_item_type(item)
    
    def delete_item_color(self,item):
            Color_Class_obj=Color_Class(self.res)
            Color_Class_obj.delete_item_color(item)