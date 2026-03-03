# PROGRAM TO GENERATE A LOOP USING NESTED LOOPS

for row in range(5, 0, -1):
    for column in range(1, row + 1):
        print(column, end="")
    print()