'''checks whether the required fields are empty and less than the identified length or not'''

from Car import CarClass
import CarModel
from functools import wraps

class FormsMethodCarclass:

    def NullCheker(func):
        @wraps(func)
        def NullChekerWrap(self,TheModelInstance,TheClassObj):
            culomnLst=TheModelInstance.__table__.columns._all_columns
            NullErorr=""
            LengthError=""
            runstate=True
            for i in culomnLst:
                if (i.type.python_type==str):
                    if( i.autoincrement=='auto'and i.type.length is not None):
                            if(i.type.length<len(TheModelInstance.__dict__[i.name])):
                                LengthError+= "طول " + i.description + " نباید بیشتر از " + str(i.type.length) + " باشد.\n"
                                runstate=False
                            if (i.nullable==False) :
                                    if (str(TheModelInstance.__dict__[i.name]).strip()==""):
                                        NullErorr+="مقدار " + i.description + " نباید خالی باشد.\n"
                                        runstate=False

            resDecorator=NullErorr+"\n"+LengthError

            if runstate:
                    func(self,TheModelInstance,TheClassObj)
                    return True
            else:
                    return resDecorator 
        return NullChekerWrap
    

    @NullCheker
    def sendToClass(self, TheModelInstance,TheClassObj):
            TheClassObj.add(TheModelInstance)
