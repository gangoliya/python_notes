#  Write a class  Employee  with attributes  name  and  salary , and a method  display() . 
# Create another class  Manager  that inherits from  Employee  and adds a new 
# attribute  department . Override the  display()  method to include the department. 
# Create a  Manager  object and call the  display()  method

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def display(self):
        print(f"Employee name: {self.name}, Salary: {self.salary}")
    
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    
    def display(self):
        print(f"Employee name: {self.name}, Salary: {self.salary}, Department: {self.department}")


m1 = Manager("John Smith", 50000, "Sales")
m1.display()


print(m1.display()) # print is expecting something to print

