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
            culomnLst=TheModelInstance.__table__.columns._all_columns
            # print(culomnLst) 
            runstate=True
            Error_Message = ""
            for i in culomnLst:
                
                 if (i.nullable==False and i.autoincrement=='auto') :
                      if (str(TheModelInstance.__dict__[i.name]).strip()==""):
                         if (i.description!=""):
                            Error_Message += i.description +", "
                         runstate=False
            
            if runstate:
                 func(self,TheModelInstance,TheClassObj)
                 return True
            else:
                    return Error_Message 
            
        return PrimaryKeyChkWrap

    @PrimaryKeyChk
    def sendToClass(self, TheModelInstance,TheClassObj):
            TheClassObj.add(TheModelInstance)
