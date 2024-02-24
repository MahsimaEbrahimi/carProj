'''checks whether the primary keys are emoty or not'''

from Car import CarClass
import CarModel
from functools import wraps
import messagebox

class FormsMethodCarclass:

    def NullCheker(func):
        @wraps(func)
        def NullChekerWrap(self,TheModelInstance,TheClassObj):
            culomnLst=TheModelInstance.__table__.columns._all_columns
            NullErorr="فیلد های زیر خالی است "
            LengthError="فیلد های زیر بیشتر از حد مجاز اند "
            runstate=True
            for i in culomnLst:
                if (i.type.python_type==str):
                    if( i.autoincrement=='auto'and i.type.length is not None):
                            if(i.type.length<len(TheModelInstance.__dict__[i.name])):
                                LengthError+=i.description
                                runstate=False
                            if (i.nullable==False) :
                                    if (str(TheModelInstance.__dict__[i.name]).strip()==""):
                                        NullErorr+=i.description
                                        runstate=False

            resDecorator=NullErorr+LengthError

            if runstate:
                    func(self,TheModelInstance,TheClassObj)
                    return True
            else:
                    return resDecorator 
        return NullChekerWrap
    

    @NullCheker
    def sendToClass(self, TheModelInstance,TheClassObj):
            TheClassObj.add(TheModelInstance)
