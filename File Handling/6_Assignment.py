# Q) Create a simple Inventory system that adds product details to a file after retrieving the product names from user input.
# Requirements:
# 1) Use class, objects and functions for adding, listing and deleting products from the file
# 2) Product class will have attributes like name, price, and quantity
# 3) Use exception handling wherever necessary.

while True:
    class inventory:

        def Add(self):
            add=int(input("How Many product you want to add>>>"))
            for i in range(0,add):
                a=int(input("Enter Product id: "))
                name=input("Product Name: ")
                price=int(input("Product price: "))
                quantity=int(input("Product Quantity: "))

                detail=(f"{a},{name},{price},{quantity} \n")
                f=open("readme.txt","a")
                data=f.write(detail)
            print("Data Added Successfully...")

        def delete(self):
            
            with open("readme.txt", "r") as f:
                data = f.readlines()
                print(data)

            
            delete = input("Enter Item to Delete: ")

            new_data = []

            for item in data:
                
                if delete in item:
                    item_found = True
                    continue  
                
                new_data.append(item)

            if item_found:
                with open("readme.txt", "w") as f:
                    f.writelines(new_data)
                print(f"Item  deleted.")
                print(new_data)
            else:
                print("Item Not Found!")



        def list(self):
            f=open("readme.txt")
            data=f.read()
            print(data)


    obj=inventory()
    option=int(input("""
    1> Add
    2>Delete
    3>See List
    """))
    if option==1:
        obj.Add()
    elif option==2:
        obj.delete()
    elif option==3:
        obj.list()
    else:
        print("Invalid!!")

