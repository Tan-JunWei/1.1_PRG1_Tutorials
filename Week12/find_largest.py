# Tan Jun Wei
# S10266704C

first = int(input("Enter the first integer number: "))
second = int(input("Enter the second integer number: "))
third = int(input("Enter the third integer number: "))
fourth = int(input("Enter the fourth integer number: "))

def find_larger(n1,n2):
    if n1 > n2:
        return n1
    else:
        return n2
    
larger = find_larger(first,second)
larger = find_larger(larger,third)
larger = find_larger(larger,fourth)

print(F"The largest integer is {larger}")