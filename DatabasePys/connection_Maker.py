from Connections import Connection

class connectionMaker:
    classConnection=None

    @classmethod
    def Stable_connection(cls):    
        ConnectionObj=Connection("DESKTOP-PF3K10O\\SQLEXPRESS","CarProj")
        session=ConnectionObj.Connection_maker()
        connectionMaker.classConnection=session