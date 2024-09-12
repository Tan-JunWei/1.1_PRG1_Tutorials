# Tan Jun Wei (S10266704) - CSF02

sales_list = []

with open("revision_sales.txt","r") as file:
    for line in file:
        line = line.strip().split(",")
        sales_list.append(line)

# print 1(a) output
print(sales_list)


product_list = ['MacBook Air', 'MacBook Pro', 'iMac']
Total_units_list = [0, 0, 0]

# print first part of 1(b) output
for i in range(len(sales_list)):
    print(f"{sales_list[i][0]:<15}{sales_list[i][1]:<15}{sales_list[i][2]}")

    for z in range(len(sales_list[i])):  # use z so that count can be added up using z+1 after identifying the index of product
        for b in range(len(product_list)):
            if sales_list[i][z] == product_list[b]:
                Total_units_list[b] += int(sales_list[i][z+1])

# print second part of 1(b) output
print(f"\n{'Product':<15}{'Total Units Sold':<20}")
for x in range(len(Total_units_list)):
    print(f"{product_list[x]:<15}{Total_units_list[x]:<20}")





