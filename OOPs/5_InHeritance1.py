class Person:
    def __init__(self,gender):
        self.gender=gender

    def Display(self):
        print(f"I am {self.gender}")

class Student(Person):
    def __init__(self,name):
        self.name=name
    def study(self):
        print(f"My Name is {self.name} and I am Studying")

obj1=Person("Male")
obj1.Display()
# obj=Student("Ram")
# obj.study()
# obj.Display()