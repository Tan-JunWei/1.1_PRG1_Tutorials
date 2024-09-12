#Programming I

########################
#     Mission 6.1      #
#  Loop even integers  #
########################

#Background
#==========
#Write a program that uses while loop to total up the even integers within the given range.

#Important Notes
#===============
#1) Comment out ALL input prompts before submitting.
#2) You are to complete this question with if statements and while loop
#3) You MUST use the following variables
#   - start : that stores the start of the range
#   - end : that stores the end of the range
#   - total that stores the total of the even numbers within the range

#START CODING FROM HERE
#======================


#Define function 
def total_num(start, end):
    i = 0
    list = []
    while i != end +1:
        if i %2 == 0:
            list.append(i)
        i += 1
    total = sum(list)
    print(total)
    return total #Do not remove this line that returns the total found


#Prompt user to enter the starting and ending values of the range

#Do not remove the next line
total = total_num(1, 10)

#Modify to display the total
print()

#input: 1, 10
#output 30
#input: 0, 100
#output 2550
