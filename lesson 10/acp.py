# Taking input from the user
base = float(input("Enter base number: "))
n = int(input("Enter exponent (n): "))

# Method 1: Using ** operator
result = base ** n

# Method 2: Using the built-in pow() function
# result = pow(base, n)

print(f"{base} raised to the power of {n} is: {result}")
