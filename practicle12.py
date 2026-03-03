# PROGRAM TO GENERATE A PATTERN USING NESTED LOOPS

for row in range(1, 6):
    for column in range(row):
        print("*", end="")
    print()