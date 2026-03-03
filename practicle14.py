# PROGRAM TO INPUT A LIST OF NUMBERS AND SWAP ELEMENTS AT THE REVEN LOCATION WITH THE ELEMENTS AT ODD LOCATION

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

for index in range(0, len(numbers) - 1, 2):
    numbers[index], numbers[index + 1] = numbers[index + 1], numbers[index]

print("Modified List:", numbers)