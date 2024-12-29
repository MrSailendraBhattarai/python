class Person:
    def __init__(self,gender):
        self.gender=gender

    def get_gender(self):
        print(f"I am {self.gender}")

class Student(Person):
    def __init__(self,name,gender):
        self.name=name
        # Person.__init__(self)
        super().__init__(gender)

    def study(self):
        print(f"My Name is {self.name} and I am Studying")

obj=Student("Ram","male")
obj.study()
obj.get_gender()
# print(obj.gender)