list= It is a data structure which is mutable or changable sequence of elements. Each element in list
is known as items.
eg:- 
#Create
list_1=['apple','ball','cat','dog']

#Delete
list_1.remove('apple')

#Access 
for item in list_1:
    print(item[0])

#Add 
list_1.append('elephant')

#wap to take 5 friends data and store in list
details = []
for i in range(2):
    name = input("Enter Your Name: ")
    mobile = input("Enter Your Number: ")
    address = input("Enter Your Address: ")

    total_data = []
    total_data.append(name)
    total_data.append(mobile)
    total_data.append(address)
    details.append(total_data)
print(details)


