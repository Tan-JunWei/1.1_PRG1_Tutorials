#Student Name: Tan Jun Wei
#Student ID: S10266704C

sees_player = str(input("Does the guard see the player (y/n)?" ))

if sees_player == "y":
    dist_from_player = int(input("How far away is the player? "))
    if dist_from_player <= 1:
        print("The guard attacks!")
    elif dist_from_player <=4:
        print("The guard advances.")
    else:
        print("The guard waits.")
else:
    print("The guard waits.")