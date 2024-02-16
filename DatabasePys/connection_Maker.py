from Connections import Connection

class connectionMaker:
    
    @classmethod
    def Stable_connection():    
        ConnectionObj=Connection("MSI","CarProj")
        session=ConnectionObj.Connection_maker()
        return session