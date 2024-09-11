#Programming I

#####################################
#            Mission 2.1            #
#           Coin Converter          #
#####################################

#Background
#==========
#Tom has 2 50-cent coins, 4 20-cent coins, 6 10-cent coins and 9 5-cent coins.
#He would like calculate the total amount in dollars.

#Requirements
#============
#Develop a pseudocode and Python program to solve the following problem:
#   -Given a number of 50-cent coins, 20-cent coins, 10-cent coins
#    and 5-cent coins, calculate the amount in dollars, print the
#    output with proper description and the amount in proper format

#Important Notes
#===============
#1) Include the pseudocode that you have developed as comments at the
#   beginning of your program.
#2) You MUST (at least) use the following variables:
#   - cent50 (number of 50-cent coins)
#   - cent20 (number of 20-cent coins)
#   - cent10 (number of 10-cent coins)
#   - cent5  (number of 5-cent coins)


#TYPE YOUR PSEUDOCODE BELOW AS COMMENTS
#======================================

#Get the number of 50-cent coins, 20-cent coins, 10-cent coins and 5-cent coins respectively
#multiply the number of coins with the values respectively
#display final value, the total amount, in dollars



#TYPE YOUR PYTHON CODE BELOW
#===========================

#Input
cent50 = 2
cent20 = 4
cent10 = 6
cent5 = 9

#Process
value50 = 0.5 * cent50
value20 = 0.2 * cent20
value10 = 0.1 * cent10
value5 = 0.05 * cent5

#Output
print("$", round(value50 + value20 + value10 + value5,2), sep="")
