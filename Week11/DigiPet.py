# Name: Tan Jun Wei
# Student ID: S10266704C

menu = ['Feed','Play','Rest','Status']
status = [3,3,3]
title = ['hungry','happiness','energy']
msg = ['Nom nom nom','XD','Zzzzz']

print("Digipet")
for i in range(len(menu)):
    print(f"({i+1}) {menu[i]}")

while True:
    option = input("Please select an option: ")
    if option == "1":
        if status[0] < 5:
            status[0] += 1
        print(msg[0])
    elif option == "2":
        if status[1] < 5:
            status[1] += 1
        print(msg[1])
    elif option == "3":
        if status[2] < 5:
            status[2] += 1
        print(msg[2])
    elif option == "4":
        for z in range(len(status)):
            print(f"{title[z]:<10}","*"*status[z],end="")
            print("."*(5-status[z]))
    for i in range(len(menu)):
        print(f"({i+1}) {menu[i]}")