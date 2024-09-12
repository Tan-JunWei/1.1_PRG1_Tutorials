# Tan Jun Wei
# S10266704C

side = int(input("Enter the length of side: "))
char = input("Enter character: ")

def print_square(char, side):
    for i in range(side):
        print((char+" ")*side)

print_square(char, side)