import sys, os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'DatabasePys'))
from ChkNullDescriptor import Descriptor
from ChkNullDescriptorClass import ChkNullDescriptorClass

class searchMethodsClass:
    ChkNullDescriptorINSTANCE=ChkNullDescriptorClass(shasinum="  ",carId="sdf",carOwner="dsfsd",phone="eee")
    print(ChkNullDescriptorINSTANCE.__dict__)

hi=searchMethodsClass()
