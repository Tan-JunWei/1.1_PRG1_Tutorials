#Student name: Tan Jun Wei
#Student ID: S10266704C

friends = ['Izzat', 'Bryan', 'Dalton', 'Ethan', 'Isaac']
new_friend = str(input("What is the name of your new friend?")).capitalize() #capitalize if input is not capitalized
friends.append(new_friend)
print(f"My friends are: {friends}")
friendzone = str(input("Who do you want to friendzone?")).capitalize() #capitalize if input is not capitalized
print(f"{friendzone} was in position {friends.index(friendzone)}. He will be friendzoned")
friends.remove(friendzone)
print(f"My eligible friends are now: {friends}")
