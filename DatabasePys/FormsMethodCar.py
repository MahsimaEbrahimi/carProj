'''checks whether the primary keys are emoty or not'''

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
            # inspectRet=inspect(TheModelInstance.__table__.columns._all_columns)
            culomnLst=TheModelInstance.__table__.columns._all_columns
            # print(culomnLst)
            for i in culomnLst:
                 if (i.nullable==False and i.autoincrement=='auto') :
                      print(i.name,"---------")
                      if TheModelInstance.__dict__[i.name].strip()=="":
                          messagebox.showinfo(title="Error",message="اشتباه در مقادیر")
        return PrimaryKeyChkWrap
                           

            # culomnLst=inspectRet.mapper.column_attrs            
            # for i in keyList:
            #     if (i.nullable!=True):
            #         if inspectRet.dict[i.name].strip()!="":  
            #             my_list.append(1)          

            #             if(len(keyList)==len(my_list)):
            #                 value=func(self, TheModelInstance,TheClassObj) 
            #                 return value
                     
            #         else:
            #           messagebox.showinfo(title="Error",message="اشتباه در مقادیر")
            #           return
            #     else:
            #         value=func(self, TheModelInstance,TheClassObj) 
            #         return value
           
            # for i in culomnLst:
            #      if i.nullable==False:
            #         TheModelInstance.__dict__[i.name]
                    #   culomnLst.remove(i)
            
            # for j in culomnLst:
                 

            

        # return PrimaryKeyChkWrap
    
    @PrimaryKeyChk
    def sendToClass(self, TheModelInstance,TheClassObj):
            TheClassObj.add(TheModelInstance)

    # def required_null(self,)