# Pograme to calculate simple interest and compound interest

principal = float(input("enter the principal ammount: "))
rate = float(input("Enter the rate of interest (%): "))
time = float(input("Enter the time (in years): "))

simple_interest = (principal + rate * time) / 100

compound_interest = principal + ((1 + rate / 100) ** time) - principal

print("\n--- Interest Calculation ---")
print("Simple Interest:", simple_interest)
print("Compound Interest:", compound_interest)