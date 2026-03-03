# PROGRAM TO CHECK THE INPUT VALUES IS ARMSTRONG AND ALSO WRITE THE FUNCTION FOR PALINDROME

def check_palindrome(number):
    return str(number) == str(number)[::-1]

number = int(input("Enter a number: "))
original_number = number
sum_of_powers = 0
number_of_digits = len(str(number))

while number > 0:
    digit = number % 10
    sum_of_powers = sum_of_powers + digit ** number_of_digits
    number = number // 10

if original_number == sum_of_powers:
    print("It is an Armstrong Number")
else:
    print("It is Not an Armstrong Number")

if check_palindrome(original_number):
    print("It is a Palindrome Number")
else:
    print("It is Not a Palindrome Number")