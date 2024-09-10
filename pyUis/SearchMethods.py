import sys, os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'DatabasePys'))
from ChkNullDescriptor import Descriptor
from ChkNullDescriptorClass import ChkNullDescriptorClass
# from Owner import OwnerClass
from connection_Maker import connectionMaker
from CarOwnerInterfaceModel import CarOwnerInterfaceModel
from CarOwnerInterfaceClass import CarOwnerInterface
import BaseUi

class RecoveryMethodsClass:
    def __init__(self,recoveryObj) -> None:
         self.recoveryObj=recoveryObj
    
    def SearchResult(self):
          firstp = self.recoveryObj.firstPart_search_id.toPlainText().strip()
          secondp = self.recoveryObj.secoundPart_search_id.toPlainText().strip()
          thirdp = self.recoveryObj.ThirdPart_search_id.toPlainText().strip()
          fourthp = self.recoveryObj.FourthPart_search_id.toPlainText().strip()
          if (firstp == '' or secondp == '' or thirdp == '' or fourthp == ''):
               carId = ''
          else:
               carId = BaseUi.format_car_id(firstp+secondp+thirdp+"-"+fourthp)
         
          ChkNullDescriptorINSTANCE=ChkNullDescriptorClass(shasinum=self.recoveryObj.ShasiTxt.toPlainText(),
                                        carId=carId,
                                        carOwner=self.recoveryObj.CarOwnerTxt.toPlainText(),
                                        phone=self.recoveryObj.PhoneTxt.toPlainText())
          condition=[]
          for i in ChkNullDescriptorINSTANCE.__dict__.keys():
              if i=="phone":
                   condition.append(CarOwnerInterfaceModel.Phone==self.recoveryObj.PhoneTxt.toPlainText().strip())
              if i=="carOwner":
                   condition.append(CarOwnerInterfaceModel.nameLastname==self.recoveryObj.CarOwnerTxt.toPlainText().strip())
              if i=="carId":
                   condition.append(CarOwnerInterfaceModel.CarId==carId)
              if i=="shasinum":
                    condition.append(CarOwnerInterfaceModel.ShasiNum==self.recoveryObj.ShasiTxt.toPlainText().strip())

          CarOwnerInterfaceClass_insance=CarOwnerInterface(connectionMaker.classConnection)
          res2=CarOwnerInterfaceClass_insance.search(condition)        
          condition.clear()

          return res2
          
                   
                   
    