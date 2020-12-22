class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount +=1

    def displayCount(self):
        print ("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", salary: ", self.salary)

# Here adding the code for putting all concepts together

#This would create first object of the Employee class"
emp1=Employee("Zara",2000)
emp2=Employee("Mukesh",3000)

emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d " % Employee.empCount)

#Here is the output:
"""
Name :  Zara , salary:  2000
Name :  Mukesh , salary:  3000
Total Employee 2
"""
