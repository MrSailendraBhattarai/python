class Employee:
    list_1=[
        {'name':'Ram','salary':35000,'bonus':2},
        {'name':'Shyam','salary':30000,'bonus':5},
        {'name':'Hari','salary':80000,'bonus':10},
        {'name':'Gopal','salary':62000,'bonus':23}
        ]


    def salary_1(self,salary,bonus):
        salary=salary+(salary*bonus/100)
        return salary
    def data(self):
        for item in self.list_1:
            name=item['name']
            salary=item['salary']
            bonus=item['bonus']
            total_salary=self.salary_1(salary,bonus)
            print(f'Name: {name}, Salary with Bonus: {total_salary}, Bonus: {bonus}%')

e=Employee()
e.data()