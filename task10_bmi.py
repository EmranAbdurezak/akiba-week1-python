name=input("Enter your name: ")
weight=float(input("Enter your weight(Kg): "))
height=float(input("Enter your height(m): "))
BMI=weight/(height*height)

print("===========================================")
print("             BMI REPORT ")
print("===========================================")
print(f"\nName: {name}")
print(f"Weight: {weight} kg")
print(f"Height: {height} m")

print(f"\nBMI: {BMI:.2f}")
print("===========================================")