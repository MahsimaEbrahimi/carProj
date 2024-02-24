'''checks whether the primary keys are emoty or not'''

from Car import CarClass
from sqlalchemy import inspect
import CarModel
from functools import wraps
import messagebox

class FormsMethodCarclass:

    def NullCheker(func):
        @wraps(func)
        def NullChekerWrap(self,TheModelInstance,TheClassObj):
            culomnLst=TheModelInstance.__table__.columns._all_columns
            # print(culomnLst) 
            runstate=True
            for i in culomnLst:
                if( i.autoincrement=='auto'):
                        if(i.type.length<len(TheModelInstance.__dict__[i.name])):
                            runstate=False
                        if (i.nullable==False) :
                                if (str(TheModelInstance.__dict__[i.name]).strip()==""):
                                    runstate=False

            if runstate:
                    func(self,TheModelInstance,TheClassObj)
                    return True
            else:
                    return False 
        return NullChekerWrap
    

    @NullCheker
    def sendToClass(self, TheModelInstance,TheClassObj):
            TheClassObj.add(TheModelInstance)
