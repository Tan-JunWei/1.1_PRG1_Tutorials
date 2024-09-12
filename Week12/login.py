# Tan Jun Wei
# S10266704C

# peter,pass1
# amy,pass2
# david,pass_david
# user4,user4

def read_accounts(accounts):
    accounts_list = []
    with open(accounts,"r") as file:
        for line in file:
            user = line.strip().split(",")
            accounts_list.append(user)

    return accounts_list

def login(user_name,password,accounts):
    for account in accounts:
        if user_name == account[0] and password == account[1]:
            return True
        else:
            return False

tries = 0

while tries < 3:
    name = input("Enter your user name: ")
    password = input("Enter your password: ")

    accounts = read_accounts("accounts.txt")

    if login(name,password,accounts):
        print(f"Hello {name.upper()}, you may proceed...")
        break

    else:
        print(f"Login incorrect. Please try again...")
    tries += 1

if tries == 3:
    print("You didn't get it in 3 attempts. Your account is locked")

