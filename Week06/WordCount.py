# Student name: Tan Jun Wei
# Student ID: S10266704C

total_letters = 0
word_list = []

while True:
    word = input("Enter word (x to exit): ")
    if word in word_list:
        print(f"{word} has already been entered.")
        continue
    
    word_list.append(word) 
    total_letters += len(word)

    if word.lower() == "x" or len(word_list) == 5:
        if "x" in word_list:
            word_list.remove("x")
            total_letters -= 1

        print(f"Your words are {word_list}\n"
              f"The number of letters in these words is {total_letters}")
        break
        

    