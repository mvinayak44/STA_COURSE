'''money = (input("Available Money:"))
print(bool(money))


#1'''
'''
r = float(input("Radius of circle:"))
area = ((22/7) * r**2)
print(round(area))
'''

#did_you = input("Did you do it?")
#print(did_you)
#else
#print("Very Good")
'''

spicyfood = input("Do you like spicy food? True or False?")
if spicyfood == "True":
return (True)
if spicyfood == "False":
	return (False)
'''
'''
closing_price1 = int(input("Enter Closing prices of 'n'th day:"))
closing_price2 = int(input("Enter Closing prices of 'n-1'th day:"))
closing_price3 = int(input("Enter Closing prices of 'n-2'th day:"))
average = ((closing_price1 + closing_price2 + closing_price3) / 3)
print("Average price is", average)

'''
#input of previous day prices

High = float(input("Previous day high price:"))
Low = float(input("Previous day low price:"))
Close = float(input("Previous day close price:"))
#formula to calculation of pivots
Pivot = (High + Low + Close)/3
R1 = (2*Pivot) - Low
S1 = (2*Pivot) - High
R2 = Pivot + (High - Low)
S2 = Pivot - (High - Low)
R3 = R1 + (High - Low)
S3 = S1 - (High - Low)
print("Pivot is",round(Pivot))
print("R1 is", R1)
print("S1 is", S1)
print("R2 is", R2)
print("S2 is", S2)
print("R3 is", R3)
print("S3 is", S3)
