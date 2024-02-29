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
    
    def SearchResult(self):
         ChkNullDescriptorINSTANCE=ChkNullDescriptorClass(shasinum=self.recoveryObj.ShasiTxt.toPlainText(),
                                                          carId=self.recoveryObj.CarIdTxt.toPlainText(),
                                                          carOwner=self.recoveryObj.CarOwnerTxt.toPlainText(),
                                                          phone=self.recoveryObj.PhoneTxt.toPlainText())
         condition=[]
         for i in ChkNullDescriptorINSTANCE.__dict__.keys():
              if i=="phone":
                   condition.append(CarOwnerInterfaceModel.Phone==self.recoveryObj.PhoneTxt.toPlainText())
              if i=="carOwner":
                   condition.append(CarOwnerInterfaceModel.nameLastname==self.recoveryObj.CarOwnerTxt.toPlainText())
              if i=="carId":
                   condition.append(CarOwnerInterfaceModel.CarId==self.recoveryObj.CarIdTxt.toPlainText())
              if i=="shasinum":
                    condition.append(CarOwnerInterfaceModel.ShasiNum==self.recoveryObj.ShasiTxt.toPlainText())

         CarOwnerInterfaceClass_insance=CarOwnerInterface(connectionMaker.classConnection)
         res2=CarOwnerInterfaceClass_insance.search(condition)        
         condition.clear()

         return res2
          
                   
                   
    