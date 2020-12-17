# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.
l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))
print ','.join(l)

# Write a program which can compute the factorial of a given numbers. The results should be printed in a comma-separated sequence on a single line. 
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)
x=int(raw_input())
print fact(x)

# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
n=int(raw_input())
d=dict()
for i in range(1,n+1):
    d[i]=i*i
print d

# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
values=raw_input()
l=values.split(",")
t=tuple(l)
print l
print t

# Define a class which has at least two methods: getString: to get a string from console input
class InputOutString(object):
    def __init__(self):
        self.s = ""
    def getString(self):
        self.s = raw_input()
strObj = InputOutString()
strObj.getString()
# Write a program that calculates and prints the value according to the given formula: Q = Square root of [(2 * C * D)/H]
import math
c=50
h=30
value = []
items=[x for x in raw_input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
print ','.join(value)

# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
input_str = raw_input()
dimensions=[int(x) for x in input_str.split(',')]
rowNum=dimensions[0]
colNum=dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]= row*col
print multilist

# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
items=[x for x in raw_input().split(',')]
items.sort()
print ','.join(items)

# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
lines = []
while True:
    s = raw_input()
    if s:
        lines.append(s.upper())
    else:
        break;
for sentence in lines:
    print sentence

# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
s = raw_input()
words = [word for word in s.split(" ")]
print " ".join(sorted(list(set(words))))

# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
value = []
items=[x for x in raw_input().split(',')]
for p in items:
    intp = int(p, 2)
    if not intp%5:
        value.append(p)
print ','.join(value)

# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number. The numbers obtained should be printed in a comma-separated sequence on a single line.
values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print ",".join(values)

# Write a program that accepts a sentence and calculate the number of letters and digits.
s = raw_input()
d={"DIGITS":0, "LETTERS":0}
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print "LETTERS", d["LETTERS"]
print "DIGITS", d["DIGITS"]

# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
s = raw_input()
d={"UPPER CASE":0, "LOWER CASE":0}
for c in s:
    if c.isupper():
        d["UPPER CASE"]+=1
    elif c.islower():
        d["LOWER CASE"]+=1
    else:
        pass
print "UPPER CASE", d["UPPER CASE"]
print "LOWER CASE", d["LOWER CASE"]

# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
a = raw_input()
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
n4 = int( "%s%s%s%s" % (a,a,a,a) )
print n1+n2+n3+n4

# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
values = raw_input()
numbers = [x for x in values.split(",") if int(x)%2!=0]
print ",".join(numbers)

# Write a program that computes the net amount of a bank account based a transaction log from console input.
netAmount = 0
while True:
    s = raw_input()
    if not s:
        break
    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation=="D":
        netAmount+=amount
    elif operation=="W":
        netAmount-=amount
    else:
        pass
print netAmount

Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

def putNumbers(n):
    i = 0
    while i<n:
        j=i
        i=i+1
        if j%7==0:
            yield j
for i in reverse(100):
    print i

A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
import math
pos = [0,0]
while True:
    s = raw_input()
    if not s:
        break
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    if direction=="UP":
        pos[0]+=steps
    elif direction=="DOWN":
        pos[0]-=steps
    elif direction=="LEFT":
        pos[1]-=steps
    elif direction=="RIGHT":
        pos[1]+=steps
    else:
        pass
print int(round(math.sqrt(pos[1]**2+pos[0]**2)))

# Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
freq = {}  
line = raw_input()
for word in line.split():
    freq[word] = freq.get(word,0)+1
words = freq.keys()
words.sort()
for w in words:
    print "%s:%d" % (w,freq[w])

# Write a method which can calculate square value of number
def square(num):
    return num ** 2

# Write a function te return cube of a number
def cube(num):
    return num ** 3

# Define a class, which have a class parameter and have a same instance parameter.
class Person:    
    name = "Person"
    def __init__(self, name = None):
        self.name = name
jeffrey = Person("Jeffrey")
print "%s name is %s" % (Person.name, jeffrey.name)
nico = Person()
nico.name = "Nico"
print "%s name is %s" % (Person.name, nico.name)

# Define a function which can compute the sum of two numbers.
def SumFunction(number1, number2):
	return number1+number2

# Define a function that can convert a integer into a string and print it in console.
def printValue(n):
	print str(n)

# Define a function that can convert a integer into a string and print it in console.
def printValue(n):
	print str(n)

# Define a function that can receive two integral numbers in string form and compute their sum and then print it in console.
def printValue(s1,s2):
	print int(s1)+int(s2)

# Define a function that can accept two strings as input and concatenate them and then print it in console.
def printValue(s1,s2):
	print s1+s2

# Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print al l strings line by line.
def printValue(s1,s2):
	len1 = len(s1)
	len2 = len(s2)
	if len1>len2:
		print s1
	elif len2>len1:
		print s2
	else:
		print s1
		print s2
		
# Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".
def checkValue(n):
	if n%2 == 0:
		print "It is an even number"
	else:
		print "It is an odd number"
		
# Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.
def printDict():
	d=dict()
	d[1]=1
	d[2]=2**2
	d[3]=3**2
	print d

# Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.
def printDict():
	d=dict()
	for i in range(1,21):
		d[i]=i**2
	print d
		
# Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the values only.
def printDict():
	d=dict()
	for i in range(1,21):
		d[i]=i**2
	for (k,v) in d.items():	
		print v
		
# Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.
def printDict():
	d=dict()
	for i in range(1,21):
		d[i]=i**2
	for k in d.keys():	
		print k
		
# Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).
def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print li
		
# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.
def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print li[:5]
		
# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list.
def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print li[-5:]
		
# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print all values except the first 5 elements in the list.
def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print li[5:]
		
# Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included). 
def printTuple():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print tuple(li)
		
# With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line. 
tp=(1,2,3,4,5,6,7,8,9,10)
tp1=tp[:5]
tp2=tp[5:]
print tp1
print tp2

# Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10). 
tp=(1,2,3,4,5,6,7,8,9,10)
li=list()
for i in tp:
	if tp[i]%2==0:
		li.append(tp[i])
tp2=tuple(li)
print tp2

# Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No". 
s= raw_input()
if s=="yes" or s=="YES" or s=="Yes":
    print "Yes"
else:
    print "No"

# Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].
li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = filter(lambda x: x%2==0, li)
print evenNumbers

# Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].
li = [1,2,3,4,5,6,7,8,9,10]
squaredNumbers = map(lambda x: x**2, li)
print squaredNumbers

# Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = map(lambda x: x**2, filter(lambda x: x%2==0, li))
print evenNumbers

# Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).
evenNumbers = filter(lambda x: x%2==0, range(1,21))
print evenNumbers

# Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).
squaredNumbers = map(lambda x: x**2, range(1,21))
print squaredNumbers

# Define a class named American which has a static method called printNationality.
class American(object):
    @staticmethod
    def printNationality():
        print "America"
anAmerican = American()
anAmerican.printNationality()
American.printNationality()

# Define a class named American and its subclass NewYorker. 
class American(object):
    pass
class NewYorker(American):
    pass
anAmerican = American()
aNewYorker = NewYorker()
print anAmerican
print aNewYorker

# Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area. 
class Circle(object):
    def __init__(self, r):
        self.radius = r
    def area(self):
        return self.radius**2*3.14
aCircle = Circle(2)
print aCircle.area()

# Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area. 
class Rectangle(object):
    def __init__(self, l, w):
        self.length = l
        self.width  = w
    def area(self):
        return self.length*self.width
aRectangle = Rectangle(2,10)
print aRectangle.area()

# Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
class Shape(object):
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.length = l
    def area(self):
        return self.length*self.length
aSquare= Square(3)
print aSquare.area()

# raise a RuntimeError exception.
raise RuntimeError('something wrong')

# Write a function to compute 5/0 and use try/except to catch the exceptions.
def throws():
    return 5/0
try:
    throws()
except ZeroDivisionError:
    print "division by zero!"
except Exception, err:
    print 'Caught an exception'
finally:
    print 'In finally block for cleanup'

# Define a custom exception class which takes a string message as attribute.
class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg
error = MyError("something wrong")

# Assuming that we have some email addresses in the "username@companyname.com" format, write program to print the user name of a given email address. Both user names and company names are composed of letters only.
import re
emailAddress = raw_input()
pat2 = "(\w+)@((\w+\.)+(com))"
r2 = re.match(pat2,emailAddress)
print r2.group(1)



# Assuming that we have some email addresses in the "username@companyname.com" format, write program to print the company name of a given email address. Both user names and company names are composed of letters only.
import re
emailAddress = raw_input()
pat2 = "(\w+)@(\w+)\.(com)"
r2 = re.match(pat2,emailAddress)
print r2.group(2)

# Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.
import re
s = raw_input()
print re.findall("\d+",s)

# Print a unicode string "hello world".
unicodeString = u"hello world!"
print unicodeString

# Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.
s = raw_input()
u = unicode( s ,"utf-8")
print u

# Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
n=int(raw_input())
sum=0.0
for i in range(1,n+1):
    sum += float(float(i)/(i+1))
print sum

# Write a program to compute: f(n)=f(n-1)+100 when n>0 and f(0)=1
def f(n):
    if n==0:
        return 0
    else:
        return f(n-1)+100
n=int(raw_input())
print f(n)

# Write a program to add an integer and [revious non negative integer
Solution:
def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return f(n-1)+f(n-2)

# Write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.
def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return f(n-1)+f(n-2)
n=int(raw_input())
values = [str(f(x)) for x in range(0, n+1)]
print ",".join(values)

# write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.
def EvenGenerator(n):
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i+=1
n=int(raw_input())
values = []
for i in EvenGenerator(n):
    values.append(str(i))
print ",".join(values)

# write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.
def NumGenerator(n):
    for i in range(n+1):
        if i%5==0 and i%7==0:
            yield i
n=int(raw_input())
values = []
for i in NumGenerator(n):
    values.append(str(i))
print ",".join(values)

# write assert statements to verify that every number in the list [2,4,6,8] is even.
li = [2,4,6,8]
for i in li:
    assert i%2==0

# write a program which accepts basic mathematic expression from console and print the evaluation result.
expression = raw_input()
print eval(expression)

# write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.
import math
def bin_search(li, element):
    bottom = 0
    top = len(li)-1
    index = -1
    while top>=bottom and index==-1:
        mid = int(math.floor((top+bottom)/2.0))
        if li[mid]==element:
            index = mid
        elif li[mid]>element:
            top = mid-1
        else:
            bottom = mid+1
    return index

li=[2,5,7,9,11,17,222]
print bin_search(li,11)
print bin_search(li,12)

# write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.
import math
def bin_search(li, element):
    bottom = 0
    top = len(li)-1
    index = -1
    while top>=bottom and index==-1:
        mid = int(math.floor((top+bottom)/2.0))
        if li[mid]==element:
            index = mid
        elif li[mid]>element:
            top = mid-1
        else:
            bottom = mid+1
    return index

# generate a random float where the value is between 10 and 100 using Python math module.
import random
print random.random()*100

# generate a random float where the value is between 5 and 95 using Python math module.
import random
print random.random()*100-5

# write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.
import random
print random.choice([i for i in range(11) if i%2==0])

# write a program to output a random number, which is divisible by 5 and 7, between 0 and 10 inclusive using random module and list comprehension.
import random
print random.choice([i for i in range(201) if i%5==0 and i%7==0])

# write a program to generate a list with 5 random numbers between 100 and 200 inclusive.
import random
print random.sample(range(100), 5)

# write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.
import random
print random.sample([i for i in range(100,201) if i%2==0], 5)

# write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.
import random
print random.sample([i for i in range(1,1001) if i%5==0 and i%7==0], 5)

# write a program to randomly print a integer number between 7 and 15 inclusive.
import random
print random.randrange(7,16)

# write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".
import zlib
s = 'hello world!hello world!hello world!hello world!'
t = zlib.compress(s)
print t
print zlib.decompress(t)

# write a program to print the running time of execution of "1+1" for 100 times.
from timeit import Timer
t = Timer("for i in range(100):1+1")
print t.timeit()

# write a program to shuffle and print the list [3,6,7,8].
from random import shuffle
li = [3,6,7,8]
shuffle(li)
print li

# write a program to shuffle and print the list [3,6,7,8].
from random import shuffle
li = [3,6,7,8]
shuffle(li)
print li

# write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].
subjects=["I", "You"]
verbs=["Play", "Love"]
objects=["Hockey","Football"]
for i in range(len(subjects)):
    for j in range(len(verbs)):
        for k in range(len(objects)):
            sentence = "%s %s %s." % (subjects[i], verbs[j], objects[k])
            print sentence

# Write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].
li = [5,6,77,45,22,12,24]
li = [x for x in li if x%2!=0]
print li

# By using list comprehension, write a program to print the list after removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].
li = [12,24,35,70,88,120,155]
li = [x for x in li if x%5!=0 and x%7!=0]
print li

# By using list comprehension, write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].
li = [12,24,35,70,88,120,155]
li = [x for (i,x) in enumerate(li) if i%2!=0]
print li

# By using list comprehension, write a program generate a 3*5*8 3D array whose each element is 0.
array = [[ [0 for col in range(8)] for col in range(5)] for row in range(3)]
print array

# By using list comprehension, write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].
li = [12,24,35,70,88,120,155]
li = [x for (i,x) in enumerate(li) if i not in (0,4,5)]
print li

# By using list comprehension, write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].
li = [12,24,35,24,88,120,155]
li = [x for x in li if x!=24]
print li

# With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists.
set1=set([1,3,6,78,35,55])
set2=set([12,24,35,24,88,120,155])
set1 &= set2
li=list(set1)
print li



# With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.
def removeDuplicate( li ):
    newli=[]
    seen = set()
    for item in li:
        if item not in seen:
            seen.add( item )
            newli.append(item)
    return newli
li=[12,24,35,24,88,120,155,88,120,155]
print removeDuplicate(li)

# Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.
class Person(object):
    def getGender( self ):
        return "Unknown"
class Male( Person ):
    def getGender( self ):
        return "Male"
class Female( Person ):
    def getGender( self ):
        return "Female"
aMale = Male()
aFemale= Female()
print aMale.getGender()
print aFemale.getGender()

# write a program which count and print the numbers of each character in a string input by console.
dic = {}
s=raw_input()
for s in s:
    dic[s] = dic.get(s,0)+1
print '\n'.join(['%s,%s' % (k, v) for k, v in dic.items()])

# write a program which accepts a string from console and print it in reverse order.
s=raw_input()
s = s[::-1]
print s

# write a program which accepts a string from console and print the characters that have even indexes.
s=raw_input()
s = s[::2]
print s

# write a program which prints all permutations of [1,2,3]
import itertools
print list(itertools.permutations([1,2,3]))

# Write a program to solve a classic ancient Chinese puzzle:  We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?
def solve(numheads,numlegs):
    ns='No solutions!'
    for i in range(numheads+1):
        j=numheads-i
        if 2*i+4*j==numlegs:
            return i,j
    return ns,ns