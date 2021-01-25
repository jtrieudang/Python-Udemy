#Data Types

#String

print("Hello"[4])
# gives the first letter of the character, subscripting, it starts from 0

# Integer
print(123+234)

# Float = decimal, decimal is like floating around

# Boolean is True or False

num_char = len(input("What is your name?"))
# this converts the length of the name into a string
new_num_char = str(num_char)
# the string converts it into the print length into a print statement
print("Your name has " + new_num_char + " characters.")

# Practice
pet_leg = len(input("Type out any letters to represent the legs your pet has?\n"))

pet_leg_string = str(pet_leg)

print("Your pet has only " + pet_leg_string + " legs?")