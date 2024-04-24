34 >>>>
    #exeption 

try:
    a = 10 / 5
    print(a)
except:                  # it exicute if the exception is raised
    print("some exception raised")
else:                    #if there is no exeption it exicute
    print("no exeption is raised ")
finally:                  #it exicute both condition 
    print("this is final block")
print("ot side the try block")



output:
	2.0
no exeption is raised 
this is final block
ot side the try block


35 >>>>>
    print("starting line")
a = [11, 22, 33]

try:
    print(a)
    print(a[2])
except:
    print("some exeption raised")
else:
    print("no exeption is raised")

finally:
        print("this is final block")
print("ot side the try block")


output:
starting line
[11, 22, 33]
33
no exeption is raised
this is final block
ot side the try block


36 >>>>>>
	print("starting line")
a = [11, 22, 33]

try:
    a = 10 / 0
except NameError:
    print("exception raised due to undefined variable")
except IndexError:
    print("exception raised due to index out of rang")
except ZeroDivisionError:
    print("exception raised due to zero division error")
except:
    print("some exeption raised")
else:
    print("no exeption is raised")

finally:
        print("this is final block")
print("ot side the try block")


output:

starting line
exception raised due to zero division error
this is final block
ot side the try block




37 >>>>>>
  print("starting line")
a = [11, 22, 33]

try:
    print(y)
    
except NameError:
    print("exception raised due to undefined variable")
try:
    print(a[5])
except IndexError:
    print("exception raised due to index out of rang")
try:
    a = 10 / 2
except ZeroDivisionError:
    print("exception raised due to zero division error")
except:
    print("some exeption raised")
else:
    print("no exeption is raised")

finally:
        print("this is final block")
print("ot side the try block")



output:

 starting line
exception raised due to undefined variable
exception raised due to index out of rang
no exeption is raised
this is final block
ot side the try block



       
