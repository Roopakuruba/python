1 .  #printing patren 

    for i in range(5):
            for j in range(i+1):
               print(j+1,end=" ")
           print()

output:
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 


2.  #printing patren by giving user input
 n = int(input())

 for i in range(n):
    for j in range(i+1):
        print(j+1,end=" ")
    print()
    

3. #printing different symbols for each line
n = int(input())

for i in range(n):
    for j in range(i+1):
        if i%2==0:
            print("*",end=" ")
        else:
            print("#",end=" ")
    print()

output:
* 
# # 
* * * 
# # # # 


5. #printing reverse star pattern 
    n = int(input())

for i in range(n):
    for j in range(n-i):
        print("*",end = " ")
    print()

output:
* * * * * 
* * * * 
* * * 
* * 
* 


6. #printing rigth star triangle   
     n = int(input())
space = n-1
start= 1
for i in range(n):
    for j in range(space):
        print(" ",end = " ")
    for j in range(start):
        print("*",end = " ")
    print()

    space= space-1
    start = start+1

output:
        * 
      * * 
    * * * 
  * * * * 
* * * * * 


7. #printing triangle numbers
     n = int(input())
space = n-1
start= 1
for i in range(n):
    for j in range(space):
        print(" ",end = " ")
    for j in range(start):
        print(j+1,end = " ")
    print()

    space= space-1
    start = start+1

output:
        1 
      1 2 
    1 2 3 
  1 2 3 4 
1 2 3 4 5 


8. #printing sum of previous number
	n = int(input())
space = n-1
start= 1
val = 1
for i in range(n):
    for j in range(space):
        print(" ",end = " ")
    for j in range(start):
        print(val,end = " ")
        val= val + 1
    print()

    space= space-1
    start = start+1

output:
      1 
    2 3 
  4 5 6 
7 8 9 10 


9. #printing right star triangle  
   n = int(input())
space = n-1
start= 1
for i in range(n):
    for j in range(space):
        print(" ",end = " ")
    for j in range(start):
        print("*",end = " ")
    print()

    space= space-1
    start = start+1

output: 
      * 
    * * 
  * * * 
* * * * 
