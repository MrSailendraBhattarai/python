# n=4
# for i in range(0,n):
#     a=input("Enter Computer Name: ")
#     b=input("Enter Brand: ")
#     c=input("Enter Price: ")


#     with open("readme.txt","a") as file_obj:
#         file_obj.write(a+"\n")
#         file_obj.write(b+"\n")
#         file_obj.write(c+"\n")
#         file_obj.write(str(n))

# f=open("readme.txt","r")
# print(f.read())

#WAP to make a system for computer shop to store computers data like, computer name,brand,price,id,generation,core

class ComputerShop:
    def __init__(self, options):
        self.options = options
        self.list_1 = []

        if self.options == 1:
            self.Store()
        elif self.options == 2:
            self.Sear()
        elif self.options == 3:
            self.sho()
        elif self.options==4:
            self.delete()
        else:
            print("Invalid Input")

    def Store(self):
        inp = int(input("How Many Data You Want to Add: "))
        for i in range(inp):  
            a = int(input("Enter Computer Id: "))
            b = input("Enter Name: ")
            c = int(input("Enter Price: "))

            data = {'Id': a, 'Name': b, 'price': c}
            self.list_1.append(data)

        with open("readme.txt", "a") as file_obj:
            file_obj.write("\n"+str(self.list_1))
        
        print("Data Added Successfully")

    def Sear(self):
        a = input("Enter PC ID: ")
        f=open("readme.txt")
        data=f.readlines()

        for item in data:
            if a in item:
                print("Search found:", item)
                break
            else:
                print("Search not found!")

    def sho(self):
        f=open("readme.txt")
        data = f.read()
        print(data)

    def delete(self):
        f=open("readme.txt")
        a=input("Enter Computer Id to Delete:  ")
        data=f.readlines()

        for item in data:
            if 'a' in item[0]:
                data.remove(item)
            print(item)

a = int(input("Enter Options: \n 1 Store Computer \n 2 Search Computer \n 3 Show All Computers \n 4 Delete Computer \n"))
CS = ComputerShop(a)





def delete(self):
        search_id = input("Enter the ID of the computer to delete: ").strip()
        with open(self.file_path, 'r') as file:
            lines = [line for line in file if not line.startswith(search_id)]
        with open(self.file_path, 'w') as file:
            file.writelines(lines)
        print("Deleted successfully!")