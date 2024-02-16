import sys, os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'DatabasePys'))
from ChkNullDescriptor import Descriptor
from ChkNullDescriptorClass import ChkNullDescriptorClass

class searchMethodsClass:
    def __init__(self,searchObj) -> None:
         self.searchObj=searchObj
    
    def senTonull(self):
         ChkNullDescriptorINSTANCE=ChkNullDescriptorClass(shasinum=self.searchObj.ShasiTxt.toPlainText(),
                                                          carId=self.searchObj.CarIdTxt.toPlainText(),
                                                          carOwner=self.searchObj.CarOwnerTxt.toPlainText(),
                                                          phone=self.searchObj.PhoneTxt.toPlainText())
     
    def Onclick(self):
         pass
         


