#Week 2 Activity 4: Accept time in seconds as input and converts it into hours, minutes and seconds
#Name: Tan Jun Wei
#Student ID: S10266704C
time_seconds = int(input("Enter time in seconds:"))

number_of_hours = time_seconds // 3600 #find number of hours

remainder_seconds = time_seconds % 3600
number_of_minutes = remainder_seconds // 60 #find number of minutes

number_of_seconds = remainder_seconds % 60 #find number of seconds remaining 

print(number_of_hours,"hr", number_of_minutes, "min", number_of_seconds, "seconds")