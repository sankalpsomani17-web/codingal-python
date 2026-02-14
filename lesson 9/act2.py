units=int(input("enter number of units consumed"))
if units < 50:
    amount, surchager = units * 2.60,25
elif  units <=100:
    amount, surchager = 130 + (units-50) *3.25, 35
elif units <=200:
    amount,surchager = 130 +162.50 + (units - 100) * 5.26 , 45
else:
    amount , surchager = 130 + 162.50 + 526 (units -200 ) * 8.45,75
print(f"elecricity bill = {amount+ surchager:2f}")