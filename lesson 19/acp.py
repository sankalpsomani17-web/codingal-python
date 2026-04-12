import math

# Define the angle in degrees
angle_degrees = 45

# Convert degrees to radians
angle_radians = math.radians(angle_degrees)

# Calculate values
sine_val = math.sin(angle_radians)
cosine_val = math.cos(angle_radians)
tangent_val = math.tan(angle_radians)

# Display results
print(f"Angle: {angle_degrees}°")
print(f"Sin: {sine_val:.4f}")
print(f"Cos: {cosine_val:.4f}")
print(f"Tan: {tangent_val:.4f}")
