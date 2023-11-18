#Decarator


def decor(func):

    def inner(name):

        if name == "Lingababu":

            print("Hi Good Morning",name)

        else:
            func(name)

    return inner


def wish (name):

    print("Hi Good afternoon",name)

wish("Lingababu")
wish("Nagalakshmi")

#-----------------------------------------------------------------------------------------
#Dataclasess and its types
'''Data clasess in python maily used for the no need to use the __init__ longer'''
'''for this we need to import @dataclass decarator'''
from dataclasses import dataclass
@dataclass()
class Person():
    name: str
    age: int
    height: float
    email: str

joe = Person('Joe', 25, 1.85, 'joe@dataquest.io')

joe.age = 35
print(joe)

#-------------------------------------------------------------------------------------------
from dataclasses import dataclass
@dataclass()
class Person():
    name: "Lingababu"
    age: 31
    height: 6.2
    email: "lingababu555@gmail.com"

joe = Person('Joe', 25, 1.85, 'joe@dataquest.io')

joe.age = 35
print(joe)

#------------------------------------------------------------------------------------------
from typing import Tuple

@dataclass
class Person():
    name: str
    age: int
    height: float
    email: str
    house_coordinates: Tuple

print(Person('Joe', 25, 1.85, 'joe@dataquest.io', (40.748441, -73.985664)))

#----------------------------------------------------------------------------------------------
#Multithreading and multiprocessing and its limitations

#Multithreading points

'''1)In Multiple threading having multiple threads assigned to single process

2)they run concurrently and parrell to each other

3)These threads share the same meomory space with in the Parent process because Increase the performance

4)Mainly we are using this for I/O bounded applications

5)Multithreading uses common address space for all threads

6)Multithreading is quick and requires few resources

7)A process is an independent instance executed in a processor core.

8)threads do share the meomory space

9)Threads are lighter and cause less overhead. Also, because they share the same memory inside a process, it is easier, faster, and safer to share data.

10)Concurrent execution means that two or more tasks are progressing at the same time.

10)threads are scheduled by the GIL.

#Multiprocessing points


1)A process is an independent instance executed in a processor core.

2)Processes do not share the same memory space,

3)Processes execution is scheduled by the operating system

5)Parallel execution implies that two or more jobs are being executed simultaneously.'''



#Fuctions
def func1(*a):
    return sum(a)
from functools import reduce
print(func1(2,3,4,5,6,7,8,9))
x=[1,2,3,4,5,6,7]
z=list(map(lambda y:y**2,x))
print(z)
a=list(filter(lambda y:y%2!=0,x))
print(a)
b=reduce(lambda x,y:x-y,x)
print(b)

#class declaration with constractor

class Student:


    def __init__(self,name,age,school,bus):

        self.name=name
        self.age=age
        self.school=school
        self.bus=bus

    def display(self):

        print("My name is",self.name,"with having",self.age)

    def second_info(self):

        print("My school is",self.school,"and having the bus",self.bus)


s1 = Student("Lingababu",31,"GMR","Benz")

s1.display()
s1.second_info()

#class declaration with out constractor 

class Student:


    def display(self,name,age):
        self.name=name
        self.age=age

        print("My name is",self.name,"with having",self.age)

    def second_info(self,school,bus):
        self.school=school
        self.bus=bus

        print("My school is",self.school,"and having the bus",self.bus)


s1 = Student()

s1.display("Lingababu",31)
s1.second_info("GMR","Benz")

#creating class with default parameter

class Student:


    def display(self):
        self.name="Lingababu"
        self.age=32

        print("My name is",self.name,"with having",self.age)

    def second_info(self):
        self.school="GMR"
        self.bus="Benz"

        print("My school is",self.school,"and having the bus",self.bus)


s1 = Student()

s1.display()
s1.second_info()


#Inheritances



#single     #simple

class A:
    def m1(self):
        print("Parent method")
class B(A):
    def m2(self):
        print("Child method")
b = B()
b.m1()

#multiple   #many to one

class A:
    def m1(self):
        print("Parent1 method")
class B():
    def m1(self):
        print("Parent2 method")
class C(B,A):
    def m1(self):
        print("Child method")
c = C()
c.m1()


#multilevel # one to one

class A:
    def m1(self):
        print("Parent1 method")
class B(A):
    def m1(self):
        print("Parent2 method")
class C(B):
    def m1(self):
        print("Child method")
c = C()
c.m1()

#hybrid     #combination of all[multiple+multilevel+single]
class A:
    def m1(self):
        print("Parent1 method")
class B(A):
    def m1(self):
        print("Parent2 method")
class C(B):
    def m1(self):
        print("Child method")
class D(C,B):
    def m1(self):
        print("Child1 method")

d= D()
c.m1()

#cyclic     #
class A(B):
    def m1(self):
        print("Parent1 method")
class B(A):
    def m1(self):
        print("Parent2 method")

#Hirechy    #single to many
class A:
    def m1(self):
        print("Parent1 method")
class B(A):
    def m1(self):
        print("Parent2 method")
class C(A):
    def m1(self):
        print("Child method")
c = C()
c.m1()
    

#super keyword  #method and constractor

class Student:

    def __init__(self,name,school):

        self.name = name
        self.school =school

    def frist_method(self):
        print("Hi my name is",self.name,"working in the school",self.school)
        
class Student1(Student):

    def __init__(self,name,school,age,bus):

        super().__init__(name,school)
        self.age=age
        self.bus=bus

    def frist_method1(self):

        super().frist_method()
        print("Hi Her name with",self.age,"and her school",self.bus)

stu = Student1("Lingababu","GMR",32,"BENZ")
stu.frist_method1()
#mro
print("---------------------------------------mro-------------------")
class A:
    def m1(self):
        print("Parent1 method")
class B():
    pass
class C(B,A):
    pass
c = C()
c.m1()

#shallow copy and deep copy

''' Shallow and Deep copy should be take it in nested lists only'''
#Shallow copy
import copy
x = [[1,2],[3,4],[5,6]]

y = copy.copy(x)

y[0][0] = "A"

print(x)
print(y)

#Deep copy

import copy
x = [[1,2],[3,4],[5,6]]

y = copy.deepcopy(x)

y[0][0] = "A"

print(x)
print(y)

#call by value and call refrence

''' Call by refrence mainly we can seen in mutable[ objects[List,set,dictionary] will occupie same meomory location'''

def M1(x):

    print(x)
    x.append(3)
    x.extend([4,5,6])
    x.remove(5)
    print(x)
    print(id(x))

y=[1]
M1(y)
print(y)
print(id(y))

#Call by value
'''Call by value only we can apply to Immutable Objects [float,string,Int] will occur will at different meomory location'''
def IM(x):

    print(x)
    x+=10
    print(x)
    print(id(x))

y=5
IM(y)
print(y)
print(id(y))

#How will concatenate using magic methods
#context mangers and its advantanges
#generators

def gene():

    yield 'A'
    yield 'B'
    yield 'C'
    yield 'D'

g = gene()

print(next(g))
print(next(g))
print(next(g))
print(next(g))
#print(next(g))
#Pickling and unpickling
'''Pickling is the process through which a Python object hierarchy is converted into a byte stream. To serialize an object hierarchy, you simply call the dumps() function.

    Unpickling is the inverse operation. A byte stream from a binary file or bytes-like object is converted back into an object hierarchy. To de-serialize a data stream, you call the loads() function.'''

'''pickle.HIGHEST_PROTOCOL − The highest protocol version available. Integer value.

pickle.DEFAULT_PROTOCOL − The default protocol version used for pickling. Integer value. Currently the default protocol is 4'''

import pickle

# Input Data
my_data = { 'BMW', 'Audi', 'Toyota', 'Benz'}

# Pickle the input
with open("demo.pickle","wb") as file_handle:
   pickle.dump(my_data, file_handle, pickle.HIGHEST_PROTOCOL)

# Unpickle the above pickled file
with open("demo.pickle","rb") as file_handle:
   res = pickle.load(file_handle)
   print(my_data) # display the output
   print(type(res))

#how will get,change,delete and modify from dictionary

x = {'A':2,'B':1,'C':5,'E':3,'H':4}
print(x['A'])
print(x.get('A'))
print(x.setdefault('C',6))
print(x)
x['C'] = 'Lingababu'
print(x)
del x['C']
print(x)
#how to get max element from dictionary
x = {'A':2,'B':1,'C':5,'E':3,'H':4}
y= max(sorted(x, key = lambda a : x[a]))
print(y)

#how to get how to sort the dictionary by keys
x = {'A':2,'B':1,'C':5,'E':3,'H':4}

y= dict(sorted(x.items()))   #{'A': 2, 'B': 1, 'C': 5, 'E': 3, 'H': 4}
print(y)
##how to get how to sort the dictionary by values
x = {'A':2,'B':1,'C':5,'E':3,'H':4}
y= dict(sorted(x.items(), key = lambda item : item[1]))
print(y)                     #{'B': 1, 'A': 2, 'E': 3, 'H': 4, 'C': 5}
#what is data_abstraction
print("------------------------------------------------------------")
#using multiple things in single step

l = list(range(1,11))
y=map(lambda x:x**2 if x%2 ==0 else x**3, l)
print(y)
from abc import ABC,abstractmethod

class Parent(ABC):

    def common_fn(self):
        print("Im in common method of parent")
    @abstractmethod
    def abs_fn(self):
        pass

class Child1(Parent):
    def abs_fn(self):
        print('abstract method of child1')


class Child2(Parent):
    def abs_fn(self):
            print('abstract method of child2')

c2 = Child2()
c2.abs_fn()
#what is Encapsulation
'''Encapsulation is combaing of the data and methods is called Encapsulation'''

class Person:

    def m1(self):
        self.a ="nucleous" #public variable
        self._a ="atom"    #protected variable
        self.__a ="molecule" #privite variable

p1 = Person()
#print(p1.a)
#print(p1._a)
#print(p1.__a)
#prime number
n= int(input("Enter the number"))

if n < 1 :
    print("Its not a prime number")

elif n == 1:
    print("Its not a prime number")

elif n > 1 :

    for i in range(2, n):

        if n%i==0:
            print("Its not a prime number")
            break

    else:
        print("Its a prime number")

else:
    print("Its not a prime number")


#how to remove the duplcates

x='aaabbbcccdddd'
x.split()
b=['w','w','w','w','w','r','r','r']
y=[]
for i in b:
    if i not in y:
        y.append(i)
print(y)


#how to remove repeated items from the string
a='aaabbbcccdddd'
b=['w','w','w','w','w','r','r','r']
d=dict()

for i in b:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
#how to get diamond shape ussing python code
#How will you get the key from nested dictionary
#How to get value from the nested list

print("-----------------------------working with regular expressions-----------")

import re
s="learning python is very Easy"
result = re.search("^easy",s,re.IGNORECASE)
if result != None:
    print("Matched")
else:
    print("Not Matched")


'''x=919059422776

import re

result = re.fullmatch('(0|91)?[7-9][0-9]{9}',x)

if result != None:
    print("Matched")'''



#How to get the email ID

'''import re
s=input("Enter the mail ID :")
result = re.fullmatch('\w[a-zA-Z0-9_.]*@gmail.com',s)
if result != None:
    print("Matched")
else:
    print("Not matched")'''
#How to get the phone number using re
'''x=+919059422776
import re
result = re.fullmatch('(0|91)?[7-9][0-9]{9}',x)
if result != None:
    print("Matched")

else:
    print("Not matched")'''
#how get specified value from string using re
#match---------------------------------------
'''match re.match() searches only from the beginning of the string
 a match of substring is found somewhere in the middle of the string, it returns none. '''
'''import re
txt = "The rain in Spain"
x = re.match("ai", txt)
print(x)'''
#search--------------------------------------
'''match re.match() searches only from the beginning of the string
 a match of substring is found somewhere in the middle of the string, it returns none.'''
import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)
#fullmatch
'''re.fullmatch() is that re.match() matches only at the beginning but re.fullmatch() tries to match at the end as well.'''
import re

txt = "The rain in Spain"
x = re.fullmatch("ai", txt)
print(x)
#findall nothing but search but its gives in list['ai','ai']
''' but it will return the output in the list format'''
import re

txt = "The rain in Spain"
x = re.fullmatch("ai", txt)
print(x)

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

txt = "The rain in Spain"
x = re.findall("ai", txt) #['ai','ai']
print(x)

#split()

'''it will split the function but its output list format'''

#sub

'''it will sub in the selected place only'''
 
#how exception handling using classes

try:

    x=int(input("Enter the value:"))
    y=int(input("Enter the value:"))

    print(x/y)

except ZeroDivisionError as e:
    print("We cannot divide by zero",e)

else:
    print("it will go to the next block if there is no exception")

finally:

    print("For cleaning activity we are using this")

#how to create the file and read and write the content to the file

'''\n Indiacte the new line'''
'''write()	:Writes the specified string to the file
   writelines()	:Writes a list of strings to the file'''

with open ('test1.txt' ,'w') as f:
    f.write("See you soon!\n")
    f.write("Good morning Lingababu")

with open('test1.txt','r') as f:
    data=f.read()
    print(data)
    count=0
    for i in data:
        if i == 'Good morning Lingababu':
            count+=1
    print(count)
#Context managers
    
'''Context managers are basically used for the many users uses the resources
    but they can not close the files when we are try to open those files we can os error'''
'''with statement are basically used for the context manager for file handling'''
#local,global,nonlocal variable
'''local and global variable we can use it normal functions'''
# declare global variable
#message = 'Hello'
def greet():
    # declare local variable
    message = 'Lingababu'
    print('Local', message)

greet()
#print('Global', message) #NameError: name 'message' is not defined
#Non local variable
'''nonlocal variable we using in nested functions'''
''' for whose variable local or global Scope not defined then non local scope will come''' 

def Outer():

    message = 'local'

    def inner():
        nonlocal message
        message ='nonlocal'

        print('inner',message)

    inner()
    print('Outer',message)

Outer()
#How to reverse the list using Inbuilt methods

#method-1

# input list
lst = [10, 11, 12, 13, 14, 15]
l = []  
for i in lst:
    l.insert(0, i)
print(l)

#method-2

# Input list
my_list = [4, 5, 6, 7, 8, 9]
reversed_list = []
for i in range(len(my_list)-1, -1, -1):
    reversed_list.append(my_list[i])
print(reversed_list)

#How to reverse the list without using Inbuilt methods

#for list
def reverse_list(l):
    return [l[i] for i in range(len(l)-1, -1, -1)]
a=[1,2,3,4,5,6,7,8,9]
print(reverse_list(a))

#for string
# Function to reverse a string
def reverse(string):
    string1 = [string[i] for i in range(len(string)-1, -1, -1)]
    return "".join(string1)
 
s = "Geeksforgeeks"
 
print("The original string  is : ", s)
 
print("The reversed string(using reversed) is : ", reverse(s))

#self
'''Self is an instance of a class or an object in Python. It is included as the first parameter.
It helps differentiate between the methods and attributes of a class with local variables.'''

#monkey patching
'''the term monkey patch refers to dynamic (or run-time) modifications of a class or module.
In Python, we can actually change the behavior of code at run-time.'''

#Name spaces
'''Scope resolution LEGB rule In Python
In Python, the LEGB rule is used to decide the order in which the namespaces are to be searched for scope resolution.
The scopes are listed below in terms of hierarchy(highest to lowest/narrowest to broadest):'''

#Local(L): Defined inside function/class
#Enclosed(E): Defined inside enclosing functions(Nested function concept)
#Global(G): Defined at the uppermost level
#Built-in(B): Reserved names in Python builtin modules
print("------------------factorial of a number--------------")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(10))

#fibnocial sequence:

def fib (n):

    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n-2)+fib(n-1)
a=20
print(fib(a))

#Difference between == and is operator

'''== is an operator that tests the equality
   is is an operator that tests for identity.

Two objects can have equal values without necessarily being identical (i.e. having the same memory address).

Remember that a is b is syntactic sugar for id(a) == id(b)'''

#When shouldn't you use the assert statement?
'''The assert statement is useful for internal testing and sanity checks.
However, it shouldn’t be used to perform data validation or error handling
because it’s generally disabled in production code for performance reasons.'''

#Using of Zip and Enumerate function

x=['A','B','C','D','E']
y=[1,2,3,4,5]

for x,y in zip(x,y):
    print(x,y)
    
x=['A','B','C','D','E']


for index,x in enumerate(x):
    print(index,y)

#iterable examples "list ,set ,tuple ,dictionary"



#iterate are applying on the iterables
''' we have two iterators
 iter -------yhis is for intialization for iterator object
 next -------this will returns the next value from iterable object'''
string = "GFG"
ch_iterator = iter(string)
 
print(next(ch_iterator))
print(next(ch_iterator))
print(next(ch_iterator))

a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
z= zip(a,b,c)
print(list(z))  #[(1, 4, 7), (2, 5, 8), (3, 6, 9)]

a = [1,2,3]
b = [4,5,6]

z=dict(zip(a,b))
print(z)   #{1: 4, 2: 5, 3: 6}

x=["Name","age"]
y=["Lingababu",30]
z=dict(zip(x,y))
print(z)  #{'Name': 'Lingababu', 'age': 30}

#what is anngstrom number
new_number = int(input("Enter the number:"))

val1=list(map(int,str(new_number)))

val2=list(map(lambda y:y**3,val1))

if (sum(val2) == new_number):
    print("Its a armstrong number ")

else:
    print("Its not a armsstorng number")
    


#what Anagrams

num1 = input("Enter the value")
num2=  input("Enter the value")


if sorted(num1) == sorted(num2):

    print("Both are anagrams")

else:
    print("Both not are anagrams")

#scope resolution in python


#LEGB Rule in python

    #Local
    #Enclosed
    #Global
    #Builtin


'''def outer_func():

    b=20
    global a
    a=a+10

    print(a)


    def inner_func():

        nonlocal b
        b=b+2



        print("The b value is",b)

    inner_func()


outer_func()'''





#Counting Vowels in a Given Word


vowel = ['a','e','i','o','u']

word = 'programming'
count=0

for char in word:

    if char in vowel:

        count+=1
print(count)

#Counting No Vowels In a Given Word

vowels=['a','e','i','o','u']

word= 'sortware engineer'

count=0
for char in word:
    if char not in word:

        count+=1

print(count)

#Counting the number of Occurance of character


word = "python"

character = 'p'

count=0

for letter in word:

    if letter == character:

        count+=1

print(count)


#find the middle number number from the list


num_list = [1,2,3,4,5,6,7,8,9,10]


mid_ele = int((len(num_list)/2))

print(num_list[mid_ele])



#convert list of elements into string



list1 = ['a','c','f','t','y','b']

string1 = ''.join(list1)

print(string)
print(type(string1))

#Adding two list elements together


lst1 =[1,2,3]

lst2 =[4,5,6]


res_lst = []

for i in range(0, len(lst1)):

    res_lst.append(lst1[i]+lst2[i])

print(res_lst)



#Comparing two are anagrams or not


str1 = "Listen"

str2 = "Silent"



str1 = list(str1.upper())

str2 = list(str2.upper())

str1.sort(),str2.sort()

if (str1 == str2 ):

    print("True")

else:

    print("False")



#Counting white spaces in astring

string = "P  r orgramm in g"


print(string.count(' '))



#Counting the Digits letters and Spaces in a string


import re


name ='Python is 1'

digitCount = re.sub("[^0-9]","",name)
letterCount = re.sub("[^a-zA-Z]","",name)
spaceCount = re.findall("[ \n]",name)


print(len(digitCount))
print(len(letterCount))
print(len(spaceCount))

#Counting special Characters in a string

import re

spChar ='!@#$%^&*()'

count = re.sub('[\w]+','',spChar)
print(len(count))


#Remove the all white spaces in a string

import re

string = 'C O D E'

result = re.sub('[\s]+','',string)
print(len(result))

#Building a Pyramid in python

floors = 3

h = 2*floors-1

for i in range(1,2*floors,2):

    print('{:^{}}'.format('*'*i,h))


#randmise the elements from the list

from random import shuffle

lst = ['Python','is','easy']

shuffle(lst)

print(lst)


#How will check whetehr year is leep or not


def LeapYear(year):

    if (year % 400 == 0) or(year % 100 != 0) and (year % 4 == 0):

        print("Given year is a leap year")


    else:

        print("The Given year is not leap year")

Year = int(input("Enter the year to whether check leap year or not"))

LeapYear(Year)

#Swapping two variables in python


num1 = int(input("Enter the frist variable : "))

num2 = int(input("Enter the second Variable : "))

num3 = int(input("Enter the second Variable : "))
print(num1)
print(num2)
print(num3)
num1 , num2,num3 =num3, num2 ,num1

print(num1)
print(num2)
print(num3)


#write a programm to dispaly the calendor

import calendar

year = int(input("Enter the yaer:  "))
month = int(input("Enter the month: "))


print(calendar.month(year,month))

print("----------------working with padding----------------------")

input_list = [1, 123, 1234, 12345]

output_list = []

for num in input_list:

    num_str = str(num)

    padded_num = num_str.zfill(6)
    output_list.append(padded_num)

print(output_list)

#write a programm with Inheritance with Dataabstraction

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.name)  # Output: Buddy
print(dog.make_sound())  # Output: Woof!

print(cat.name)  # Output: Whiskers
print(cat.make_sound())  # Output: Meow!


#Unpacking the tuple


x = [1, 2, 3, 4, 5, (6), 7, 8]
new = []
for e in x:
    if isinstance(e, tuple):
        new.append(e)
    else:
        new.append(e)
print(new)


#Sorting the List without using any Inbuilt methods
s = [-5, -23, 5, 0, 23, -6, 23, 67]
nl = []
for i in range(len(s)):
    a = min(s)
    nl.append(a)
    s.remove(a)
print(nl)




print("-----------------with out print using the return using ------------")
def sep_items(l):
    
    even=[]
    odd=[]
    
    for i in l:
        if i%2 ==0:
            even.append(i)
            
        
        else:
            odd.append(i)
            
    return even,odd
    #print ("Then odd items list",odd)          
    #print ("The even items list",even)
x=eval(input("Enter the Input:"))
a,b=sep_items(x)
print("Even list",a)
print("Odd list",b)

print ("-------------------seperating even and odd numbers from the list with Print-------")
def sep_items(l):
    
    even=[]
    odd=[]
    
    for i in l:
        if i%2 ==0:
            even.append(i)
            
        
        else:
            odd.append(i)
            
    
    print ("Then odd items list",odd)          
    print ("The even items list",even)
x=eval(input("Enter the Input:"))
sep_items(x)


# property                Recursion           Iteration

# Defination      Function calls itself   A set of instractions

# Apllications    For functions           For loops

# Code size       small code size         Large Code size

# Time            Very high time          Low time Complexicity

# Space           More space              Less space

# meomory         more meomory            less meomory



#Recursion

def countdown(n):

    if n <=0:

        return 'Blastoff'

    else:
        return n
        countdown(n-1)

countdown(3)


#print("------------multiple nestded dictionary into single dictionary")

def flatten_list(lst):
    flattened = []
    for item in lst:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)
    return flattened

l1 = [1, 2, [3, 4], 5, [6, 7, 8, 9], [10, [11, 12, 13, [14, 15]]]]
flattened_list = flatten_list(l1)

print(flattened_list)


#we are finding max element from repeated element from list
from collections import Counter

test = [1, 2, 3, 9, 2, 7, 3, 5, 9, 9, 9]

count_dict = Counter(test)
max_count = max(count_dict.values())

test = [1, 2, 3, 9, 2, 7, 3, 5, 9, 9, 9]

count_dict = {}
for num in test:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

max_count = max(count_dict.values())

#we are finding max element from repeated element from list
test = [1, 2, 3, 9, 2, 7, 3, 5, 9, 9, 9]

max_count = max(test.count(x) for x in test)


#How to print the Pyrimd 

def print_diamond(height):
    for i in range(height):
        print(" " * (height - i - 1) + "*" * (2 * i + 1))

# Example usage
print_diamond(5)

#How to prepare the Diamond

def print_diamond(height):
    for i in range(height):
        print(" " * (height - i - 1) + "*" * (2 * i + 1))
    
    for i in range(height-2, -1, -1):
        print(" " * (height - i - 1) + "*" * (2 * i + 1))

# Example usage
print_diamond(5)


#how to add the two list using the lambda

y =[12,23,32,22]

p =[5,10,15,20]
z = list(map(lambda i,j:i*j,y,p))

print(z)  #[60, 230, 480, 440]

#squaring the dictionay values

x={'a':2,'b':3,'c':4}

y={i:j**2 for i,j in x.items()}
print(y)

#if dictionary having the two keys then find the third dictionary
D1 = {'A': 15, 'B': 40}
D2 = {'B': 20, 'C': 70}

D3 = {**D1, **D2}

for key in D1.keys() & D2.keys():
    D3[key] = D1[key] + D2[key]
print(D3)

#How to the multiply the two values from the dictionary 
D1 = {'A': 15, 'B': 40}
D2 = {'B': 20, 'C': 70}

D3 = {**D1, **D2}

for key in D1.keys() & D2.keys():
    D3[key] = D1[key] * D2[key]
print(D3)


#Status codes of particular Rest_API

#Information(1XX)



#Success(2XX):

# 200 OK
# 201 Created
# 204 No Content

#Redirection(3XX):

# 301 Moved Permanently

# 302 Found

# 304 Not Modified


#Client Error(4XX):

# 400 Bad Request

# 401 Unauthorised request

# 403 Forbidden


#Server Error(5XX)

# 500 Internal server Error

# 503 Server Unavaliable


#when your passing 3 parameters from the list when passing the argument

def probability_Checking(x, lst):
    out_put = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            for k in range (j+2, len(lst)):
                if lst[i] + lst[j] +lst[k] == x:
                    out_put.append([lst[i], lst[j], lst[k]])
    return out_put

x=int(input("Enter the number :"))
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(probability_Checking(x, lst))

#when your passing 2 parameters from the list when passing the argument
def probability_Checking(x, lst):
    out_put = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
                if lst[i] + lst[j] == x:
                    out_put.append([lst[i], lst[j]])
    return out_put

x=int(input("Enter the number :"))
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(probability_Checking(x, lst))


#Keyword arguments
def add_sum(**x):

    return max(x.values())

print(add_sum(a=10,b=20,c=30,d=40,e=50))


#it will takes arguments in the  dictionary format[**x]
def add_sum(**x):

    return sum(x.values())

a={'a':10,'b':20,'c':30,'d':40}
print(add_sum(**a))    #dictionary format it will take the arguments


#it will takes arguments in the  tuple format[*x]
def add_sum(*x):

    return sum(x)

a=(20,10,20,40,50)
print(add_sum(*a))     #tuple format it will take the arguments







def cheaking_security(l):

    valid = [2000, 500, 100, 50, 20, 10]
    total = 0


    for i in l:

        if not i[0].isdigit():

            raise Exception ("It should contain the digits only")

        if not i[1:4].isalpha():

            raise Exception ("It should contain the alphabets only")

        if int(i[4:]) not in valid:

            raise Exception ("Invaid denomination :Last 4Characters")


        total+=int(i[4:])
    return total
        
input_l = ['1BEX2000','4PIM0500','6BIO0020','1SJJ0010','9ACD0100']
try:

    total=cheaking_security(input_l)
    print("Total sum",total,"ruppess")

except ValueError as e:

    print("Error:",str(e))






#for post the request in this we need the [url,pay_load,file_path]

import request
def send_post_request(url,payload,file_path):
    reponse=requests.post(url, json=payload)
    if response.status_code == 200:
        with open('file_path','w') as file:
            file.write(response.text)
        print("Response saved to file:",file_path)
    else:
        print("Request failed with status code:",response.status_code)
#Example
url = "https://api.example.com/endpoint"
payload={"key":"value1","key2":"value2"}
file_path ='response.json'



#for get the request in this we need the [url,file_path]
import requests
def send_get_request(url, file_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, 'w') as file:
            file.write(response.text)
        print("Response saved to file:", file_path)
    else:
        print("Request failed with status code:", response.status_code)

# Example usage
url = "https://api.example.com/endpoint"
file_path = "response.json"
send_get_request(url, file_path)





#for patch the request in this we need the [url,payloadfile_path]

import requests
def send_patch_request(url, payload, file_path):
    response = requests.patch(url, json=payload)
    if response.status_code == 200:
        with open(file_path, 'w') as file:
            file.write(response.text)
        print("Response saved to file:", file_path)
    else:
        print("Request failed with status code:", response.status_code)
# Example usage
url = "https://api.example.com/endpoint"
payload = { "key1": "value1","key2": "value2"}
file_path = "response.json"



#x='aaabbbcc' to '3a3b2c'
from itertools import groupby
input1 = 'aaabbbcccddd'
gr = groupby(input1)
ls = ''.join([v + str(len(list(k))) for v, k in gr])
print(ls)




#Convert binary number into integer
binary_string="01010101"
decimal_number = int(binary_string,2)
print(decimal_number)


#Convert integer into dbinary number
decimal_number = 5
binary_string = bin(decimal_number)[2:]
print(binary_string)

#How to reverse the number into reverse order

n = 294389374
reversed_n = 0

while n > 0:
    reversed_n = (reversed_n * 10) + (n % 10)
    n = n // 10

print(reversed_n)

#Check the pattrens for checking whether corrector not

def check_pattern(s):
    stack = []
    opening = "({["
    closing = ")}]"
    pairs = {")": "(", "}": "{", "]": "["}
    
    for char in s:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if len(stack) == 0 or stack[-1] != pairs[char]:
                return False
            stack.pop()
    
    return len(stack) == 0


S1 = "({[]})"
S2 = "}([])}"
S3 = "})[](}"

print(check_pattern(S1))  # True
print(check_pattern(S2))  # False
print(check_pattern(S3))  # False

#Difference between is and ==

#1) is to check the identity and should have same meomory address
#2)== to check the equality.

a=[1,2,3,4,5]

b=a

c = a[:]
print(b)

# it will check for equality
print(a == b)#True

print(a is b)#True

print(a == b)#True
# it will check for identity and equality means should have same meomory address
# after copying it will occupies different meomory address

print(a is c)#false

#1)== is for value equality. It's used to know if two objects have the same value.
#2)is is for reference equality. It's used to know if two references refer
#                       (or point)to the same object, i.e if they're identical.
#Two objects are identical if they have the same memory address.

#pandas
#------------------------------------------------------
#what is syntax for the dataframe

#pandas.DataFrame( data, index, columns, dtype, copy)


#how to create the dataframe add the new column and modify the existing column
#how will you convert txt to csv
#how will you convert txt to excell
#how will you convert txt to tsv
#How would you iterate over rows in a DataFrame in Pandas?
#How are iloc() and loc() different?
#How can you sort the DataFrame?
#How can you find the row for which the value of a specific column is max or min?
# Compare the Pandas methods: map(), applymap(), apply()
#How do you split a DataFrame according to a boolean criterion?
#Is it a good idea to iterate over DataFrame rows in Pandas?
#Name the advantage of using applymap() vs apply() method
#What is the difference(s) between merge() and concat() in Pandas?
