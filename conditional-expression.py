import math

# a one-line shortcut for if-else statement (ternary operator)
# X if condition else Y (return X if condition else Y)

num = 5

print("Positive" if num > 0 else "Negative")
result = "EVEN" if num % 2 == 0 else "ODD"
print(result)

a = 9
b = 10

magic = a if math.sqrt(a) == 4 else b
print(magic)