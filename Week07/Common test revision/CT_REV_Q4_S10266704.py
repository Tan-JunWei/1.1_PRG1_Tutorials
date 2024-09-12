# Tan Jun Wei (S10266704) - CSF02
num = int(input("Enter a number between 0 and 5000: "))
number = num
#Tn = ((n**2)+n)/2
# n^2 + n == 2(input)
# Tn refers to number of dots in entire arrangement
# n refers to number of dots in base

number_of_dots_in_row = 1
dots = 0
while number_of_dots_in_row <= number:
    number -= number_of_dots_in_row
    dots +=1
    number_of_dots_in_row += 1

if number == 0:
    print(f"{num} is a triangular number and it is the {dots}th number")
else:
    print(f"{num} is a NOT triangular number.")


'''
##############################################
#   suggested answer using while else loop   #
##############################################

n = 1
while n < num:
    Tn = ((n**2)+n)/2
    if Tn == num:
        print(f"{num} is a triangular number and it is the {n}th number.")
        break
    
    n += 1

else: 
    print(f"{num} is NOT a triangular number.")
'''