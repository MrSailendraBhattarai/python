with open ("store.txt","w") as file_obj: #create file and write
    file_obj.write("Hello")

f=open("store.txt")# read data from file
data=f.read()

f=open("store.txt")
data=f.readline()

f=open("store.txt")
data=f.readlines()