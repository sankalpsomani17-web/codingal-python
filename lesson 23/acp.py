# Sample dictionary
test_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 1}

# Value to check
target_value = 1

# Calculate frequency
frequency = list(test_dict.values()).count(target_value)

print(f"The frequency of {target_value} is: {frequency}")
