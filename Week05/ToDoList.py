#Student name: Tan Jun Wei
#Student ID: S10266704C

with open("todolist.txt","r") as datafile:
    todo = datafile.readline()
    prepare = datafile.readline()
    narrate = datafile.readline().strip()

print(todo,prepare,narrate)