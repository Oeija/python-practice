name = input("What is your name?: ")

result = len(name)
result = name.find("a")
result = name.rfind("a")
# if python not find, resulting -1
print(result)

name = name.capitalize() # only the first letter of the string is capitalize
name = name.upper() # all uppercase
name = name.lower() # all lowercase
print(name)

result = name.isdigit() # check if all characters in the string are digits (no spaces and alphabet)
result = name.isalpha() # check if all characters in the string are letters (no spaces and digits)
result = name.isalnum() # check if all characters in the string are letters or digits (no spaces and special chars)
print(result)