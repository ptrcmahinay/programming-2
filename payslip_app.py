# Activity 1
rate = 500
tax = 0.12
def grossSalary(rate, hourRendered):
    result = rate * hourRendered
    return result

def salaryDeduction(tax, loan, insurance):
    total_deduction = tax + loan + insurance
    return total_deduction

def netSalary():
    return grossSalary(rate, hourRendered) - salaryDeduction(tax, loan, insurance)


print("Payslip App")
name = input("Enter name: ")
while True:
    try:
        hourRendered = int(input("Enter Hour Rendered: "))
        loan = int(input("Enter Loan: "))
        insurance = int(input("Enter Insurance: "))

        print("\nEmployee Payslip Details")
        print("Name: ", name)
        print("Hour Rendered: ", hourRendered) 

        print("\nGross Salary: Php", format(grossSalary(rate, hourRendered), '.2f'))

        tax = tax * grossSalary(rate, hourRendered)
        print("\tTax: Php", format(tax, '.2f'))
        print("\tLoan: Php", format(loan, '.2f'))
        print("\tInsurance: Php", format(insurance, '.2f'))

        print("\nTotal Deductions: Php", format(salaryDeduction(tax, loan, insurance), '.2f'))
        print("\nNet Salary: Php", format(netSalary(), '.2f'))
        break
    except:
        print("Invalid input, Please input a number")





