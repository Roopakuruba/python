#driving license
n = int(input())
if n < 18:
   print("Ineligible")
else:
   print("Eligible")


#Calculator program

num1 = int(input())
num2 = int(input())
operator = input()[0]


if operator == '+':
   print(num1 + num2)
elif operator == '-':
   print(num1 - num2)
elif operator == '*':
   print(num1 * num2)
elif operator == '/':
   print(num1 // num2)
else:
   print("Invalid operator")


#to do list
todo_list = ["1. Buy groceries", "2. Finish report", "3. Call mom"]

print("To-Do List:")
for item in todo_list:
    print(item)
