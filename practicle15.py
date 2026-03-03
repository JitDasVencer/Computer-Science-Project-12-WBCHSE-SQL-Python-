# PROGRAM FOR BINARY SEARCH OPERATION

numbers = list(map(int, input("Enter sorted numbers: ").split()))
element_to_search = int(input("Enter element to search: "))

lower_index = 0
upper_index = len(numbers) - 1

while lower_index <= upper_index:
    middle_index = (lower_index + upper_index) // 2

    if numbers[middle_index] == element_to_search:
        print("Element found at position", middle_index)
        break
    elif numbers[middle_index] < element_to_search:
        lower_index = middle_index + 1
    else:
        upper_index = middle_index - 1
else:
    print("Element not found")