from Connections import Connection

class connectionMaker:
    classConnection=None

    @classmethod
    def Stable_connection(cls):    
        ConnectionObj=Connection("MSI","CarProj")
        session=ConnectionObj.Connection_maker()
        connectionMaker.classConnection=session