# Activity 1

rate = 500
tax = 600.00
def grossSalary(rate, hourRendered):
    result = rate * hourRendered
    return float(result, '.2f')

def salaryDeduction(tax, loan, insurance):
    total_deduction = float(tax + loan + insurance, '.2f')
    return total_deduction
def netSalary():
    return float(grossSalary(rate, hourRendered) - salaryDeduction(tax, loan, insurance), '.2f')

print("Payslip App")
name = input("Enter name: ")

while True:
    try:
        hourRendered = float(input("Enter Hour Rendered: "))
        loan = float(input("Enter Loan: "))
        insurance = float(input("Enter Insurance: "))
        print("\nEmployee Payslip Details")
        print("Name: ", name)
        print("Hour Rendered: ", hourRendered) 

        print("\nGross Salary: Php", grossSalary(rate, hourRendered))

        print("\tTax: Php", tax)
        print("\tLoan: Php", loan)
        print("\tInsurance: Php", insurance)

        print("\nTotal Deductions: Php", salaryDeduction(tax, loan, insurance))
        print("\nNet Salary: Php", netSalary())
        break
    except:
        print("Invalid input, Please input a number")







