class Descriptor:
    def __set_name__(self,owner,variable):
        self.variable=variable

    def __get__(self,instance,owner):
         instance.__dict__[self.variable]

    def __set__(self,instance,value):
        if value.strip()!="":
          instance.__dict__[self.variable] = value
        else:
            print("nooooo")
