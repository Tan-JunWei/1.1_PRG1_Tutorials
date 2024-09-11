#Optional Activities in Week02 PRG1 tutorial
#Question 1: ChickenRice.py: calculate total cost of purchase in a chicken rice order
#Name: Tan Jun Wei
#Student ID: S10266704C
import math

chickenRice = float(input("Enter the price of chicken rice: "))
sideDishesNumber = int(input("Enter the number of side-dishes: "))
sideDishesCost = 1.20

sideDishes = sideDishesNumber * sideDishesCost #calculate total cost of side dishes
GST = math.ceil(9/100 * (chickenRice+sideDishes) * 10)/10 #calculate GST to nearest ten-cent

total = chickenRice + sideDishes + GST

print(f"Total cost of the purchase is ${total:.2f}")
