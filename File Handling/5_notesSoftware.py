
class Notes:
    def add_notes(self):
        n=int(input("How Many Computer Want to Add: "))
        for i in range(0,n):
            Id=input("Enter Computer Id: ")
            name=input("Enter Computer Name: ")
            brand=input("Enter Computer Brand: ")
            price=input("Enter Computer Price: ")
            quantity=input("Enter Computer Quantity: ")

            full_detail=(f"Id: {Id},Name: {name},Brand: {brand},Price: {price},Quantity: {quantity}")

            f=open("readme.txt","a")
            d=f.write("\n"+full_detail)

    def show(self):
        f=open("readme.txt")
        data=f.read()
        print(data)
    
    def Search(self):
        a=input("What to Search: ")
        f=open("readme.txt")
        data=f.readlines()

        for item in data:
            splitted_item=item.split(",")
            if a in splitted_item[0]:
                print(item)


N=Notes()
while True:
    print("""
    1: Add Notes
    2: Display Notes
    3: Search
    """)

    menu_input=input("Enter Menu: ")
    if menu_input=="1":
        N.add_notes()
    elif menu_input =="2":
        N.show()
    elif menu_input=="3":
        N.Search()

