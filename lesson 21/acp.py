# Get start and end range from the user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Create lists to hold the results
even_squares = []
odd_squares = []

# Iterate through the range (inclusive of the end value)
for num in range(start, end + 1):
    square = num ** 2
    
    # Check if the squared value is even or odd
    if square % 2 == 0:
        even_squares.append(square)
    else:
        odd_squares.append(square)

# Display the results
print(f"Even squares: {even_squares}")
print(f"Odd squares: {odd_squares}")

