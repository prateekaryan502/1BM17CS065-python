class Student:
    def __init__(self):
        self.id,self.age,self.marks=None,None,None
    def validate_marks(self):
        if 0<=self.marks<=100:
            return True
        return False
    def validate_age(self):
        if self.age>20:
            return True
        return False
    def check_qualification(self):
        if self.validate_age() and self.validate_marks():
            if self.marks>65:
                return True
        return False
    def set(self,name,marks,age):
        self.name,self.marks,self.age=name,marks,age
    def get(self):
        return self.name,self.marks,self.age

s1=Student()
s1.set("Prateek",78,24)
s=s1.get()
print("Marks validaion ? :",s1.validate_marks(),"\n","Age validation :",s1.validate_age(),"\n","Qualification :",s1.check_qualification(),"\n","Details :",s)
