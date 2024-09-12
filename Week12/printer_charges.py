# Tan Jun Wei
# S10266704C

def calculate_charge(pages):
    '''
    takes in the number of pages and return the corresponding charge
    '''

    if pages <= 100:
        cost = 0.03 * pages
    elif pages <= 300:
        cost = (0.03 * 100) + 0.02 * (pages - 100)
    else: 
        cost = (0.03 * 100) + 0.02 * (200) + 0.01 * (pages-300)

    return cost


def calculate_gst():
    '''
    takes in the amount and return the corresponding GST charged
    '''
    cost = calculate_charge(pages)
    include_gst = (9/100) * cost + cost
    return include_gst


print(f"{'Pages':<10}{'Charge($)':>10}{'Include gst($)':>20}")

for i in range(11):
    pages = i * 50
    print(f"{pages:<10}{calculate_charge(pages):>10.2f}{calculate_gst():>20.2f}")