# Defining the tuple
numbers = (4, 3, 2, 2, -1, 18)

# Initializing product to 1
product = 1

# Multiplying each element
for num in numbers:
    product *= num

# Output the result
print(f"Original Tuple: {numbers}")
print(f"Product of all numbers: {product}")
