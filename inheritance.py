#inheritance
#single i heritance
class S:
    def _init_(self,name,rollno):
        self.name=name
        self.rollno=rollno
class S1(S):
    def _init_(self,name,marks,rollno):

        self.marks=marks
        S._init_(self,name,rollno)

obj2=S1("shree",99,40)
print(obj2.name)
print(obj2.rollno)
print(obj2.marks)

#inheritance
#multiple inheritance
class S:
    def _init_(self,name,rollno):
        self.name=name
        self.rollno=rollno
class S1:
    def _init_(self,marks):

        self.marks=marks

class S2(S,S1):
    def _init_(self,name,rollno,marks,place):
        self.place=place
        S._init_(self,name,rollno)
        S1._init_(self,marks)
obj2=S2("shree",40,98,"ballari")
print(obj2.name)
print(obj2.rollno)
print(obj2.marks)
print(obj2.place)


#inheritance
#multilevel inheritance
class S:
    def _init_(self,name,rollno):
        self.name=name
        self.rollno=rollno
class S1(S):
    def _init_(self,name,marks,rollno):

        self.marks=marks
        S._init_(self,name,rollno)
class S2(S1):
    def _init_(self,name,rollno,marks,place):
        self.place=place
        S._init_(self,name,rollno)
        S1._init_(self,name,marks,rollno)
obj2=S2("shree",40,95,"ballari")
print(obj2.name)
print(obj2.rollno)
print(obj2.marks)
print(obj2.place)
