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


