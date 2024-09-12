# Name: Tan Jun Wei
# Student ID: S10266704C

days = int(input("Enter number of days: "))
first_day = input("When is the first day of the week: ")

days_in_a_week_dict = {
    0:"Sun",  # Sunday is zero because of the calendar formatting
    1:"Mon",
    2:"Tue",
    3:"Wed",
    4:"Thu",
    5:"Fri",
    6:"Sat"
}

calendar = [ 
    [' ', ' ', ' ', ' ', ' ',' ',' '],
    [' ', ' ', ' ', ' ', ' ',' ',' '],
    [' ', ' ', ' ', ' ', ' ',' ',' '],
    [' ', ' ', ' ', ' ', ' ',' ',' '],
    [' ', ' ', ' ', ' ', ' ',' ',' '],
    [' ', ' ', ' ', ' ', ' ',' ',' ']
]

print(" ".join(days_in_a_week_dict.values())) # print first line showing the days of the week

for key,value in days_in_a_week_dict.items(): # find the index that the first number shld be inserted in
    if first_day == value:
        number = key

i = 1 # initialise the counter as 1 since dates start frm 1.
# this counter is used for both for loops since dates are increasing linearly

for k in range(len(calendar)):
    if k == 0: # make a separate for loop for first line due to the first_day input
        for index in range(number,len(calendar[k])):
            calendar[k][index] = str(i)
            i+=1
    else: 
        for index in range(len(calendar[k])):
            if i <= days:  # ensure that it does not exceed the number of days entered as input
                calendar[k][index] = str(i)
            i+=1

for row in calendar:
    print(" ".join(day.rjust(3) for day in row)) # .rjust is used for right justify for proper formatting

'''
# Without the use of dictionaries: 

days = int(input("Enter number of days: "))
first_day = input("When is the first day of the week: ").lower()

calendar = [ 
    [' ', ' ', ' ', ' ', ' ',' ',' '],
    [' ', ' ', ' ', ' ', ' ',' ',' '],
    [' ', ' ', ' ', ' ', ' ',' ',' '],
    [' ', ' ', ' ', ' ', ' ',' ',' '],
    [' ', ' ', ' ', ' ', ' ',' ',' '],
    [' ', ' ', ' ', ' ', ' ',' ',' ']
]

weekdays = ["sun","mon","tue","wed","thu","fri","sat"]

counter = 1

if first_day in weekdays:
    index = weekdays.index(first_day)
else:
    print("Invalid input for first day of the week. ")

for i in range(len(calendar)):
    if i == 0:
        for z in range(index,len(calendar[i])):
            calendar[i][z] = str(counter)
            counter += 1
    else:
        for z in range(len(calendar[i])):
            if counter <= days:
                calendar[i][z] = str(counter)
                counter += 1

print(" ".join(weekday.capitalize().rjust(3) for weekday in weekdays))
for row in calendar:
    print(" ".join(day.rjust(3) for day in row)) # .rjust is used for right justify for proper formatting
'''

