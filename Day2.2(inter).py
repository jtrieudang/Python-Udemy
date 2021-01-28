# 3 + 5
# 7 - 4
# 3 * 2
# # float
# 6 / 3
# # to the power of
# 2 ** 3
# PEMDA
# ()
# **
# *
# /
# + or -
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# BMI = int(float(weight) / (int(height ** 2)))
# print(BMI)


# solution

bmi = int(weight) / float(height) ** 2
# weight needs to be a float to not give the error below
bmi_as_ont = int(bmi)
print(bmi_as_ont)

# Note that putting a decimal value on height will give an error 
# because it is not a float. need to change it into a float