# Name: Tan Jun Wei
# Student ID: S10266704C

map = [ [' ', 'T', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
      ]

def display_map(map):
    for row in map:
        print("+---+---+---+---+---+")
        print("|"," | ".join(row),"|")
    print("+---+---+---+---+---+")

display_map(map)
direction = input("Enter your direction or Q to quit: ").lower()

def move():
    found = False
    for i in range(len(map)): # map[i] refers to 1 row
        for j in range(len(map[i])): 
            if map[i][j] == 'T':
                # coordinates = i,j
                # print(coordinates) # i,j is the coordinates of "T"
                
                # Check above 'T' (W)
                if direction == 'w':
                    if i > 0 and map[i-1][j] == ' ':
                        map[i][j] = ' '
                        map[i-1][j] = 'T'
                        display_map(map)
                    else:
                        print("Sorry, you are not allowed to move up.")

                # Check left of 'T' (A)
                elif direction == 'a':
                    if j > 0 and map[i][j-1] == ' ':
                        map[i][j] = ' '
                        map[i][j-1] = 'T'
                        display_map(map)
                    else:
                        print("Sorry, you are not allowed to move left. ")

                # Check below 'T' (S)
                elif direction == 's':
                    if i < len(map) -1 and map[i+1][j] == ' ':
                        map[i][j] = ' '
                        map[i+1][j] = 'T'
                        display_map(map)
                    else:
                        print("Sorry, you are not allowed to move down. ")

                # Check right of 'T' (D)
                elif direction == 'd':  # Move right
                    if j < len(map[i]) - 1 and map[i][j+1] == ' ':
                        map[i][j] = ' '  
                        map[i][j+1] = 'T'  
                        display_map(map)  
                    else:
                        print("Sorry, you are not allowed to move right.")
                else:
                    print("invalid")

                found = True
                break
        if found:
            break

while direction != "q":
    move()
    direction = input("Enter your direction or Q to quit: ").lower()
    
if direction == 'q':
    print("Bye-bye!")