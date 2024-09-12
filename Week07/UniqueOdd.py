#Student Name: Tan Jun Wei
#Student ID: S10266704C

numbers = [2, 7, 11, 6, 7, 3, 17, 7, 12, 41, 8, 11, 13, 10, 15]
odd = []

for num in numbers:
    if num not in odd and num % 2 and len(odd) < 5:
        odd.append(num)
print(odd)