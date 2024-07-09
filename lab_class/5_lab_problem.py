class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id


employee1 = Employee("Maria", 21, "232071014")


print(employee1.name, employee1.age, employee1.employee_id)
