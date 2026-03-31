def factorial(x):
    """this is a recursive fuction to find the factorial of integer"""

    if x==0 or x==1 :
        return 1
    else:
        return x*factorial(x-1)
print(factorial.__doc__)
print("the factorial of 0:",factorial(0))
print("the factorial of 2:",factorial(2))
print("the factorial of 5:",factorial(5))