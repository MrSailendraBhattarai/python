
#syntax for file create
with open("file_name.extension",mod) as file_obj:


with open("readme.txt",'r+')as file_obj: #file Create
    file_obj.write("Hello World")
    print(file_obj.read()) #readline(), readlines()


    f=open("readme.txt","r")#file read
    print(f.read())

with open ("readme.txt","a") as file_obj: # Append data in file
    file_obj.write("Hello")