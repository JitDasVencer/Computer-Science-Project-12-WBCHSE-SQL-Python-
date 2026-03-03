# PROGRAM TO PRIME NUMBER CHECK

number = int(input("Enter a number: "))
is_prime = True

if number <= 1:
    is_prime = False
else:
    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break

if is_prime:
    print("It is a Prime Number")
else:
    print("It is Not a Prime Number")