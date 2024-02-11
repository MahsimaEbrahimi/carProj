class OwnerClass:
    def __init__(self,session) -> None:
        self.session=session
    def add(self,OwnerModel):
       self.session.add(OwnerModel)
       if(self.session.commit()==None):
        #   messagebox.showinfo(title="Add",message="اطلاعات با موفقیت اضافه گردید")
           return True        
    