class Employee:
    def putdata(self):
        self.id=int(input("Enter empID:"))
        self.name=input("Enter emp name:")
        self.salary=float(input("Enter empSal:"))

    def display(self):
        print("EmpId:",self.id)
        print("EmpName:",self.name)
        print("EmpSal:",self.salary)

a=Employee()
a.putdata()
a.display()