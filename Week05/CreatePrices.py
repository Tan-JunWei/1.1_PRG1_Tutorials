#Student name: Tan Jun Wei
#Student ID: S10266704C

prices = [ ["kopi",0.4], ["teh",0.4], ["milo",0.5], ["soft drinks",1.20] ]

with open("prices.txt","a") as datafile:
    datafile.write(f"{prices[0][0]}: ${prices[0][1]:.2f}\n")
    datafile.write(f"{prices[1][0]}: ${prices[1][1]:.2f}\n")
    datafile.write(f"{prices[2][0]}: ${prices[2][1]:.2f}\n")
    datafile.write(f"{prices[3][0]}: ${prices[3][1]:.2f}\n")