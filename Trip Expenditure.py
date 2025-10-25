def hotelcost(nights):
    return 140*nights
def planecost (city):
    if "Charlotte" == city:
        return 183
    elif "Tampa" == city:
        return 220
    elif "Pitsburgh" == city:
        return 222
    elif "Los Angles" == city:
        return 475
def rentalcar(days):
    if days >=7:
        return 40*days-50
    elif days >=3:
        return 40*days-20
    else:
        return 40*days
def tripcost(city,days,spentmoney):
    return rentalcar(days)+hotelcost(days)+planecost(city)+spentmoney
print("Cost of car rental",rentalcar(5))
print("cost of plane ride",planecost("Los Angles"))
print("Cost of hotel room",hotelcost(7))
print("Total Cost of the trip",tripcost("Los Angles",7,500))
print(tripcost("Tampa",6,500))