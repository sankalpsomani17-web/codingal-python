odd = []
even = []
num=int(input("enter a number"))
for i in range (num):
    n=int(input("enter a number in list"))
    if n%2==0:
        even.append(n)
    else:
        odd.append(n)
print(f"odd list equals{odd}")
print(f"odd list equals{even}")