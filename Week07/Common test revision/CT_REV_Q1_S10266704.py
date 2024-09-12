# Tan Jun Wei (S10266704) - CSF02

times = input('Enter time taken of 2 laps separated by semi-colon (seconds):')

times_list = times.split(';')

firstlap_time = int(times_list[0])
secondlap_time = int(times_list[1])

if firstlap_time < secondlap_time: 
    best = firstlap_time 
else:
    best = secondlap_time 

total = firstlap_time + secondlap_time 
average = total / len(times_list)

print(f"Tom's best time is {best:.1f} s and average time is {average:.1f} s")
