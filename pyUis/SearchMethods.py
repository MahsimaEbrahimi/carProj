import sys, os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'DatabasePys'))
from ChkNullDescriptor import Descriptor
from ChkNullDescriptorClass import ChkNullDescriptorClass
from Owner import OwnerClass
from connection_Maker import connectionMaker


class searchMethodsClass:
    
    def __init__(self,searchObj) -> None:
         self.searchObj=searchObj
    
    def senTonull(self):
         ChkNullDescriptorINSTANCE=ChkNullDescriptorClass(shasinum=self.searchObj.ShasiTxt.toPlainText(),
                                                          carId=self.searchObj.CarIdTxt.toPlainText(),
                                                          carOwner=self.searchObj.CarOwnerTxt.toPlainText(),
                                                          phone=self.searchObj.PhoneTxt.toPlainText())
         print(ChkNullDescriptorINSTANCE.__dict__)

         for i in ChkNullDescriptorINSTANCE.__dict__.keys():
              if i=="phone":
                   Owner_instance=OwnerClass(connectionMaker.classConnection)
                   Owner_instance.search(ChkNullDescriptorINSTANCE.__dict__["phone"])
                   print(ChkNullDescriptorINSTANCE.__dict__["phone"])

                   
    