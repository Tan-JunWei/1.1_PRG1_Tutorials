# Name: Tan Jun Wei
# Student ID: S10266704C

char = input("Enter a character: ")
n = int(input("Enter a number: "))

for row in range(n):

    # Print leading spaces
    print(" "*(n-row-1),end="")

    # Print characters accordingly
    for k in range(row + 1):
        print(char, end=" ")
    # Move to the next line
    print()