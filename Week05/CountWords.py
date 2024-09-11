#Student name: Tan Jun Wei
#Student ID: S10266704C

filename = input("Please enter the filename: ")

with open(filename,"r") as datafile:
    result = []
    for line in datafile:
        removed = line.strip()
        list = removed.split(" ")
        num = len(list)
        result.append(num)
    total = sum(result)

    print(f"Number of words in {filename}: {total}")

    with open("output.txt","a") as datafile2:
        datafile2.write(f"There are {total} words in the document.")

    print("Number of words successfully written to output.txt")
