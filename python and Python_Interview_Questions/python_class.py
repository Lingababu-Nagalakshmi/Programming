# Python introduction
# --------------------
# Python is a popular programming language..
# It was created by Guido van rossum, and released in 1991...
# It is used for
# ..web development
# ..software development
# ..mathematics
# ..system scripting..
# What can python do ?
# ..python can be used on a server to create web applications..
# ..python can be used to create software workflows...
# ..python can connect database systems...it can also used to read and
# modify files..
# ..python can be used to perform complex mathematics..
# ..python can be used for production ready software development...
# Why python ?
# ------------
# ..python works on different platforms..(windows,Mac,Linux,...etc)
# ..python has a simple syntax similar to english language..
# ..python has syntax that allows programmers to write programs in fewer
# lines..
# ..python runs on an interpreter systems,...excuted
# ..python can be treated in a procedural way, an object oriented way and
# functional way...
# Assignment
# ----------
# ..Differences between procedural way, object oriented way and functional
# way...
# ..python versions python 3.x.... 3.10...october 4th
# ..pycharm ---- download...
# 1..Introduction
# a)Getting started
# b)Variables and literals, python comments
# c)input and output
# d)Type conversion
# e)operators
# 2..Decision making and loop
# a)if..else statement
# b)while loop
# c)for loop
# d)break and continue
# e)pass
# Control flow examples
# 3)Functions
# a)Function
# b)Variable scope and lifetime
# c)Function arguments
# d)Anonymous function
# e)Recursion
# 4)***Collections/Data structures
# ---------------------------------
# a)lists
# b)Tuples
# c)Strings
# d)sets
# e)Dictionary
# 5)Modules and files/File handling
# ---------------------------------
# a)Modules
# b)Files
# c)Directory
# 6)Exception handling
# a)Exception
# b)Exception handling
# c)Custom exceptions
# 7)***Object-oriented programming
# a)Class and object
# b)Constructors
# c)inheritence
# d)Polymorphism
# e)Encapsulation
# f)Namespaces..
# ..python email handling...
# ..Assert() keyword
# Advanced topics
# ----------------
# 1)Iterators
# 2)Generators
# 3)Closures
# 4)Decorators
# 5)python@property
# ..Deep copy and shallow copy
# ..Docstring in pandas...
# Introduction
# -------------
# a)Getting started
# -------------------
# The only way you can get better at programming is by writing code...
# Example
-------
#write a program to print hello world..
print("Hello world")
#write a program sum of two numbers...
a=5
b=3
sum=a+b
print(sum)
b)variables and literals
------------------------
Python variables
-----------------
A variable in programming is used to store data(value)...
For example
a=5
variable 'a' has value 5...
Changing variable values
------------------------
Example
--------
a=5
a=10
print(a)
..we change variable value from a=5 to a=10 manually...
Rules for naming a variables
----------------------------
..A variable name consists of alphabets(a to z) (A to Z) or digits(0 to
9) or an underscore...
..you cannot start a variable name with a digit..
..use underscore if you want to create a variable name having two words..
Example
--------
First_name,second_name,number,number1...
1number---syntax error...
Python Literals
---------------
Literal is a raw data used for representing fixed values....
Three types of literals...
1..Numeric literals
----------------
Three types : Integer,float and complex
Integers -- 1,2,3,0,-1,-2....etc
Float -- 2.3,3.4,8.7..........etc
Complex .. 1.5j,2+3.4j........etc
Binary,hexadecimal and octal systems..
a=0b1011 #binary
b=0o310 #octal
c=0x12c #hexadecimal
2)String Literals
-----------------
A string literal is a sequence of characters surrounded by quotes..
we can use single,double,or triple quotes for a string...
Example
-------
name="Ramya"
name='ramya'
For multiline strings, we use triple quotes..
multiline_string="""This is our
python class"""
3)Boolean literals
-------------------
Two boolean literals : True and False
Note : True and False are case sensitive..
Python comments
----------------
A comment is used to describe what's going on inside a program...
# symbol --- we will start to write a comment..
Example
-------
#This is a comment
c)input and output
-------------------
python provides built-in functions that allows you to output data and
take input from the user...
print() and input()
Python print()
---------------
print() function is used to display data to the standarad output
device(screen)
Example
---------
print("This is the python programming session")
The print() function prints the content inside the paranthesis()..
input()
-------
Take input from the user...
name=input("Enter name:")
print("Hello",name)
d)Type conversion...
---------------------
Convert from one data type to another datat type...
Data types : Integer , string, float..etc..
Two types :
Implicit type Conversion
------------------------
Python automatically converts one data type to another data type..
Example
-------
number_integer=12
number_float=12.3
sum=number_integer+number_float
print(sum)
Type() function
----------------
We can find the type of a variable using type() function..
Example
-------
number_integer=12
number_float=12.3
sum=number_integer+number_float
print(type(sum))
Explicit type conversion
-------------------------
predefine functions like int(),float(),str()..etc to convert to one
datatype to another data type
Example
--------
float_number=1.23455
#converting to integer
integer_number=int(float_number)
print(integer_number)
print(type(integer_number))
#write a program to convert string to int and float..
a='55'
integer_number=int(a)
float_number=float(a)
print(integer_number)
print(float_number)
Assignment
------------
#write a program to convert integer number to float number...
#write a program to convert integer number and float number to string...
e)Operators
------------
An operator is a special symbol that carries arithmetic and logical
computation...
Arithmetic operators
--------------------
Addition,subtraction,multiplication,division...etc
+ operator
----------
x=1
y=2
z=3
result=x+y+z
print(result)
Concatenate two strings
-----------------------
+ operator is used to concatenate two strings..
Example
-------
first_name='ramya'
last_name='sri'
name=first_name+' '+last_name
print(name)
- operator
-----------
a=12
b=9
result=a-b
print(result)
* operator
-----------
a=12
b=9
result=a*b
print(result)
Multiply string
---------------
a='sri'
b=9
result=a*b
print(result)
/ and // operator
------------------
result=14/3
result1=14//3
print(result)
print(result1)
% operator
----------
remainder....
result=14%3
print(result)
**operator
----------
result=2**6
print(result)
Assignment operators
--------------------
= opertaor is used to assign values to variables..
Example
--------
x=100
x=x+5
print(x)
More Assignment operators
-------------------------
+= x+=5 x=x+5
-= x-=5 x=x-5
*= x*=5 x=x*5
/= x/=5 x=x/5
%= x%=5 x=x%5
//= x//=5 x=x//5
**= x**=5 x=x**5
Example
-------
x=100
x+=5 #x=x+5
print(x)
Boolean Operators
------------------
True and False
Example
--------
print(5<6)
print(3<2)
Comparision operators
----------------------
Either True or False
Greater than(>), less than(<), ==Equal to, Not equal to(!=), Greater than
or equa to(>=), less than or equal to(<=)
Example
-------
x=10
y=12
print(x>y)
print(x<y)
print(x==y)
print(x!=y)
print(x>=y)
print(x<=y)
Logical operators
-----------------
and ----- True if both operands are true
Example
--------
print(True and True)
print(True and False)
print(False and True)
print(False and False)
or --- True if one operand is True
Example
---------
print(True or True)
print(True or False)
print(False or True)
print(False or False)
not --- True if the operand is false
print(not True)
print(not False)
2)Decision Making and loop
---------------------------
if..else statement
------------------
if statement
------------
syntax:
if boolean_expression:
statement(s)
boolean_expression evaluates to True the body of if will executed
boolean_expression evaluates to False the body of if statements will
skip...
Example
--------
number=3
if number>2:
print("Number is positive")
print("This is always executed")
if..else statement
-------------------
if boolean expression:
statement(s)
else:
statement(s)
IF the boolean_expression evaluates True the body of if statement is
executed..
if the boolean_expression evaluates False the body of else statement is
executed..
Example
--------
number=3
if number>=0:
print("Number is positive")
print("The body of if is executed")
else:
print("Negative number")
print("The body of else is executed")
if..elif..else
---------------
if boolean_expression:
statement(s)
elif boolean expression:
statement(s)
else:
statement(s)
Example
--------
number=0
if number>0:
print("positive number")
elif number==0:
print("Zero")
else:
print("Negative number")
While Loop
----------
While loop is used to repeat a block of code as long as the
boolean_expression is true..
Syntax:
while boolean_expression:
statement(s)
Example
---------
n=3
i=1
while i<=n:
print("Loop is easy")
i=i+1
Example
--------
# write a program to print sum of natural numbers...
n=10
#initialize sum and count
sum=0
i=1
while i<=n: #1<=10 # True
sum=sum+i # sum=0+1 == sum=1
i=i+1 # 1+1 =2
print("The sum is",sum)
For Loop
--------
for loop in python is used to iterate over a sequenceof objects...
Sequences
----------
strings --- A string is a sequence of characters...
Example
-------
text='python programming'
Lists
-------
A list is a sequence of items seperated by commas and enclosed in square
brackets..
Example
-------
my_list=[2,"text",5.6]
range()
------
range() is used to create a sequence of numbers..
Example
--------
numbers=range(1,6)
Syntax
------
for val in sequence:
statement(s)
Example
-------
languages=['java','python','c++']
for item in languages:
print(item)
Example
---------
numbers=range(1,101)
for item in numbers:
print(item)
Assignment
----------
#write a program to print sum of numbers 1 to 100 by using range()
Example
--------
numbers = range(1,101)
sum=0
for i in numbers:
sum=sum+i // sum+=i
print("sum=",sum)
Break and continue
------------------
python break statement
----------------------
sometimes we may need to terminate the loop immediately without checking
the next expression then we use break statement...
Example
---------
numbers=[1,2,-3,46,78]
for val in numbers:
if val<0:
break
print(val)
Python continue statement
--------------------------
numbers=[1,4,-100,5,-9]
for val in numbers:
if val<=0:
continue
print(val)
print("This is outside loop")
pass statement
--------------
numbers=[1,4,-100,5,-9]
for val in numbers:
pass
print("statement after loop")
...we have a loop or function that is not properly implemented yet, but
we want to implement it in the future..
It cannot have a empty body, passs statement is used..
Assignment
-----------
1..Write a program to find the largest number among three numbers..
2..Write a program to check leap year
3..write a program to generate fibonacci sequence..
0,1,1,2,3,5,8,..........etc
The first two terms are 0 and 1..
n_term=20
#first two terms
n1=0
n2=1
count=0
print("fibonacci sequence upto",n_term)
while count<n_term:
print(n1,end=',')
nth=n1+n2
n1=n2
n2=nth
count=count+1
print()
4..write a progarm to check prime number..
Example
-------
num=504
flag=1
for i in range(2,num):
if(num%i)==0:
print(num,"is not a prime number")
print(i,"times",num//i,"is",num)
flag=0
break
if flag==1:
print(num,"is a prime number")
Functions
----------
Function helps break our program into smaller and modular chunks..
As our program grows larger by larger functions make it organized and
manageable..
How to create a function
-------------------------
def function_name(parameters):
statement(s)
def -- keyword makes the start of the function header..
function_name=unique name given to identify function (simliar to
variables)
parameters (arguments) are used to pass values to function.. They are
optional..
colon : ... mark the end of the functionheader..
return statement --- optional..
Example
-------
def greet(name):
print("Hello",name)
print("What's going on?")
greet('bhuvana') --- function call
Example
--------
# write a program to add two numbers using functions...
def add_numbers(n1,n2):
sum=n1+n2
print("sum=",sum)
num1=5
num2=7
add_numbers(num1,num2)
Return statement
----------------
A function may have optional return statement..
It is used to exit a function and go back to the place from where it is
called..
Example
-------
def add_numbers(n1,n2):
sum=n1+n2
return sum
result=add_numbers(5,7)
print("sum=",result)
Variable scope
---------------
def my_func():
x=10
print("Value inside function",x)
x=20
my_func()
print("Value outside function",x)
Local and global scope
-----------------------
Local variable scope
--------------------
# Write Python 3 code in this online editor and run it.
def my_func():
x=10
my_func()
print(x) #Nameerror...
Function Arguments
------------------
We learned how to define functions and the way to call them..
we also learned a bit about passing arguments to a function...
Example
-------
def greet(name,msg):
"""This funcion greets to the
person with the provided
message"""
print("Hello",name+','+msg)
greet("Mounika","Good Morning!!")
Example
---------
def greet(name,msg):
"""This funcion greets to the
person with the provided
message"""
print("Hello",name+','+msg)
greet("Mounika")
Output
------
Traceback (most recent call last):
File "<string>", line 9, in <module>
TypeError: greet() missing 1 required positional argument: 'msg'
Default arguments
------------------
# Online Python compiler (interpreter) to run Python online.
def greet(name,msg="Good Morning"):
"""This funcion greets to the
person with the provided
message"""
print("Hello",name+','+msg)
greet("Mounika")
greet("Divya")
greet("Bhuvana","How are you")
Anonymous function
------------------
You can define function without name...
This function is called as anonymous function..
Lambda as our keyword...
syntax
-------
lambda arguments:expression
Example
-------
#write a program to perform square of a number
#lambda fuction
square=lambda x:x*x
#function call
result=square(10)
print(result)
Python Recursion
----------------
A function that calls itself is known as a recursive function..
Example
-------
def calc_sum(n):
if n==1:
return 1
else:
return n+calc_sum(n-1)
sum=calc_sum(3)
print(sum)
4)Collections/Data structures
------------------------------
data types : int,float and bool...
Sequences ----
Lists
-----
list is one of the most frequently used and versatile data type in
python...
A list is created by placing elements inside [] square brackets...
Example
-------
numbers=[1,23,44]
How to create a list
--------------------
A list can have any number of items...
And these items may be of different data types like int,float and str...
Example
-------
#empty list
list1 = []
#list of integers
list1=[1,2,3,4]
#list with mixed datatypes
list1=[1,3.4,"strain"]
#Nested_list
.. A list which contians another list is called nested list..
my_list=["Hello",[1,2,3],["a"]]
Access Elements from a List
---------------------------
We can use the index operator[] to access item in a list..
Example
--------
numbers=[1,22,10,100,3.33]
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])
..We can acces first element using numbers[0],the second element
numbers[1]........
..Index starts from 0 (not 1).... so list having 5 elements will have an
index from 0 to 4...
..If you try to access an item outside the list you will get an
IndexError..
Negative Indexing
-----------------
python allows negative indexing for its sequences..
The index of -1 refers to the last item, -2 refers the second last item
and so on...
Example
--------
numbers=[1,22,10,100,3.33]
print(numbers[-1])
print(numbers[-2])
print(numbers[-3])
print(numbers[-4])
print(numbers[-5])
print(numbers[-6])
Slicing of a list
-----------------
We will learn to access a range of items.. This is done by using slicing
operator (:)
Example
-------
my_list=['p','y','a','b','c','h']
#elements 3rd to 5th
print(my_list[2:5])
#elements 4th to end
print(my_list[3:])
#elements begining to 4th
print(my_list[:3])
#elements begining to end
print(my_list[:])
Change items of a list
----------------------
Lists are mutable... we can add,update,delete...
We use = operator to change an item or range of items in a list...
Example
-------
odd=[2,4,6,8]
#change the 1st item
odd[0]=1
print(odd)
#change range of elements (2nd to 4th items)
odd[1:4]=[3,5,7]
print(odd)
Add elements in a list
----------------------
To add a single item in a list we use append() method..
To add multiple items in a list we use extend() method...
Example
-------
odd=[1,3,5]
odd.append(2)
print(odd)
odd.extend([9,11,13])
print(odd)
using + and * operators
------------------------
we can also use + operator to combine two lists..This is called
concatenation..
If you need to repeat items of a list we use * operator
Example
--------
odd=[1,3,5]
print(odd+[7,9,11])
print(['a','b']*3)
insert()
---------
odd=[1,5]
odd.insert(1,3)
print(odd)
Delete items from a list
------------------------
we can delete one or more items from a list using the keyword del...
It can even delete the entire list...
Example
--------
my_list=[1,2,3,4,5,6]
del my_list[2]
print(my_list)
del my_list[1:5]
print(my_list)
del my_list
print(my_list)
List copy
---------
you can use = operator to copy from one list to another...
Example
-------
list1=[1,2,3]
list2=list1
print(list2)
Loop through a list
-------------------
for loop..
for fruit in ['apple','banana','mango']:
print("I like",fruit)
Nested lists
------------
A list can have another list in it...
Example
---------
my_list=[1,2,[3,4,5]]
print(my_list[0])
print(my_list[2][0])
print(my_list[2][1])
print(my_list[2])
Tuples
-------
A tuple is similar to a list...
The difference between the two is that we cannot change the elements of a
tuple once it is assigned.. but in list elements can be changed..
A tuple is created by placing all elements inside parantheses ()...
A tuple can have any number of items and they can be different data
types...
Example
-------
my_tuple=() #empty tuple
my_tuple=(1,2,3,4) #tuple having integers
my_tuple=(1,"hello",3.4) #mixed datatypes
my_tuple=('cat',[8,4],(1,2,3)) #nested tuple
..We can create a list in a tuple too...
my_tuple=3,4.6,'dog'
print(my_tuple)
...Better use parantheses when you practice tuple...
Creating Tuples with one item
-----------------------------
t1=("hello")
print(type(t1))
t2=("hello",)
print(type(t2))
t3="hello",
print(type(t2))
..Having one item within parantheses is not enough..
We will need a trailing comma to indicate that it is a tuple...
Accessing Tuple Elements
-------------------------
Similar to lists, we use the index operator [] to access tuple elements..
Example
-------
my_tuple=('a','b','c','d')
we can access the first item with my_tuple[0] and second element
my_tuple[1] and so on...
my_tuple=('a','b','c','d')
print(my_tuple[0])
print(my_tuple[1])
Negative indexing
-----------------
python allows negative indexing for its sequences...
The index -1 refers to the last item -2 the second last item and so on..
Example
--------
my_tuple=('a','b','c','d')
print(my_tuple[-1])
print(my_tuple[-2])
Slicing
-------
We will learn how to access a range of items.. This is done by using the
slicing operator (:)
Example
-------
my_tuple=('p','y','t','h','o','n')
#elements from 2nd to 4th
print(my_tuple[1:4])
#elements from begining to 2nd
print(my_tuple[:-4])
#elements 6th to end
print(my_tuple[5:])
#elements from begining to end
print(my_tuple[:])
Changing Tuple elements
------------------------
tuples are immutable..
this means that elements cannot be changed once it has been assigned...
Example
-------
my_tuple=(1,2,3)
my_tuple[0]=0
output
-------
Traceback (most recent call last):
File "<string>", line 4, in <module>
TypeError: 'tuple' object does not support item assignment
using + and * operators
------------------------
we can use + operator to combine two tuples.. This is called
concatenation...
If you need to repeat items of a tuple we can use * operator..
Example
--------
odd=(1,3,5)
print(odd+(7,9,11))
letters=('a','b')
print(letters*3)
Deleting a tuple
----------------
we cannot delete items of a tuple..
Example
-------
my_tuple=(1,2,3)
del my_tuple[0]
output
-------
Traceback (most recent call last):
File "<string>", line 5, in <module>
TypeError: 'tuple' object doesn't support item deletion
other tuple operators
----------------------
we can check whether an item exists in a tupe or not using in keyword..
Example
-------
my_tuple=('a','p','p','l','e')
print('a' in my_tuple)
print('b' in my_tuple)
Iterating through a tuple
-------------------------
for loop is used to iterate each item in a tuple...
Example
---------
for name in ('divya','sindhu','mounika'):
print("Hello",name)
Python Strings
---------------
A string is a sequence of characters..
Computers donot allow characters they deal only with numbers(binary)...
Internally it is stored and manipulated at a combination of 0's and 1's..
The conversion of character to a number is called encoding and the
reverse process is decoding...
How to create strings
----------------------
Strings can be created by enclosing characters inside a single quotes or
double quotes..
Triple quotes can be used in python for multiline strings...
Example
--------
my_string='hello'
print(my_string)
my_string="Hello"
print(my_string)
my_string='''Hello'''
print(my_string)
my_string="""Hello,welcome to python
world, where we discuss"""
print(my_string)
Access characters in a string
--------------------------------
Similar to lists and tuples we can access characters in a string by using
the index operator[]..
Example
-------
my_string='hello'
print(my_string[0])
print(my_string[1])
Indexing starts with 0 not 1...
Negative indexing
-----------------
The index of the last character is -1 and second last character is -2 and
so on.....
Example
-------
my_string='python'
print(my_string[-1])
print(my_string[-2])
Slicing a string
------------------
we can access a range of characters in a string using slicing operator
(:)
Example
-------
my_string='python'
#2nd to 4th characters
print(my_string[1:4])
#begining to 4th character
print(my_string[0:4])
#begining to 4th character
print(my_string[:4])
Deleting a string
-----------------
Strings are immutable...
Its not possible to change or delete characters of a string...
Example
---------
my_string='python'
del my_string[0]
output
------
Traceback (most recent call last):
File "<string>", line 5, in <module>
TypeError: 'str' object doesn't support item deletion
Python string operations
-------------------------
Concatenation of two strings
-----------------------------
we use + operator to combine or concatenate two strings..
Example
--------
first_name='ramya'
second_name='sri'
name=first_name+ ' '+second_name
print(name)
Repeat two strings
------------------
we cab repeat a string using * operator..
Example
-------
my_string='hello'
print(my_string*3)
Iterating through a string
--------------------------
we can iterate through a sequence using for loop..
Example
-------
write a program to count the number of 'l' in a string..
count=0
for letter in 'Hello world':
if(letter=='l'):
count+=1
print(count,"letters found)
Check whether substring exists
-------------------------------
in keyword
Example
-------
result='a' in 'Hello'
print(result)
result='o' in 'hello'
print(result)
Escape sequence
---------------
He said, " what's there ?" ---Syntax error...
Example
-------
print('''He said,"what's there?"''')
Python sets
-------------
A set is a unordered collection of items..
Every element is unique (no duplicates)...
Creating sets
-------------
A set is created by placing all the items inside curly braces {} and
seperated by commas..
Example
---------
my_set={1,2,3}
print(my_set)
#set of mixed datatypes
my_set={1,2,"hello",3.4,(1,2,3)}
print(my_set)
Let's try to create a set with duplicate elements..
Example
-------
my_set={1,2,1,3,1,4,2,3}
print(my_set)
Add and update sets
--------------------
sets are mutable..
But since they are unordered , indexing has no meaning...
we cannot access or change elements of a set using indexing or slicing..
set doesnot support it
we can add single element using add() method and multiple elements using
update() method..
The update() method can take tuples,lists,strings or other sets as its
arguments..
Example
-------
my_set={1,3}
print(my_set)
my_set.add(2)
print(my_set)
my_set.update([4,5,6])
print(my_set)
Removing elements from a set
-----------------------------
To remove elements from a set we can either use remove() or discard()
methods..
The only difference between the two is that , discard(), if the item is
not exists in the set it remains unchanged..
But remove() will raise an error ..
Example
-------
my_set={1,2,3,4,5,6}
my_set.discard(4)
print(my_set)
my_set.discard(7)
print(my_set)
my_set.remove(7)
print(my_set) #Error :keyerror
Set methods : pop() and clear()
-------------------------------
The pop() method removes a random element from a set and returns it..
Example
-------
my_set={1,2,3,4,5,6}
result=my_set.pop()
print(my_set)
print(result)
The clear() removes all elements from a set
Example
--------
my_set={1,2,3,4,5,6}
my_set.clear()
print(my_set)
python set operations
----------------------
union, intersection, difference and symmetric..
Set union
---------
The union of two sets A and B is a set of all elements from both sets..
It is performed using | operator..
same can be performed by using union() method..
Example
--------
A={1,2,3}
B={3,4,5,6}
result=A|B
print(result)
result=B.union(A)
print(result)
Set Intersection
----------------
The intersection of two sets A and B is a set of all elements that are
common in both sets..
It is performed using & operator..
Same can be performend by using intersection()..
Example
---------
A={1,2,3}
B={2,3,4,5,6}
result=A&B
print(result)
result=B.intersection(A)
print(result)
Set Difference
--------------
The difference of set B from A is a set of elements that are only in A
but not in B..
It is performed by using A-B ..
Same can be performed by using difference()..
Example
-------
A={1,2,3}
B={2,3,4,5,6}
result=A-B
print(result)
result=B-A
print(result)
result=A.difference(B)
print(result)
Set Symmetric Difference
-------------------------
The symmetric difference between two sets A and B is a set of elements in
both A and B except those are common in both..
It is perfromed using ^ operator ... (caret)
Same can be performed by using symmetric_difference()
Example
--------
A={1,2,3}
B={2,3,4,5,6}
result=A^B
print(result)
result=A.symmetric_difference(B)
print(result)
Iterating through a set
------------------------
for loop...
Example
--------
for letter in set('apple'):
print(letter)
Check if an element exists
--------------------------
in keyword..
Example
-------
my_set=set("apple")
print('a' in my_set)
print('w' in my_set)
Python Dictionary
-----------------
A dictionary is a unordered collection of items ...
key:value pairs..
How to create a dictionary
----------------------------
A dictionary is as simple as placing items inside curly braces {},
seperated by commas..
A item in a dictionary has a key and the corresponding value expressed as
a pair.. key:value
While values can be of any data type and can repeat, keys must be
unique..
Example
-------
#empty dictionary
my_dict={}
#dictionary with integer keys
my_dict={1:'apple',2:'ball'}
#dictionary with mixed keys
my_dict={name:'divya',1:[22,3,4]}
Creating Dictionaries using dict()
----------------------------------
A dictionary can also be created using dict()
Example
-------
my_dict=dict({1:'apple',2:'ball})
#creating dictionary from a sequence
my_dict=dict([(1,'apple'),(2,'ball')])
print(my_dict)
Access Dictionary Elements
---------------------------
A dictionary has a key:value pairs as elemenents..
To access the value of an element we use its key...
Example
--------
person={'name':'sindhu','age':26}
person_name=person['name']
print(person_name)
person_age=person['age']
print(person_age)
Access value using get()
------------------------
We can also access the value of an element using the get() method..
Example
-------
person={'name':'sindhu','age':26}
person_name=person.get('name')
print(person_name)
person_age=person.get('age')
print(person_age)
Change and add dictionary elements
----------------------------------
Dictionary is mutable..
we can add items or change the value of existing items using =
operators..
Add Element to a dictionary
---------------------------
person={'name':'sindhu','age':26}
#adding element
person['city']='hyderabad'
print(person)
update element to a dictionary
------------------------------
we can update an element in similar way to how we add an element
Example
-------
person={'name':'sindhu','age':26}
#updating age
person['age']=19
print(person)
Remove Dictionary Item
----------------------
To remove a single item from a dictionary we can use pop() method..
The method removes an item with the provided key and retuurns the value..
Example
-------
person={'name':'ramya','age':25}
#removing elements using pop()
result=person.pop('age')
print('value removed',result)
print('updated dictionary',person)
use of del in a dictionary
----------------------------
The del keyword can be used to delete an individual items..
It can be also used to delete entire dictionary..
Example
-------
person={'name':'ramya','age':25}
#deleting items using del keyword
del person['age']
print(person)
#delete entire dictionary
del person
print(person)
Iterating thorugh a dictionary
------------------------------
for loop...
Example
-------
squares={1:1,2:4,3:9,4:16}
for i in squares:
print(squares[i])
check if a key exists
-----------------------
in keyword
Example
-------
squares={1:1,2:4,3:9,4:16}
print(1 in squares)
print(5 in squares)
print(4 in squares)
# write a porgram to caluclate number of characters in a string..
string="Python programming language"
count=0
for i in range(0,len(string)):
if(string[i]!=''):
count=count+1
print("Total number of characters in a string:"+str(count))
# write a program to count the frequency of each character in the
string...
Create an empty dictionary to store the character as key and frequency of
character as value..
d=dict()
Loop over the string to get one character at a time..
for i in string:
use get() the function checks the character is present in the dictionary,
if present it returns the value of character then add one to it..
If the character is not present then the get() function returns 0, that
is second parameter add 1 to it and put the character into the
dictionary...
d[i]=d.get(i,0)+1
Finally print the dictionary with characters as keys and values....
print(d)
string=input("Enter the string:")
d=dict()
for i in string:
d[i]=d.get(i,0)+1
print(d)
output
------
Enter the string:python programming langugae
{'p': 2, 'y': 1, 't': 1, 'h': 1, 'o': 2, 'n': 3, ' ': 2, 'r': 2, 'g': 4,
'a': 3, 'm': 2, 'i': 1, 'l': 1, 'u': 1, 'e': 1}
Assignment
----------
# write a python program to count the frequency of each character in the
string using "in" operator..
What is the correct python file extension ?
.py
In the following code n is assigned a/an---- value?
n='5'
.. string.. quotes
what will be the output of the following code?
a=3.44
b=3
result=a+b
print(result)
print(type(result))
... float value .... 6.44
What is the output of the following code?
str='abc'
print(str*3)
...abcabcabc
what is the output of the following code?
str1='4'
str2='3'
result=str2+str1
print(result)
..34
What is the output of the following code?
my_range=range(1,5)
a=0
for val in my_range:
a=a+1
print(a)
..4
Modules and files
------------------
Python Modules
--------------
Modules refers to a file containing python statements and definitions..
we use modules to break down large program into small and manageable and
organized files..
modules provide reusability of code..
we can define our most used functions in a module and import it...
instead of copying their definitions into different programs..
Create and import module
------------------------
To create a module , write python code in a file and save .py extension..
Let's create a file named example.py and save the following code..
def add(a,b):
"""This program adds two
numbers"""
result=a+b
return result
Import module
--------------
To use this module, we need to import it...
Let's create a new file main.py and import the example module..
import example
output=example.add(20,30)
Python standard modules
-----------------------
math is one of the standard modules..
Built in method : dir()
-----------------------
we can use dir() function to find out the list of valid attributes
defined inside module..
Example
-------
import math
print(dir(math))
output
------
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos',
'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb',
'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp',
'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma',
'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt',
'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan',
'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh',
'sqrt', 'tan', 'tanh', 'tau', 'trunc']
Example:math module
--------------------
import math
x=2.25
y=3
#square root of x
result=math.sqrt(x)
print(result)
#x is raised to the power of y
result=math.pow(x,y)
print(result)
#value of pi
print(math.pi)
#value of e
print(math.e)
Import with renaming
--------------------
we can rename the module during import..
Example
--------
import math as m
print("The value of pi is",m.pi)
from..import statement
----------------------
we can import specific names from a module without importing the module
as a whole...
Example
-------
from math import pi,e
print(pi)
print(e)
Python files
-------------
A file is a named location on disk to store related information..
It is used to permanently store data in memory...
when we want to read from or write to a file we need to open file first..
when we are done it need to be closed,...
1..open a file
2..Read or write (perform operations)
3..close file
How to open a file
------------------
Python has a built in function open() to open afile..
Example
-------
f=open("test.txt") #open a file in current directory
f=open("C:\Users\Ramyasri.X.Kapalavai\OneDrive - Quest
Diagnostics\Desktop\Ramya\pythonclass.txt") #specifying full path
Specifying mode during file open()
----------------------------------
We can use modes while opening a file...
'r' -- open a file for reading
'w' -- open a file for writing.. create a new file if it does not
exist..
'a' -- open a file for appending at the end of the file.. creates a new
file if it does not exist..
'x' --- open a file for exclusive creation..if the file already exists,
the operation fails..
't' -- open a file in text mode..(default)
'b' -- open a file in binary mode, used for images and binary files..
'+' -- open a file for updtaing (reading and writing)...
Example
--------
f=open("python class.txt") #equivalent to 'r' or 'rt'
f=open("python class.txt",'w') #write in text mode
f=open("img.png",'r+b') # read and write in binary mode..
specifying Encoding type in open()
----------------------------------
When working with files in text mode, it is highly recommended to use
encoding type..
f=open("python class.txt", mode='r', encoding='utf-8')
..in windows it is 'cp1252' but in linux it is 'utf-8'...
Close a file
-------------
when we complete our file operations to the file we need to close the
file properly..
closing a file will free up the resources that were tied in the file
using python close() method..
Example
--------
f=open("python class.txt")
#perform file operations
f.close()
try..finally
------------
try:
f=open("python class.txt")
#perform file operations
finally:
f.close()
How to write a file
---------------------
In order to write into a file in python we need to open a file it in 'w',
append 'a'..
writing a string or sequence of bytes is done using write()...
Example
-------
f=open("python class.txt",'w')
f.write("my first file\n")
f.write("This file\n")
f.write("contains python class\n")
f.close()
output
-------
my first file
This file
contains python class
How to read files
-----------------
To read a file in python we must open the file in reading mode..
There are various methods available for this purpose..
we use read(size) method to read the size of the parameter of data...
Example
-------
f=open("python class.txt",'r')
#read the first 4 data
print(f.read(4))
output
------
my f
#read the next 4 data
print(f.read(4)
irst..
#read the rest and till end of file
print(f.read())
This file
contains python class..
'\n' -- returns a newline..
seek() and tell() methods
--------------------------
we can change our current file cursor (position) using seek() method..
similarly tell() method returns the current position of cursor..
Example
--------
f=open("python class.txt",'r')
#read in the rest ad till end of file
f.read()
#get the current file cursor
print(f.tell())
#bring file cursor to initial position
f.seek(0)..
Read file line by line
----------------------
we can read a file line-by-line using for loop..
This is both efficient and fast..
Example
-------
f=open("python class.txt",'r')
for line in f:
print(line)
readline() method..
-------------------
we can use the readline() method to read individual lines of a file..
This method reads a file till the newline..
Example
-------
file.py
f=open("C:\Users\Ramyasri.X.Kapalavai\OneDrive - Quest
Diagnostics\Desktop\Ramya\python class.txt",'r')
print(f.readline()) #my first file
print(f.readline()) #This file
Python directory
----------------
A directory or folder is a collection of files and subdirectories..
If there are large number of files to handle in your python progaram you
can arrange the code with different directories to make things more
manageable..
python has the 'os' module which provides us with many useful methods to
work with directories..
Get current directory
---------------------
present working directory -- getcwd() method defined in the os module..
import os
current_directory=os.getcwd()
print(current_directory)
List of directories and files
------------------------------
All files and subdirectories inside a directory can be known using
listdir() method..
Example
-------
import os
folder_path='C:\Users\Ramyasri.X.Kapalavai\OneDrive - Quest
Diagnostics\Desktop\Ramya'
result=os.listdir(folder_path)
print(result)
Create a new directory
----------------------
we can make a new directory using mkdir() method..
Example
-------
import os
os.mkdir('test')
Renaming a directory
--------------------
Rename() method can be used to rename a directory or file..
Example
-------
import os
os.rename('test','test1')
Moving files/directories
--------------------------
if we want to move files/directories from one place to another we use
rename() method..
Example
-------
import os
os.rename('test','Documents')
Removing directory or files
---------------------------
A file can be removed using remove() method...
Similarly rmdir() method removes and empty directory...
Example
-------
import os
os.listdir()
['test','python.txt']
os.remove('python.txt')
os.listdir()
['test']
os.rmdir('test')
os.listdir()
[]
Exception Handling
-------------------
Python Exceptions
-------------------
Errors occur at runtime(syntax errors,name error, indentation error,type
error)... These errors are known as exceptions...
Built-in exceptions
-------------------
When a file we try to open does not exist FileNotFoundError..
Dividing a number with zero , ZeroDivisionError
Module try to import is not found ImportError..
Assignment
-----------
python.org -- website
built-in exceptions page ----
Interview questions
---------------------
1.. Introduction of python..
2..what is python ? what are the benefits of using python?
3..what is a dynamically typed language ?
4..what is a interpreted language ?
5..what is scope in python ?
6..what are lists and tuples ? what is the key difference between these
two ?
7..what are common-built in data types in python ?
8..what is slicing in python ?
9..what are modules in python?
10..what are global,protected,private attributes in python ?
11.what is the use of self in python?
12..what is __int__() ?
13..what is break, continue and pass in python ?
14.. How is memory managed in python ?
15..what is an exception?
16..why we use raise keyword?
17..what is try clause and except clause.. when to use?
18..What is custom exceptions?
19..when we use try..finally clause?
Python Exception Handling
-------------------------
When the exception occurs it causes the current process to stop and
passes it to the calling function until it is handled..
Catching Exceptions
--------------------
In python exceptions can be handled using a try statement..
An operation which can raise an exception placed inside a try clause and
the code get handled the exception is written using except clauses..
Example
-------
def findReciprocal(value):
try:
print("value:",value)
r=1/value
print("The reciprocal of value is",r)
except:
print("You cannot find reciprocal of",value)
findReciprocal("Hello")
findReciprocal(2)
Catching specific exceptions
------------------------------
def findReciprocal(value):
try:
print("value:",value)
r=1/value
print("The reciprocal of value is",r)
except ValueError:
print("You got value error")
except ZeroDivisionError:
print("You got a zero division error")
except:
print("Haandling all errors")
findReciprocal("Hello")
findReciprocal(2)
findReciprocal(0)
Raising exceptions
------------------
raise keyword --- we can forcefully raise some errors/exceptions..
Raise --- optional..
Example
----------
a=int(input("Enter a positive integer:"))
try:
if a<=0:
raise ValueError("Not a positive number")
print("You entered",a)
except ValueError as ve:
print(ve)
try..finally
------------
finally -- optional
try..finally uses mainly in file operations..
Example
-------
try:
f=open("test.txt","r")
#perform file operations
finally:
f.close()
Custom/userdefined Exceptions
-------------------------------
users can define such exceptions by creating a new class..
Example
-------
class Error(Exception):
"""Base class for other
exceptions"""
pass
class ValueTooSmallError(Error):
"""Raise when the input value is too
small"""
pass
class ValueTooLargeError(Error):
"""Raise when the input value is too
large"""
pass
Assignment coding questions
---------------------------
1). Write a program to reverse an integer in Python
2). Write a program in Python to check whether an integer is Armstrong
number or not.
3). Write a program in Python to check given number is prime or not.
4). Write a program in Python to print the Fibonacci series using
iterative method.
5). Write a program in Python to print the fibonacci series using
recursive method.
6). Write a program in Python to check whether a number is palindrome or
not using iterative method.
7). Write a program in Python to check whether a number is palindrom or
not using recursive method.
8). Write a program in Python to find greatest among three integers.
9). Write a program in Python to check if a number is binary?
10). Write a program in Python to find sum of digits of a number using
recursion?
11). Write a program in Python to swap two numbers without using third
variable?
12). Write a program in Python to swap two numbers using third variable?
13). Write a program in Python to find prime factors of a given integer.
14). Write a program in Python to add two integer without using
arithmetic operator?
def add(a,b):
#iterating till there is no sum
while(b!=0)
#set of bits a and b
sum=a&b
#sum of bits of a and b where at least one of the bits is not set
a=a^b
#adding bits given to the required sum
b=sum<<1
return a
print(add(15,32))
..def add(a,b)
for i in range(1,b+1):
a=a+1
a=add(10,32)
print(a)
..def add(a,b):
if(b==0):
return a
else:
return add(a^b,(a&b)<<1)
15). Write a program in Python to find given number is perfect or not?
16). Python Program to find the Average of numbers with explanations.
17). Python Program to calculate factorial using iterative method.
18). Python Program to calculate factorial using recursion.
19). Python Program to check a given number is even or odd.
20). Python program to print first n Prime Number with explanation.
21). Python Program to print Prime Number in a given range
22). Python Program to find Smallest number among three.
Object - Oriented programming
------------------------------
Class and Objects
-----------------
Python is an object oriented programming..
Procedural language, functional language, object oriented programming..
.... object is a simply collection of data(variables or methods or
functions)...
...Class --- blueprint of object..
...class house
contains doors,floors,windows etc..
An object is also called an instance of class and the process of creating
object is called instaniation..
How to defined a class
-----------------------
class --- keyword
class My NewClass:
#methods and attributes
pass
Creating an object
-------------------
To access the attributes of a class we use objects instantiated it..
Example
--------
class MyClass:
a=10
def func(self):
return "hello"
#instantiate an object
obj=MyClass()
print(obj.a)
print(obj.func())
Creating Multiple objects
-------------------------
class MyClass:
a=10
def func(self):
return "hello"
obj1=MyClass()
obj2=MyClass()
print(obj1.a)
print(obj1.a)
obj1.a=11
obj2.a=1000
print(obj1.a)
print(obj2.a)
Class objects
-------------
when we define a class in python an object of the same class name is
automatically created..
Example
-------
class MyClass:
a=10
def func(self):
return "hello"
print(MyClass.a)
Example
-------
class Number:
def add(self,a,b):
return a+b
def multiply(self,a,b):
return a*b
#instantiate an object
n1=Number()
sum=n1.add(2,3)
print(sum)
product=n1.multiply(2,5)
print(product)
Assignment
----------
..what is the use of self parameter?
The self parameter is a reference to the current instance of the class,
and it is used to access variables, methods that belongs to the class..
class MyClass:
def __init__(abc,name,age):
abc.name=name
abc.age=age
def func(MyObject):
print("Hello my is "+MyObject.name)
obj=MyClass("Sindhu",25)
obj.func()
Constructors
-------------
__init__() function .... also called as constructor..
__ ---- class functions that begin with double underscore are called
special functions..
Example
-------
class MyClass:
def __init__(self,p1=0,p2=0):
self.a=p1
self.b=p2
obj=MyClass(2,3)
print(obj.a,obj.b)
obj1=MyClass()
print(obj1.a,obj1.b)
Assignment
----------
Write a program to find distance from origin..
class Point(object):
def __init__(self,x=0,y=0):
self.x=x
self.y=y
def distance(self):
return(self.x**2+self.y**2)**0.5
p1=Point(6,8)
distance=p1.distance()
print(distance)
Deleting Attributes of an object
--------------------------------
you can delete attributes of an object using del statement...
Example
-------
class Point(object):
def __init__(self,x=0,y=0):
self.x=x
self.y=y
p1=Point(6,8)
print(p1.x,p1.y)
#deleting attribute y..
del p1.y
print(p1.x)
print(p1.y)
If we want to access deleted attribute will face AttributeError..
Deleting objects
----------------
You can also delete the objects itself using del statement..
Example
--------
class Point(object):
def __init__(self,x=0,y=0):
self.x=x
self.y=y
p1=Point(6,8)
print(p1)
del p1
print(p1)
If we want to access deleted object will face NameError..
Python Inheritence
------------------
Inheritence is a powerful feature in object oriented programming
language..
It referes to defining a new class with little or no modification to an
existing class..
The new class is derived class(child class) and the one from which it
inherits is called base class(parent class)
Grandfather(parent class)
....
Father... (Derived class)
....
you ... (Derived class)
Syntax
------
class BaseClass:
#Body of the baseclass
class DerivedClass(BaseClass):
#Body of the derived class
Why inheritence?
-----------------
class Polygon:
def __init__(self,no_of_sides):
self.n=no_of_sides
self.sides=[]
for i in range(no_of_sides):
self.sides.append(0)
def input_sides(self):
for i in range(self.n):
self.sides[i]=float(input("Enter side"+str(i+1)+":"))
#inheriting Triangle from polygon class
class Triangle(Polygon):
def __init__(self):
Polygon.__init__(self,3)
def find_area(self):
a,b,c=self.sides
#caluclate the semi-perimeter
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("The area of the triangle is",area)
t=Triangle()
t.input_sides()
t.find_area()
Method overriding and method overloading
----------------------------------------
Method overloading is an example of compile time polymorphism..
In this more than one method of the same class shares the same method
name having different signatures..
Method overloading is used to add more of the method behaviours and there
is no need of more than one class for method overloading..
Example
-------
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Function to take multiple arguments
def add(datatype,*args):
#if datatype is int
#intialize with 0
if datatype=='int':
answer=0
#if datatype is string
#intaialize with ''
if datatype=='str':
answer=''
#Traverse trhough the arguments
for x in args:
#This will do addition if the arguments are int..
#This will do concatenation if the arguments are str
answer=answer+x
print(answer)
#integer
add('int',5,6)
#string
add('str','Hi','Python')
Assignment
----------
write an example for method overloading by using class...
Method overriding
-----------------
Method overriding is an example of runtime polymorphism..
In this the specific implementation of the method that is already
provided by parent class is provided by the child class..
It is used to change the behaviour of existing methods and there is need
for at least two classes for method overriding..
Inheritence always required as it done between parent class and child
class..
Example
-------
class A:
def func1(self):
print('feature1 of class A')
def func2(self):
print('feature2 of class A')
class B(A):
#Modified function that is already exists in class A
def func1(self):
print('Modified feature-1 of class A by class B')
def func3(self):
print('feature-3 of class B')
#create instance
obj=B()
#call the override function
obj.func1()
Assignment
----------
what are the differences between method overloading and method
overriding..
isinstance() and issubclass()
-----------------------------
Two built-in functions..
isinstance()---function returns True if the object is an instance of
class..
issubclass() -- used to check class inheritence..
Example
-------
class polygon:
pass
class Triangle(polygon):
pass
t=Triangle()
print(isinstance(t,Triangle))
print(isinstance(t,polygon))
print(isinstance(t,int))
print(isinstance(t,object))
print(issubclass(polygon,Triangle))
print(issubclass(Triangle,polygon))



Polymorphism
--------------
The word polymorphism means having many forms..
In programming, polymorphism means the same function name but with
different signatures being used for different types..
Example
---------
#polymorphism with inheritence
class Bird:
def intro(self):
print("There are many types of birds")
def fly(self):
print("Most of the birds can fly but some cannot")
class sparrow(Bird):
def fly(self):
print("sparrows can fly")
class ostrich(Bird):
def fly(self):
print("ostriches cannot fly")
obj_bird=Bird()
obj_spr=sparrow()
obj_ost=ostrich()
obj_bird.intro()
obj_bird.fly()
obj_spr.intro()
obj_spr.fly()
obj_ost.intro()
obj_ost.fly()
#polymorphism example
class India():
def capital(self):
print("New Delhi is the capital of India")
def language(self):
print("Hindi is the most spoken language of india")
def type(self):
print("Inida is a developing country")
class USA():
def capital(self):
print("washington DC is the capital of US")
def language(self):
print("English is the most spoken language")
def type(self):
print("USA is developed country")
obj_ind=India()
obj_usa=USA()
for country in(obj_ind,obj_usa):
country.capital()
country.language()
country.type()
Encapsulation
-------------




Encapsulation in python describes the concept of building data and
methods within a single unit..
when you create a class it means you are implementing encapsulation..
Example
-------
class Employee:
#constructor
def __init__(self,name,salary,project):
#data memebers
self.name=name
self.salary=salary
self.project=project
#method
#to display employee details
def show(self):
print("Name: ",self.name,"salary: ",self.salary)
def work(self):
print(self.name,'is working on',self.project)
emp=Employee('rama',10000,'NLP')
emp.show()
emp.work()
..using encapsulation we can hide an objects internal representation from
the outside..
This is called data hiding/Information hiding..
Also encapsulation allows us to restrict accessing variables and methods
directly to prevent from data modification by creating private data
members and methods in a class...
Access modifiers in python
Encapsulation can be achieved by declaring the datamembers and methods of
a class either as private or protected..
But in python we dont have access for modifiers like public,private and
protected..
we can use single underscore and double underscores..
public member : Accessible anywhere from outside class..
All member variables of the class are by default public..


Example
--------
class Employee:
#constructor
def __init__(self,name,salary):
#data memebers
self.name=name
self.salary=salary
#method
#to display employee details
def show(self):
print("Name: ",self.name,"salary: ",self.salary)
emp=Employee('rama',10000)
emp.show()
private member : Accessible within class..
to define a private member we have to add two underscores as a prefix at
the start of the variable names..
Example
--------
class Employee:
#constructor
def __init__(self,name,salary):
#public data memeber
self.name=name
#private data member
self.__salary=salary
emp=Employee('rama',10000)
print('salary:',emp.__salary)
In the above example, the salary is a private variable..
As we know we can't access private variable from the outside class..
Instance method
---------------
Accessing private members outisde a class using instance(public) method..
Example
-------
class Employee:
#constructor
def __init__(self,name,salary):
#public data memeber
self.name=name
#private data member
self.__salary=salary
#public method
def show(self):
print("Name:",self.name,"salary:",self.__salary)
emp=Employee('rama',10000)
emp.show()
protected member : Accessible within the class and its subclass..
To define protected member prefix the member variable with a single
underscore(_)
protected data members are used when you implement inheitence and want to
allow data members access to only child class...
Example
--------
class Company:
def __init__(self):
#protected member
self._project='NLP'
class Employee:
#constructor
def __init__(self,name):
#public data memeber
self.name=name
Company.__init__(self)
#public method
def show(self):
print("Employee name:",self.name)
#accessing protected members
print("working on project:",self._project)
emp=Employee('rama')
emp.show()
print("project:",emp._project)
Getters and setters in python
------------------------------
To implement proper encapsulation in python we use getter and setter
methods..
use the getter method to access data members and the setter methods to
modify data members..
when we want to avoid direct access to private members..
To add validation logic for setting a value..
Example
-------
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class Student:
def __init__(self,name,age):
self.name=name
self.__age=age
#getter method
def get_age(self):
return self.__age
#setter method
def set_age(self,age):
self.__age=age
stud=Student('rama',15)
#retreiving age by using getter
print("Name:",stud.name,stud.get_age())
#changing age using setter
stud.set_age(17)
print("Name:",stud.name,stud.get_age())
Namespaces
----------
Name(identifier)
NAme is simply a name given to objects..
Everything in python is an object..
NAme is a way to underly the object..
For example when we do the assignment a=2 here 2 is an object stored in
memory and a is the name we assosciate with it...
We can get the address in RAM of some object through built in function
id()
Example
------
a=2
print('id(2)=',id(2))
print('id(a)=',id(a))
Namespace
---------
A namespace is a collection of names..
A namespace containing all built-in names is created when we start the
python intreprter and exists as long as we don't exists..
This is the reason that built-in namespaces like
id(),int(),print(),input()...etc are always available to us from any part
of the program..
Each module creates its own global namespaces...
Assignment
-----------
what is a local namespace, global namespace and built-in namespaces..
Advanced Python
----------------
Iterators
---------
Iterators are everywhere in python...
For example when we implement for loops ...
Iterator in python is simply an object that can be iterated upon..
An object which will return data one element at a time....
special methods : __iter__() and __next__()
The iter() function which in turn calls __iter__() methods returns an
itertor from them...
Iterating through a iterator
----------------------------
we can use next() function to manually iterate through all the items of
an iterator...
when we reach at the end of the iteration there is no more data to be
returned, it will raise StopIteration..
Example
-------
my_list=[4,7,0]
#get an iterator using iter()
my_iter=iter(my_list)
print(next(my_iter))
print(next(my_iter))
print(my_iter.__next__())
print(next(my_iter))
Assignment
----------
Write a program using iterators....
Infinite iterators
------------------
Example
-------
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class InfIter:
"""Infinite iterator to return
all
odd numbers"""
def __iter__(self):
self.num=1
return self
def __next__(self):
num=self.num
self.num+=2
return num
i=InfIter()
a=iter(i)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
# so on
Generators
-----------
Python generators are a simple way of creating iterators..
A generator is a function that returns an object which can iterate
over..(one value at a time)
How to create a generator
-------------------------
If a function contains one yield statement , it may contain other yield
or return statements...it becomes a generator function..
Both yiled and return wil return some value from a function...
The difference is that while a return statement terminates a function
entirely, yield statement pauses the function saving all its states and
later continues from there on successive calls...
..Generatorfunction contains one or more yield statements...
..when called, it returns an object (itertor) but does not start
execution immediately...
..methods like __iter__() and __next__() are implemented automatically...
so we can iterate through next()
..Finally when the function terminates , StopIteration
Example
--------
def my_gen():
n=1
print("This is printed first")
yield n
n+=1
print("This is printed second")
yield n
n+=1
print("This is printed third")
yield n
a=my_gen()
next(a)
next(a)
next(a)
next(a)
Using generators with for loop
-----------------------------
def my_gen():
n=1
print("This is printed first")
yield n
n+=1
print("This is printed second")
yield n
n+=1
print("This is printed third")
yield n
#using for loop
for item in my_gen():
print(item)
