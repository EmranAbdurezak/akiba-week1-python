name = input("Enter employee name: ")
B_S = int(input("Enter basic salary (ETB): "))
T_A = int(input("Enter transport allowance (ETB): "))
F_A = int(input("Enter food allowance (ETB): "))

G_S = B_S + T_A + F_A

print("========================================")
print("             EMPLOYEE PAYSLIP       ")
print("========================================")
print()
print(f"Employee: {name}")
print()
print(f"Basic Salary:          {B_S:,} ETB")
print(f"Transport Allowance:   {T_A:,} ETB")
print(f"Food Allowance:        {F_A:,} ETB")
print("----------------------------------------")
print(f"Gross Salary:          {G_S:,} ETB")
print("========================================")
