from Connections import Connection

class connectionMaker:
    classConnection=None

    @classmethod
    def Stable_connection(cls):    
        ConnectionObj=Connection("CarProj")
        session=ConnectionObj.Connection_maker()
        connectionMaker.classConnection=session