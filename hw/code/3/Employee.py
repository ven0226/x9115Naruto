__author__ = 'Venkatesh'

class Employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self):
        return 'Name: %s Age: %d' % (self.name,self.age)

    def __lt__(self, other):
        return self.age < other.age

emp1 = Employee('Venky',27)
print emp1

print

emp_list = [Employee("John",28),Employee("Doe",20),Employee("Jane",24)]
print emp_list

print sorted(emp_list)