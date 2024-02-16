from ownerModel import OwnerModelclass
from sqlalchemy import select
class OwnerClass:
    def __init__(self,session) -> None:
        self.session=session
    def add(self,OwnerModel):
       self.session.add(OwnerModel)
       if(self.session.commit()==None):
        #   messagebox.showinfo(title="Add",message="اطلاعات با موفقیت اضافه گردید")
           return True        


    def search(self, phone):
       res=self.session.execute(select(OwnerModelclass).where(OwnerModelclass.phone == phone))  
       print(res) 
     