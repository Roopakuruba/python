#list programs


	l = [15, 18, 2, 22, 181,2,45]
n = len(l)
target = 2
result = 0

for index in range(n):
    if l[index]==target:
        result = result + 1

print("total no of occurrenceis ",result)


output:
	total no of occurrenceis  2




11.
	def findtotaloccurences(listofnumbers, target):
    result = 0
    n = len(listofnumbers)
    for index in range(n):
        if listofnumbers[index] == target:
            result = result + 1
        return result

listofnumbers = [12,34,21,-12,34,55,56,34,12]
target = 35

result = findtotaloccurrences(list2,target2)
print(result)

output: error


12.
	def totalevenno(l):
    result = 0
    n = len(l)
    for index in range(n):
        if l[index] %2 == 0:
            result = result + 1
    return result

l = [12,34,21,-12,34,55,56,34,12]

result = totalevenno(l)
print("total even numbers is",result)

:output:
 	total even numbers is 7


13.

	def findgreaterelement(nmbers):
    result = 0
    n = len(numbers)

    for index in range(n):
        if numbers[index] > result:
            result = numbers[index]
    return result

numbers = [12,34,21,-12,34,55,34,11]
result = findgreaterelement(numbers)
print("greatest number is:" , result)


output:
	greatest number is: 55



14.	def findsmallerelement(numbers):
    result = 100
    n = len(numbers)

    for index in range(n):
        if numbers[index] < result:
            result = numbers[index]
    return result

numbers = [12,34,21,34,55,34,11]
result = findsmallerelement(numbers)
print("smallest number is:" , result)



output: smallest number is: 11


15.	l = list(map(int, input().split()))
print(l)
print(l[0])  #start index
print(l[-1])# revers index  printing


output: 
	[11, 22, 33, 44, 55, 66]
        11
        66


16.

 l = list(map(int, input().split()))
print(l)
w = set(l)# multi value print single time
print(w)


result = max(l)# find maximum no in list
print(result)

output: [11, 22, 33, 44, 55, 66, 58, 58, 11, 22]
{33, 66, 11, 44, 22, 55, 58}
66
