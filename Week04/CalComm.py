#Student Name: Tan Jun Wei
#Student ID: S10266704C

monthly_sales = int(input("Enter monthly sales of sales agent:"))

if monthly_sales >= 10000:
    commission_rate = 10
    commission = commission_rate/100 * monthly_sales
else: 
    commission_rate = 5
commission = commission_rate/100 * monthly_sales
print(f"The commission rate is : {commission_rate}%")
print(f"The commission paid is : ${commission:.2f}")