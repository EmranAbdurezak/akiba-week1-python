Customer=input("Enter customer name: ")
Product1=input("Enter first product name: ")
Price1=float(input("Enter the price(ETB): "))
Quantity1=int(input("Enter the quantity: "))
total1=Price1*Quantity1

Product2=input("Enter second product name: ")
Price2=float(input("Enter the price(ETB): "))
Quantity2=int(input("Enter the quantity: "))
total2=Price2*Quantity2

TOTAL=total1+total2

print("=====================================")
print("             RECEIPT                 ")
print("=====================================")
print()
print(f"Customer: {Customer}")
print()
print(f"{'Product':<18}{'Price':>10}{'Qty':>6}")
print("----------------------------------------")
print(f"{Product1:<18}{Price1:>10.1f}{Quantity1:>6}")
print(f"{Product2:<18}{Price2:>10.1f}{Quantity2:>6}")

print()
print(f"Total:  {TOTAL} ETB")
print()
print("Thank you for your purchase!")
print("=====================================")
