from ChkNullDescriptor import Descriptor
class ChkNullDescriptorClass:
    shasinum=Descriptor()
    carId=Descriptor()
    carOwner=Descriptor()
    phone=Descriptor()
    def __init__(self,shasinum,carId,carOwner,phone) -> None:
        self.shasinum=shasinum
        self.carId=carId
        self.carOwner=carOwner
        self.phone=phone


    