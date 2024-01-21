class Employee:
    def __init__(self, salary, name):
        self.salary = salary
        self.name = name

    def getsalary(self):
        print(self.salary)

rahul = Employee("rahul" , "50000")
print(rahul.salary)
print(rahul.name)
rahul.getsalary()

harry = Employee("harry" , "70000")
print(harry.salary)
print(harry.name)

ramsha = Employee("ramsha" , "50000")
print(ramsha.salary)
print(ramsha.name)


