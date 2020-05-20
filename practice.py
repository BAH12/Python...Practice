# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they
# will turn 100 years old.

print("What is Your Name ?")
name = input()
print("What is Your Age ?")
age = int(input())
year = str((2020 - age) + 100)
print(name + " Will be 100 years old in a year " + year)

# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user.

print("Enter a Number of Your Choice")
num = int(input())
mod = num % 2
if mod > 0:
    print("You picked an 'ODD' Number")
else:
    print("You picked an 'EVEN' Number")

#  Ask the user for a number and return a list that contains only
#  elements from the original list a that are smaller than that number given by the user.
#
print("Choose a number from this list \n(1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89):")
list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
user_choice = int(input())
if user_choice not in list1:
    print("You didn't picked a number from the list")
elif user_choice in list1:
    print("Correct, you have picked a number from the list")
    print("Thank You")

# Create a program that asks the user for a number and then
# prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

print("Please choose a number to divide")
num = int(input())
list_Range = list(range(1, num + 1))
divisor_list = []
for number in list_Range:
    if num % number == 0:
        divisor_list.append(number)
print(divisor_list)