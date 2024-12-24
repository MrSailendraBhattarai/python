class Cat:
    species="Black"
    def __init__(self,name,sound,weight):
        self.name=name
        self.sound=sound
        self.weight=weight
        print(f"Name: {name}, Sound: {sound}, Weight: {weight}")
    def food_calc(self):
        if self.weight == 5:
            print("50g of food")
        elif self.weight == 10:
            print("100g of food")
        elif self.weight<=5:
            print("10g food")
        else:
            print("No Data Found...")



obj=Cat('kitty','meow meow',5)
obj.food_calc()

obj_1=Cat('cat','meow',2)
obj_1.food_calc()

obj_2=Cat('cat','mee',10)
obj_2.food_calc()

# obj_1.food_calc(2)
