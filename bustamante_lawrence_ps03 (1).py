employee_name = input("Employee Name: ")
rendered_hours = float(input("Rendered Hours: "))
rate_per_hour = float(input("Rate per Hour: "))
sss_contribution = float(input("SSS Contribution: "))
philhealth_contribution = float(input("PhilHealth Contribution: "))
loans = float(input("Loans: "))

gross_salary = rendered_hours * rate_per_hour

total_deductions = sss_contribution + philhealth_contribution + loans

net_salary = gross_salary - total_deductions

print("==============PAYSLIP==============")
print("======EMPLOYEE INFORMATION=======")
print("Employee Name: ", employee_name)
print("Rendered Hours: ", rendered_hours)
print("Rate per Hour: ", rate_per_hour)
print("Gross Salary: ", gross_salary)
print("=============DEDUCTIONS===========")
print("SSS: ", sss_contribution)
print("PhilHealth: ", philhealth_contribution)
print("Loans: ", loans)
print("Total Deductions: ", total_deductions)
print("==========NET SALARY==============")
print("Php. ", net_salary)
