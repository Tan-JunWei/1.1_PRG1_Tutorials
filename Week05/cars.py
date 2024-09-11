#Student name: Tan Jun Wei
#Student ID: S10266704C

with open("Cars.txt","r") as datafile:
    content = datafile.read()
    list = content.split("\n")
    #['Fesla Corp', '***Price List***', 'Fesla Model S : $87490', 'Fesla Model 3 : $39990', 'Fesla Model X : $97490', 'Fesla Model Y : $46990', '']
    
    first = list[2]
    second = list[3]
    third = list[4]
    fourth = list[5]

    print(f"1. {first}\n"
          f"2. {second}\n"
          f"3. {third}\n"
          f"4. {fourth}\n")
    
    order_number = input("Enter the order number: ")
    customer_name = input("Customer Name: ")
    choice = input("Enter car choice: ")
    
    complement = {"1":first,
                  "2":second,
                  "3":third,
                  "4":fourth}

    with open(f"{order_number}.txt","a") as datafile2:
        datafile2.write(f"{customer_name} ordered the {complement[choice][0:13]} at {complement[choice][16:]}")

    print("Car has been successfully ordered.")