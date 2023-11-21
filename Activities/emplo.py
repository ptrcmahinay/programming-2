class Employee:
    def __init__(self, name, office, position, salary):
        self.name = name
        self.office = office
        self.position = position
        self.salary = salary

employees = [
    Employee("Giovanni N. de los Santos", "IT department", "Data Manager", "15000"),
    Employee("Patricia Ann C. Mahinay", "IT department", "Student", "5000"),
    Employee("Charles Gula", "IT department", "Student", "500")
]

for employee in employees:
    print(f"Name: {employee.name}")
    print(f"Office: {employee.office}")
    print(f"Position: {employee.position}")
    print(f"Salary: {employee.salary}")
    print("\n")