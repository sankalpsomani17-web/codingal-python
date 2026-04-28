try:
    # Ask the user to enter their age
    age = int(input("Enter your age: "))

    # Check if the age is "correct" (non-negative and within a realistic range)
    if age < 0 or age > 120:
        print("Error: The age entered is incorrect. Please enter a valid age between 0 and 120.")
    else:
        print(f"The age entered ({age}) is valid.")

        # Check if the age is even or odd
        if age % 2 == 0:
            print("The age is even.")
        else:
            print("The age is odd.")

except ValueError:
    # Handle cases where the input is not a whole number
    print("Error: Invalid input. Please enter a numerical value for age.")
