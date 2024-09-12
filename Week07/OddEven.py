#Student Name: Tan Jun Wei
#Student ID: S10266704C


num = int(input("Please enter a number (0 to end): "))
number_list = []
odd = []
even = []

#append all input into a number list
while True: 
    if num != 0:
        number_list.append(num)
        num = int(input("Please enter a number (0 to end): "))
    else:
        break

#check whether numbers in list are even or odd
for number in number_list:
    if number %2:
        odd.append(number)
    else:
        even.append(number)
odd.sort()
even.sort()


#calculate average
average = sum(number_list) / len(number_list)

print(f"Odd numbers: {odd}")
print(f"Even numbers: {even}")
print(f"Average = {average:.2f}")