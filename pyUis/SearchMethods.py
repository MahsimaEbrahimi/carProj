import sys, os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'DatabasePys'))
from ChkNullDescriptor import Descriptor
from ChkNullDescriptorClass import ChkNullDescriptorClass
# from Owner import OwnerClass
from connection_Maker import connectionMaker
from CarOwnerInterfaceModel import CarOwnerInterfaceModel
from CarOwnerInterfaceClass import CarOwnerInterface

class RecoveryMethodsClass:
    
    def __init__(self,recoveryObj) -> None:
         self.recoveryObj=recoveryObj
    
    def senTonull(self):
         ChkNullDescriptorINSTANCE=ChkNullDescriptorClass(shasinum=self.recoveryObj.ShasiTxt.toPlainText(),
                                                          carId=self.recoveryObj.CarIdTxt.toPlainText(),
                                                          carOwner=self.recoveryObj.CarOwnerTxt.toPlainText(),
                                                          phone=self.recoveryObj.PhoneTxt.toPlainText())
     #     print(ChkNullDescriptorINSTANCE.__dict__)
         
     #     lst=dict()
     #     lst['ShasiTxt']=lambda:(CarOwnerInterfaceModel.ShasiNum==self.recoveryObj.ShasiTxt.toPlainText())
     #     lst['CarIdTxt']=lambda:(CarOwnerInterfaceModel.CarId==self.recoveryObj.CarIdTxt.toPlainText())
     #     lst['CarOwnerTxt']=lambda:(CarOwnerInterfaceModel.carOwner==self.recoveryObj.CarOwnerTxt.toPlainText())
     #     lst['PhoneTxt']=lambda:(CarOwnerInterfaceModel.phone==self.recoveryObj.PhoneTxt.toPlainText())

     #     print(lst)
         condition=[]
         for i in ChkNullDescriptorINSTANCE.__dict__.keys():
              if i=="phone":
                   condition.append(CarOwnerInterfaceModel.phone==self.recoveryObj.PhoneTxt.toPlainText())
               #     Owner_instance=OwnerClass(connectionMaker.classConnection)
               #     Owner_instance.search(ChkNullDescriptorINSTANCE.__dict__["phone"])
               #     print(ChkNullDescriptorINSTANCE.__dict__["phone"])
              if i=="carOwner":
                   condition.append(CarOwnerInterfaceModel.nameLastname==self.recoveryObj.CarOwnerTxt.toPlainText())
              if i=="carId":
                   condition.append(CarOwnerInterfaceModel.CarId==self.recoveryObj.CarIdTxt.toPlainText())
              if i=="shasinum":
                    condition.append(CarOwnerInterfaceModel.ShasiNum==self.recoveryObj.ShasiTxt.toPlainText())

         CarOwnerInterfaceClass_insance=CarOwnerInterface(connectionMaker.classConnection)
         CarOwnerInterfaceClass_insance.search(condition)
         condition.clear()
          
                   
                   
    