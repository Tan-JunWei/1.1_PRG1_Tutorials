# Tan Jun Wei (S10266704) - CSF02

card1 = int(input("Enter card 1: "))
card2 = int(input("Enter card 2: "))
card3 = int(input("Enter card 3: "))

# 1 is ace
# 11 is jack
# 12 is queen
# 13 is king

if card1 > 10:
    card1 = 10
if card2 > 10:
    card2 = 10
if card3 > 10:
    card3 = 10

total = card1 + card2 + card3 

if card1 == 1 or card2 ==1 or card3 ==1:
    total += 10
    if total > 21:
        total -= 10

print(f"Total value is {total}")

####################
#   Initial Code   #
####################

# total = 0
# if card1 !="1" and not(card1>10): #check if card1 is ace or face cards
#     total += card1
# else: #card1 must be ace or face cards
#     if card1 > 10: #face cards
#         total += 10
#     else:
#         if total + 11 < 21: #card is ace, check total
#             total += 11
#         else: #card is ace, and total > 21
#             total +=1

# if card2 !="1" and not(card2)>10: #check if card2 is ace or face cards
#     total += card2
# else: #card2 must be ace or face cards
#     if card2 > 10: #face cards
#         total += 10
#     else:
#         if total + 11 < 21: #card is ace, check total
#             total += 11
#         else: #card is ace, and total > 21
#             total +=1

# if card3 !="1" and not(card3)>10: #check if card3 is ace or face cards
#     total += card3
# else: #card3 must be ace or face cards
#     if card3 > 10: #face cards
#         total += 10
#     else:
#         if total + 11 < 21: #card is ace, check total
#             total += 11
#         else: #card is ace, and total > 21
#             total +=1
    
# print(f"Total value is {total}")