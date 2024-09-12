# Tan Jun Wei
# S10266704C

letters = {}

sentence = input('Enter a sentence: ').lower()

for char in sentence:
    if char.isalpha():
        letters[char] = sentence.count(char)

for letter, count in letters.items():
    print(f'{letter} : {count}')