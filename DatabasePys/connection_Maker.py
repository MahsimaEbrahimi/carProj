from Connections import Connection

class connectionMaker:
    classConnection=0

    @classmethod
    def Stable_connection():    
        ConnectionObj=Connection("MSI","CarProj")
        session=ConnectionObj.Connection_maker()
        connectionMaker.classConnection=session