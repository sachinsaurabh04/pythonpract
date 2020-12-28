#!/usr/bin/python3
class Employee:
    'Common base class for all employees'
    empCount=0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount +=1

    def displayCount(selfself):
        print("Total Employee %d" % Employee.empCount)

        def displayEmployee(self):
            print("Name :", self.name, ",Salary: ", self.salary)

emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)
print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)


"""
/home/sachin/PycharmProjects/pythonProject1/venv/bin/python "/home/sachin/PycharmProjects/pythonProject1/Object Oriented/class2.py"
Employee.__doc__: Common base class for all employees
Employee.__name__: Employee
Employee.__module__: __main__
Employee.__bases__: (<class 'object'>,)
Employee.__dict__: {'__module__': '__main__', '__doc__': 'Common base class for all employees', 'empCount': 2, '__init__': <function Employee.__init__ at 0x7f2b0c7cbf70>, 'displayCount': <function Employee.displayCount at 0x7f2b0c7db040>, '__dict__': <attribute '__dict__' of 'Employee' objects>, '__weakref__': <attribute '__weakref__' of 'Employee' objects>}
"""