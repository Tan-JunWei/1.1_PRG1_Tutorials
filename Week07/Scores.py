#Student Name: Tan Jun Wei
#Student ID: S10266704C

print(f"{'ID':12}{'Name':10}{'Test1':^10}{'Test2':^10}{'Average'}")
average_list = []
line_list = []

def average(score1,score2):
    average = (int(score1) + int(score2)) / 2
    average_list.append(average)
    return average

with open("scores.txt","r") as file:
    next(file)
    for i in file:
        i = i.strip()
        i = i.split(",")
        line_list.append(i)
        
        print(f"{i[0]:12}{i[1]:10}{i[2]:^10}{i[3]:^10}{average(i[2],i[3]):>7.2f}")

highest_average = max(average_list)
index = average_list.index(highest_average)
print(f"{line_list[index][1]} has the highest average score of {highest_average}")