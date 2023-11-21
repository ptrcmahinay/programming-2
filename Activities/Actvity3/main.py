from SalaryDeductions import salary_deduction
from NetSalary import netSalary
from GrossSalary import gross_salary

rate = 500
tax = 0.12

hourRendered = int(input("Enter Hour Rendered: "))
loan = int(input("Enter Loan: "))
insurance = int(input("Enter Insurance: "))

salary = gross_salary(rate, hourRendered)
deduction = salary_deduction(tax, loan, insurance)
net = netSalary(salary, deduction)
tax = tax * salary

print("Payslip App")
name = input("Enter name: ")
while True:
    try:
        print("\nEmployee Payslip Details")
        print("Name: ", name)
        print(f"Hour Rendered: {hourRendered:.2f}") 
        print("\nGross Salary: Php", format(salary, '.2f'))
        print("\tTax: Php", format(tax, '.2f'))
        print("\tLoan: Php", format(loan, '.2f'))
        print("\tInsurance: Php", format(insurance, '.2f'))
        print("\nTotal Deductions: Php", format(deduction, '.2f'))
        print("\nNet Salary: Php", format(net, '.2f'))
        break
    except:
        print("Invalid input, Please input a number")
        break



