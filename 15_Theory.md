What is Data Structure?
It is a specialized format for organizing and Storing Data so it can accessed used efficiently.

Types of Data Structure:
Linear: Data items arranged in sequential order
Array: Collection of Similar Types of Data.
Stack: In Stack it can store data in Lifo Method, Where First added data is store in last and last added data can serve first.
Queue: Un-Like Stack, Queue structure can store data in Fifo Method, Where first added data can serve first and last added data is served at last.
Non-Linear: Data items arranged in non-Sequential order
Graph: In Graph all vertex is connected to each other through edges.
Tree: It is a collection of vertices and edges. However, in tree data structure, there can only be one edge between two vertices.

What is List With Example? How to Create list? How to access list items using while and for loop?

List: It is a simple Series of Words & Numbers
Create: List_1=[]
List_1=[‘Apple’,’Ball’,’Cat’]
Access Item in List
Using While Loop:
While i<len(List_1)
Print(List_1[i])
Using For Loop
For i in List_1:
Print(List_1[i])

How to add item and remove item from List? Change value of List.
Add Item:
list_1=[‘apple’,’ball’]
List_1.append(‘cat’)

Remove Item:
List_1.remove(‘apple’)
Change Value:
List_1[1]=’bat’

Data=[1,2,4] Data[2]=4

What is Dictionary With Example? How to Create Dictionary.
Dictionary in Python is used to store value in Key:Value pairs
Example: a={‘fruit’:’apple’,’student’:’sushil’}

Dictionary is Create same like list but it is surrounded by curly braces {}. And to create dictionary we can have to give both key and values.

Access item from dictionary:
Detail={‘fruit’:’apple’,’student’:’sushil’}
For key in Detail:
if key==’student’:
Print(Detail[key])
Add key and Value in Dictionary
Dict_1={‘fruit’:’apple’,’student’:’sushil’}
Dict_1[teacher]=’Abc’
Dict_1[College]=’XYZ’

Change value of Specific key in dictionary:
Dict_1={‘fruit’:’apple’,’student’:’sushil’}
Dict_1[“fruit”]=”Banana”
