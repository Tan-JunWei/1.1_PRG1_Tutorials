# Name: Tan Jun Wei
# Student ID: S10266704C

player = ['Hafu', 'Toast', 'Pokimane', 'Pewdiepie', 'Ninja', 'Markiplier']

results = [ 
    [98, 107, 87, 121],
    [88, 111],
    [79, 130, 99],
    [86, 100, 121, 66, 98],
    [108, 79, 92],
    [77, 126, 93, 100, 73, 89]
]

print(f"{'Player':15}{'Games':^10}{'Wins':^10}{'Total':^5}")
for i in range(len(player)):
    games = len(results[i])   # results[i] refers to each list in results
    wins = 0
    total = 0
    for score in results[i]:
        total += score
        if score > 100:
            wins += 1
    print(f"{player[i]:15}{games:^10}{wins:^10}{total:^5}")