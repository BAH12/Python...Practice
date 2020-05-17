#  Create a program that asks the user to enter their name and their age.
#  Print out a message addressed to them that tells them the year that they
#  will turn 100 years old.

print("What is Your Name ?")
name = input()
print("What is Your Age ?")
age = int(input())
year = str((2020 - age) + 100)
print(name + " Will be 100 years old in a year " + year)
