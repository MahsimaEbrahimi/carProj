from Car import CarClass
from sqlalchemy import inspect
import CarModel
from functools import wraps
import messagebox

class FormsMethodCarclass:

    def PrimaryKeyChk(func):
        @wraps(func)
        def PrimaryKeyChkWrap(self,TheModelInstance,TheClassObj):
            my_list=[]
            inspectRet=inspect(TheModelInstance)
            keyList=inspectRet.mapper.primary_key
            for i in keyList:
                 if inspectRet.dict[i.name].strip()!="":  
                     my_list.append(1)          

                     if(len(keyList)==len(my_list)):
                           value=func(self, TheModelInstance,TheClassObj) 
                           return value
                 else:
                      messagebox.showinfo(title="Error",message="مقادیر پلاک و شماره شاسی را درست وارد کنید")
                      return
        return PrimaryKeyChkWrap
    
    @PrimaryKeyChk
    def sendToCar(self, TheModelInstance,TheClassObj):
            TheClassObj.add(TheModelInstance)
            