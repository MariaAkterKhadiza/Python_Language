#
class Employee:
    def __init__(self, salary):
        self._salary = salary
    
    def display_salary(self):
        print(self._salary)

class Manager(Employee):
    def __init__(self, salary):
        super().__init__(salary)
    
    def show_salary(self):
        self.display_salary()

manager = Manager(100000)
manager.show_salary()
