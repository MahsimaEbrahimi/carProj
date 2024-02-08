import messagebox
class CarClass:
    def __init__(self,session) -> None:
        self.session=session
    def add(self,carModel):
       self.session.add(carModel)
       if(self.session.commit()==None):
          messagebox.showinfo(title="Add",message="اطلاعات با موفقیت اضافه گردید")
