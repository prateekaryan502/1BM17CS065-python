class calldetail():
    def __init__(self,phonenoto,phonenofrom,duration,typeof):
        self.phonenoto=phonenoto
        self.phonefrom=phonenofrom
        self.duration=duration
        self.type=typeof

class util():
    u=[]
    def __init__(self):
        self.list_of_call_objects=[]

    def parse_customer(self,list_of_call_string):
        for i in list_of_call_string:
            self.list_of_call_objects.append(calldetail(i[0],i[1],i[2],i[3]))
            
    def printlistofobjects(self):
        for i in self.list_of_call_objects:
            print(i.phonenoto,i.phonefrom,i.duration,i.type,type(i))
    
            
call='9990055566','9330023412',23,'STD'
call2='9990054541','9300012345',54,'Local'
call3='9899245678','8989945456',5,'ISD'

list_of_call_string=[call,call2,call3]
x=util()
x.parse_customer(list_of_call_string)
x.printlistofobjects()
