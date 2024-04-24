17.    
	#slicing
word = input()

t= word[2:9]
print(t)


output: annavee


18.    #slicing



word = input()
print(word[::-1])
t= word[5:10]
print(t)
a = word[14:21]
print(a)
b = word[21:26]
print(b)
c = word[27:30]
print(c)
d= word[0:4]
print(d)
e = word[5:16]
print(e)
f = word[9:13]
print(f)
g = word[17:31]
print(g)
print(word[20:13:-1])


output:

egaugnual nohtyp gninrael ma i
learn
python 
laung
age
i am
learning py
ning
hon launguage
nohtyp


##  day 3

19.  
	#dictionaries creating

word = input()
print(word)
store = dict()
print(store)

store['q'] = 12
store['p'] = 23
store['W'] = 18
store["channaveeresh"] = 17
print(store)

allkeys = store.keys()
print(allkeys)

allvalues = store.values()
print(allvalues)

#for each loop
for ele in allkeys:
    print(ele)

for ch in "channaveeresh":
    print(ch)


output:DICTIONARIES
{}
{'q': 12, 'p': 23, 'W': 18, 'roopa': 17}
dict_keys(['q', 'p', 'W', 'roopa'])
dict_values([12, 23, 18, 17])
q
p
W
roopa
r
o
o
p
a




20>
    word = input()
print(word)
store = dict()

for ch in word:
    if ch in store:
        store[ch] = store[ch] + 1
    else:
        store[ch] = 1
print(store)


output:
	abeabedrtdrtksrdkfv
{'a': 2, 'b': 2, 'e': 2, 'd': 3, 'r': 3, 't': 2, 'k': 2, 's': 1, 'f': 1, 'v': 1}



21>    
    	word = input()
print(word)
store = dict()

for ch in word:
    if ch in store:
        store[ch] = store[ch] + 1
    else:
        store[ch] = 1
print(store)
resultchar = '#'
resultfrequency = 0

allkeys = store.keys()
for ele in allkeys:
    if store[ele] > resultfrequency:
       resultfrequency = store[ele]
       resultchar = ele
print(resultchar, resultfrequency) 


OUTPUT:
abeabedrtrtkasrdkfva
{'a': 4, 'b': 2, 'e': 2, 'd': 2, 'r': 3, 't': 2, 'k': 2, 's': 1, 'f': 1, 'v': 1}
a 4


22>   
#while loop
print("last line get exiguted")

i = 23
while i < 25:
    print("statement-1")
    print("statement-2")
    print("statement-3")
    i  = i + 1
print("1st line get exiguted")
print("2nd line get exiguted")


output:

last line get exiguted
statement-1
statement-2
statement-3
statement-1
statement-2
statement-3
1st line get exiguted
2nd line get exiguted


