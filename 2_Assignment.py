Difference between list,Dictionary,tuple and set with example with [create, delete, access, add]

list= It is a data structure which is mutable or changable sequence of elements. Each element in list
is known as items.
eg:- 
Create
list_1=['apple','ball','cat','dog']

Delete
list_1.remove('apple')

Access 
for item in list_1:
    print(item[0])

Add 
list_1.append('elephant')

Dictionary= It is a mutable data structure which allow to store key & value pairs.
eg:-
Create
Dict_1={'1':'Apple','2':'Ball'}

Delete
del Dict_1[1]

Access
for 2 in Dict_1:
    print(Dict_1[2])

Add 
Dict_1[3]={
'Cat'
}

Tuple= It is used to store multiple value in single variable. It is Ordered and un-changable. 
It allow to store duplicate values.
eg:-
Create
tuple_1=('apple','ball','cat')

Delete
delete tuple_1

Access
print(tuple_1[1])

Add
new_element=dog
appended_tuple=tuple_1+(new_element,)

Set= It is a collection which is un-changable, un-Ordered & un-indexed.
eg:-
Create
set_1={'apple','ball'}

Delete
set_1.remove('ball')

Access
for item in set_1:
    print(set_1)

Add
set_1.add('cat')


What is function and it's Types

It is a specific block of code which can be used multiple times by calling it.
Eg:-
def add():
    c=a+b
    print(c)
if a==1:
    add()

Types of Function:
without parameter and without return Types
def add():
    c=a+b
    print(c)

without parameter and with return Types
def add():
    c=a+b
    return c 

with parameter and without return Types
def add(a,b):
    c=a+b 
    print(c)
with parameter and with return Types
def add(a,b):
    c=a+b 
    return c