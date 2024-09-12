card1 = int(input("Enter card 1: "))
card2 = int(input("Enter card 2: "))
card3 = int(input("Enter card 3: "))

if card1 > 10:
    card1 = 10
if card2 > 10:
    card2 = 10
if card3 > 10:
    card3 = 10

total = card1 + card2 + card3

if card1 == 1 or card2 ==1 or card3:
    total += 10
    if total > 21:
        total -= 10

print(f"Total value is {total}")