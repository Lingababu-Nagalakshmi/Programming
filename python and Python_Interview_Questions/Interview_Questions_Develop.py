#Decarators


def decor(func):

    def inner(name):

        if name == "Lingababu":

            print("Hi Good morning!",name)

        else:
            func(name)

    return inner

@decor
def wish(name):

    print("Hi Good evening",name)

wish("Lingababu")
wish("Nagalakshmi")

#dictionary


x ={'A':2,'B':3,'C':4,'D':1,'E':5}

y={'F':8,'G':7,'H':6,'I':9,'J':10}

z = dict(zip(x,y))
print(z)

#sort by value
x ={'A':2,'B':3,'C':4,'D':1,'E':5}


w= dict(sorted(x.items(),key=lambda item:item[1]))
print(w)

#sort by key

#method-1
mykeys = list(y.keys())
mykeys.sort()

sorted_dict = { i: y[i] for i in mykeys }
print(sorted_dict)

#method-2

e= dict(sorted(y.items()))
print(e)

#how will you get the max value from the dictionary
max_val ={'A':2,'B':3,'C':4,'D':1,'E':5}

y= max(max_val, key = lambda x: max_val[x])
print("Max value is",y)


#How to get prime number

num = int(input("Enter the number:"))

if num == 1:
    print("Its not a prime number")

elif num > 1 :

    for i in range(2, num):

        if (num%i) == 0:
            print("Its not a prime number")
            break

    else:
        print("Its a prime number")
else:
    print("Its not a prime number")
#fibbonacial series

def fibnocial(n):

    if n < 0:

        print("Please provide correct value")

    elif n == 0:

        return 0
    
    elif n == 1 or n == 2 :
        
        return 2

    else:

        return fibnocial(n-1)+fibnocial(n-2)


print(fibnocial(12))

#palindrome

x="aba"


if x == x[::-1]:
    
    print("Its a palindrome")

else:

    print("Its not a palindrome")

#call by reference or call by value in python


#call by reference [when values are modified with in the function also gets reflected in outside of the function is called call by refrence]

def myFunc(mylist):

    mylist.append(3)
    mylist.extend([2,4])
    mylist.remove(4)

    print("my list is ",mylist)

    
list1=[1]
myFunc(list1)
print("my list is ",list1)




#call by value

#what ever values passing to the function are not reflected in outside of the function is called get by value
#Immutable objects


def myFunc(a):
    print("Value received in 'a'",a)

    a+=2

    print("Value received after modification", a)
num=13
myFunc(num)
print("Value received after modification", num)


#shallow copy and deep copy


#shallow copy:when you made changes to the original list that changes also reflected in the latest list


import copy

old_list = [[1,1,1],[2,2,2],[3,3,3]]
new_list = copy.copy(old_list)

old_list[1][1] = 'aa'

print(old_list)
print(new_list)

#deep copy
import copy

old_list = [[1,1,1],[2,2,2],[3,3,3]]
new_list = copy.deepcopy(old_list)

old_list[1][1] = 'aa'

print(old_list)
print(new_list)

x="qqqeerrttyu"
x.split()

d=dict()

for i in x:
    if i in d:
        d[i]+=1

    else:
        d[i]=1

print(d)

#remove duplicates without using the set function



x=[1,2,3,4,4,5,6,6]

res=[]

for i in x:

    if i not in res:

        res.append(i)

print(res)

#how to remove the duplicates in string

x="aabbccdd"

y=list(x)
li=[]
z=''
for i in y :
    if i not in li:
        z.join(str(i))
print(z)

#how to work with try exception handling


try:

    x= int(input("Enter the value:"))
    y= int(input("Enter the value:"))

    print(x/y)

except (ZeroDivisionError,ValueError) as msg:

    print(msg)



    
x = "remove duplicates without using the set function"

y=x.split()

print(len(y))


z = "remove duplicates without using the set function"
print(len(z))
z.strip()
print(len(z))

with open("abc.txt","w") as f:

    lst ="Hyderabad is the capital of southern India's Telangana state. A major center for the technology industry, it's home to many upscale restaurants and shops. Its historic sites include Golconda Fort,"
    f.writelines(lst)


with open(r"C:\Users\linga\Downloads\abc.txt","r") as f :
    #data = f.read()   #Note this
    #print(data)
    #data1 = f.readline()
    #print(data1)
    count=0
    data2 = f.readlines()
    print(data2)
    for i in data2:
        if i == "the":
            count+=1

        else:
            count=1
    print("Count the no of the values",count)








y= {i:i**2  for i in range(21) }

print(y)

#---------------------------------------

def decor(func):

    def inner(name):

        if name == "Lingababu":

            print("Hi Good morning",name)

        else:
            func(name)

    return inner

@decor
def wish(name):

    print("Hi Good evening",name)

wish("Lingababu")
wish("Maha")
wish("Raju")
#-----------------------------------------

#Decarator with parameters

#-----------------------------------------
def decorator(*args, **kwargs):
    print("Inside decorator")
     
    def inner(func):
        # code functionality here
        print("Inside inner function")
        print("I like", kwargs['like'])
         
        func()
         
    # returning inner function   
    return inner
 
@decorator(like = "geeksforgeeks")
def my_func():
    print("Inside actual function")


#---------------------------------------



class Exception:


    def __init__(self,x,y):

        self.x=x
        self.y=y

    def handling(self):
    
        try:

            print(self.x/self.y)

        except ZeroDivisionError as msg:

            print("please pass positive integer",msg)


exp = Exception(2,0)






class Hyderabad:

    def __init__(self,people,companys,areas,parkings):

        self.people = people
        self.companys = companys
        self.areas = areas
        self.parkings = parkings

    def About_people(self):

        print("Hyderabad more concentrated the at the main citys.",self.people)



    def About_companys(self):

        print("Hyderabad more concentrated with the at the main citys",self.companys)

        


    def About_areas(self):

        print("Hyderabad more concentrate at the main citys.",self.areas,"and",self.parkings)


        
obj = Hyderabad(15000,"TechM","Madhapur","Metro")

obj.About_people()
obj.About_companys()
obj.About_areas()

#without Init


class Hyderabad:



    def About_people(self,people):
        self.people = people

        print("Hyderabad more concentrated the at the main citys.",self.people)



    def About_companys(self):

        print("Hyderabad more concentrated with the at the main citys",self.companys)

        


    def About_areas(self):

        print("Hyderabad more concentrate at the main citys.",self.areas,"and",self.parkings)


        
obj = Hyderabad()

obj.About_people(15000)

    


#work with abstract method method

from abc import *

class Test(ABC):
    
    @abstractmethod
    def m1(self):
        pass
class Test1(Test):

    def m1(self):
        print("Here Implemented")


#single Inheritance

class Parent:

    def talk(self):
        print("Talk Talk")


class Children(Parent):

    def walk(self):
        print("Walk Walk")

obj=Children()

obj.talk()              


#Multiple Inheritance     {  Many to one }

class P1:

    def p1(self):
        print("frist parent")

class P2:

    def p2(self):
        print("second parent")

class C(P1,P2):

    def c (self):
        print("child parent")

obj=C()
obj.p2






#Multilevel Inheritance  {one to one}

class P:

    def p(self):
        print("frist parent")
class C(P):

    def c(self):
        print("frist child")
class CC(C):

    def cc(self):
        print("seccond child")
        
class CCC(CC):

    def ccc(self):
        print("third child")

obj = CCC()
obj.c()

#Hirarche Inheritance     {from parent to many child }

class P:

    def p(self):
        print("frist parent")
class C1(P):

    def c1(self):
        print("frist child")
class C2(P):
    def c2(self):
        print("second child")
class C3(P):
    def c3(self):
        print("third child")

obj = C3()
obj.c3()



#Hybrid Inheritance      {single + multiple + multilevel }


#class P
#class C1
#class C2
#class C3



#cyclic Inheitance     {A-B,B-A}

#class P
#class C1
#class C2
#class C3


#method overloading

class P:

    def m1(self):
        print("no argument")
    def m1(self,a):
        print("with one argument")
    def m1(self,a,b):
        print("with two argument")

obj = P()
obj.m1(2,3)





#*arguments

def sum_all(*a):

    return sum(a)

print(sum_all(2,3,4,5,6,6,7,7))


#**keyword arguments





#method overriding

class P1:

    def m1(self):

        print("Normal Implementation")

    def carrer_path(self):
        print("CA")

class C(P1):

    def carrer_path(self):
        print("mba")


obj = C()
obj.m1()






#super keyword

#Super keyword is used to call the super class constractors and variables and methods from the child class


class Person:

    def __init__(self,name,age):

        self.name =name
        self.age = age


    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)

class Student(Person):

    def __init__(self,name,age,rollno,marks):

        super().__init__(name,age)
        self.rollno = rollno
        self.marks = marks

    def display(self):

        super().display()
        print("Roll no:",self.rollno)
        print("Marks:",self.marks)

s1 = Student('Durga',22,101,90)
s1.display()
         
#pytest

 








#Unittesting







