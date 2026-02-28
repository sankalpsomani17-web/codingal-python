rowSize=int(input("enter the number of rows:"))
half=rowSize//2 + rowSize%2
for i in range(1,half+1):
    for s in range(half-i):
        print(" ",end='')
    for num in range (1,2 * i):
        print(num,end='')
    print()

for i in range (half-1,0,-1):
    for s in range(half-i):
        print(" ",end='')
    for num in range (1,2 * i):
        print(num,end='')
    print()
