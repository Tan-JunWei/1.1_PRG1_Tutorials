#Programming I

#####################################
#            Mission 2.1            #
#    Compound Interest Calculator   #
#####################################

#Background
#==========
#Tom won a lottery amounting to $10000, and he is deciding if he should
#deposit it into a bank account to accumulate interest.

#Tom wishes to find out how much he will have in the bank account after
#a specified number of years, given his input.

#Requirements
#============
#1) Write pseudocode that sets the principal amount of $10000 to variable p,
#   annual nominal interest rate of 8% to variable r, number of times the
#   interest is compounded per year of 12 to variable n. The number of years
#   that the money will be compounded, t, is given by the user. Calculate
#   and print the final amount (up to 3 decimal places) after t years.
#   Note: Refer to the question in Coursemology for the formula.
#2) Code the Python program base on the pseudocode that you have developed.

#Important Notes
#===============
#1) Include the pseudocode that you have developed as comments at the
#   beginning of the next section.
#2) You MUST (at least) use the following variables:
#   - P (principal amount)
#   - r (annual nominal interest rate [as a decimal])
#   - n (number of times the interest is compounded per year)
#   - t (number of years)


#TYPE YOUR PSEUDOCODE BELOW AS COMMENTS
#======================================
#Set principal amount of $10000 to variable p
#Set 8% interest rate to r
#Set number of times the money is compounded per year of 12 to n
#Set number of years the money will be compounded t as input given by the user
#calculate final amount A using formula given
#display final amount



#TYPE YOUR PYTHON CODE BELOW
#===========================

#Input
P = 10000
r = 8
n = 12
t = int(input("Number of years the money will be compounded:"))

#Process
A = P * (1 + (r/n)) ** (n*t)

#Output
print(f"${A:.3f}")