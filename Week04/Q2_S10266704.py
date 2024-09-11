# Tan Jun Wei (S10266704) – CSF02
# Revision Test

# Enter the vehicle number to be validated: SBA1234K
# Validity of the vehicle number: Invalid

vehicle_number = input("Enter the vehicle number to be validated: ")

check = vehicle_number[1:] #Removes 'S'
# print(check)

#using string index to assign a value to each character
alphabets ="ABCDEFGHIJKLMNOPQRSTUV"
#initialise new list
numbers = []
num1 = alphabets.index(check[0].upper()) + 1
num2 = alphabets.index(check[1].upper()) + 1
numbers.append(num1)
numbers.append(num2)

remaining_4_numbers = [int(number) for number in check[2:6]]
#print(remaining_4_numbers)

numbers.extend(remaining_4_numbers)
#print(numbers)

#9,4,5,4,3,2
result = numbers[0]*9 + numbers[1]*4 + numbers[2]*5 + numbers[3]*4 + numbers[4]*3 + numbers[5]*2

position = result % 19
reference_string = "AZYXUTSRPMLKJHGEDCB"
valid_alphabet = reference_string[position]

if vehicle_number[-1] == valid_alphabet:
    print("Validity of the vehicle number: Valid")

else:
    print("Validity of the vehicle number: Invalid")