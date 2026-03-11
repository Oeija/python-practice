#1. Variables
first_name = "Vincent"
age = 21
gpa = 3.88
lockin = True

print(f"Hi, my name is {first_name} and im {age} years old.")
print(f"My GPA is {gpa}")

if lockin:
    print("You are really ready for becoming AI Solution Engineer!")
else:
    print("LOCK INNNN!")


#2. Typecasting
# str, int, float, bool
name = "Vincent Oei"
age = 21
gpa = 3.88
is_student = True

print(type(name))

gpa = int(gpa)
print(gpa)
is_student = str(is_student)
print(is_student)


#3. User Input
# input() function

name = input("What is your name?: ")
print(f"Hello {name}!")

age = int(input("What is your age?: "))
age += 1
print(f"You are {age}")


