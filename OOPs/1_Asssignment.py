class Employee:
    list_1=[
        {'name':'Ram','salary':35000,'bonus':2},
        {'name':'Shyam','salary':30000,'bonus':5},
        {'name':'Hari','salary':80000,'bonus':10},
        {'name':'Gopal','salary':62000,'bonus':23}
        ]


    def salary_1(self,salary,bonus):
        bonus=salary*bonus/100
        salary=salary+bonus
        return salary,bonus
    def data(self):
        for item in self.list_1:
            name=item['name']
            salary=item['salary']
            bonuss=item['bonus']
            total_salary,bonus=self.salary_1(salary,bonuss)
            print(f'Name: {name}, Salary: {salary}, Salary with Bonus: {total_salary},Bonus Amount: {bonus} Bonus%: {bonuss} ')

e=Employee()
e.data()


