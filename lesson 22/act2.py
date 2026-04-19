def palid(r):
    return r==r[::-1]

r = (1,2,3,3,2,1)

if(palid(r)):
    print("the tuple is flip-flop")
else:
    print("the tuple is not flip-flop")