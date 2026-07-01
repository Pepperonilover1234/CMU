# HW401_2 - Binary to ASCII Converter
# Input: 8-digit binary number
# Output: Decimal value and corresponding ASCII character

# Read 8-digit binary input
binary_input = input()

# Convert binary to decimal
decimal_value = int(binary_input, 2)

# Convert decimal to ASCII character
ascii_character = chr(decimal_value)

# Print output: decimal value and character separated by space
print(decimal_value, ascii_character)
