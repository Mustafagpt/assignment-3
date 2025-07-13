import math

# 1. Ask the user for a number as input.
# The float() function converts the user's text input into a number.
try:
    num = float(input("Enter a number: "))

    # 2. Calculate the required values using the math module.
    square_root = math.sqrt(num)
    natural_log = math.log(num) # This is log base e
    sine_of_num = math.sin(num) # Assumes the input number is in radians

    # 3. Display the calculated results.
    print(f"\n--- Results for {num} ---")
    print(f"Square Root: {square_root}")
    print(f"Natural Logarithm: {natural_log}")
    print(f"Sine: {sine_of_num}")

except ValueError:
    print("Invalid input. Please enter a number.")
except ValueError as e:
    # This will catch math domain errors, e.g., sqrt of a negative number
    print(f"An error occurred: {e}. Please check your input.")