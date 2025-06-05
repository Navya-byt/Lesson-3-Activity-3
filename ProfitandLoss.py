og_price = int(input("Enter the orginal price"))
rate = int(input("Enter the rate at which the product was sold"))
if(rate>og_price):
    amount = rate-og_price
    print("Total profit is",amount)
else: 
    print("Loss")
    