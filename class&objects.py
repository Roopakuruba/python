27 >>>>
  # classs

class Box:
    def __init__(self):
        self.name = "channa"
        self.rollno = 204
        self.dbmsmarks = 67
        self.osmarks = 78
        self.javamarks = 89
        self.dsmarks = 79
        self.cmarks = 68

student1 = Box()
print(student1.name)
print(student1.rollno)
print(student1.cmarks)


28 >>>


	class Box:
    def __init__(self, currname,currrollno,currdbmsmarks,currosmarks,currjavamarks,currdsmarks,currcmarks):
        self.name = currname
        self.rollno = currrollno
        self.dbmsmarks = currdbmsmarks
        self.osmarks = currosmarks
        self.javamarks = currjavamarks
        self.dsmarks = currdsmarks
        self.cmarks = currcmarks

student1 = Box( "channa",263,88,75,92,95,80)
print(student1.name)
print(student1.rollno)
print(student1.cmarks)


student2 = Box("veeresh",561,78,65,64,89,38)
print(student2.name)
print(student2.rollno)
print(student2.cmarks)


30 >>>>
 	class Card:
    def __init__(self, imageURL,price,rating,description,deliverywithin,comments,brandname):
        self.image = imageURL
        self.price = price
        self.rating = rating
        self.description = description
        self.deliverywithin = deliverywithin
        self.comments = comments
        self.brandname = brandname

phone1 = Card("dfdkddj.jpg",10000,5,"good quality", "7 days"," nice","apple")
print(phone1.image)
print(phone1.rating)
print(phone1.price)



31 >>>>
  	class Card:
    def __init__(self, imageURL,price,rating,description,deliverywithin,comments,brandname):
        self.image = imageURL
        self.price = price
        self.rating = rating
        self.description = description
        self.deliverywithin = deliverywithin
        self.comments = comments
        self.brandname = brandname

    def printalldetails(self):
        print("brand name is:",self.brandname)
        print("product rate is:",self.price)
        print("product rating is:",self.rating)
        

phone1 = Card("dfdkddj.jpg",100000,5,"good quality", "7 days"," nice","apple")
phone1.printalldetails()
laptop = Card("dhygu.jpg",120000,4.9,"best quality","5 days","okk","dell")
laptop.printalldetails()




32 >>>>
	class Card:
    def __init__(self, imageURL,price,rating,description,deliverywithin,comments,brandname):
        self.image = imageURL
        self.price = price
        self.rating = rating
        self.description = description
        self.deliverywithin = deliverywithin
        self.comments = comments
        self.brandname = brandname

    def printbasicdetails(self):   #this is member function
        print("brand name is:",self.brandname)
        print("product rate is:",self.price)
        print("product rating is:",self.rating)

    def printalldetails(self):
        print("brand name is:",self.brandname)
        print("product rate is:",self.price)
        print("product rating is:",self.rating)

    def calculategst(self):
        print("calculating GST")
        

phone1 = Card("dfdkddj.jpg",100000,5,"good quality", "7 days"," nice","apple")
phone1.printalldetails()
phone1.printbasicdetails()
laptop = Card("dhygu.jpg",120000,4.9,"best quality","5 days","okk","dell")
laptop.printalldetails()
laptop.printbasicdetails()



33 >>>>
	actualpassword = 2387
password = int(input())

if password != actualpassword:
    print("Incorrect password,you are left with 2 attempts")

elif password != actualpassword:
    print("Incorrect password,you are left with 1 attempts")

elif password != actualpassword:
    print("Incorrect password,you are left with 1 attempts")

else:
    print("successfuly looged in")


Classes and Objects  (Student details)

class Box:
   def __init__(self, currentName, currentRollNo, currentdbmsMarks, currentPythonMarks, currentCMarks, currentOSMarks, currentCNMarks):
       self.name = currentName
       self.rollNo = currentRollNo
       self.dbmsMarks = currentdbmsMarks
       self.pythonMarks = currentPythonMarks
       self.cMarks = currentCMarks
       self.osMarks = currentOSMarks
       self.cnMarks = currentCNMarks
      
   def printDetails(self):
       print(self.name, self.rollNo, self.dbmsMarks, self.pythonMarks, self.cMarks, self.osMarks, self.cnMarks)
      


student1 = Box("Harika", "5A1", 78, 67, 77, 89, 46)
student2 = Box("Swapna", "5A2", 38, 65, 97, 59, 41)
student3 = Box("Sushma", "5A3", 88, 95, 47, 89, 31)


student1.printDetails()
student2.printDetails()
student3.printDetails()
      


Classes and objects (Amazon card)

class Card:
   def __init__(self, currId, currImageUrl, currDeviceType, currPrice, curRating):
       self.id = currId
       self.imageUrl = currImageUrl
       self.deviceType = currDeviceType
       self.price = currPrice
       self.rating = curRating
      
   def printDetails(self):
       print("Product -", self.id, ":")
       print("imageUrl:", self.imageUrl)
       print("deviceType:", self.deviceType)
       print("price:", self.price)
       print("rating:", self.rating)
      
      
mobile = Card(1, "Dummy-url 1", "Mobile", 56000, 4.5)
laptop = Card(2, "Dummy-url 2", "Laptop", 94000, 4.8)
watch = Card(3, "Dummy-url 3", "Smart-watch", 18000, 3.5)


mobile.printDetails()
print()
laptop.printDetails()
print()
watch.printDetails()
