# PROGRAM FOR FACTORIAL USING RECURSION

def calculate_factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * calculate_factorial(number - 1)

number = int(input("Enter a number: "))
factorial_result = calculate_factorial(number)

print("Factorial =", factorial_result)