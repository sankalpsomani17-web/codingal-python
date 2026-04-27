num = int(input("Enter a number: "))
count = 0

# Special case for 0
if num == 0:
    count = 1
else:
    # Use absolute value to handle negative numbers
    n = abs(num)
    while n > 0:
        n //= 10  # Integer division to remove the last digit
        count += 1

print(f"Total digits: {count}")
