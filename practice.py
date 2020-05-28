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
#  elements from the original list a that are smaller than that number
#  given by the user.


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

# Take two lists, say for example these two:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains
# only the elements that are common
# between the lists (without duplicates). Make sure your
# program works on two lists of different sizes.


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for i in b:
    if i in a:
        c.append(i)
print(c)

# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

print("Please Enter a Word")
wrd = input()
rvs = wrd[::-1]
print(rvs)
if wrd == rvs:
    print("This is a palindrome")

# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
# Write one line of Python that takes this list a and makes a new list that has only the even
# elements of this list in it.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [number for number in a if number % 2 == 0]
print(b)

# Make a two-player Rock,Paper,Scissors Game (Ask for player plays (Using input )
# Compare them ,print out a message congratulation to the winner
# and ask if the players want to start a new game)

import sys

print("What's Your Name")
user1 = input()
print("What's Your Name")
user2 = input()
print("%s Do you want to choose ROCK,PAPER or SCISSORS ?" % user1)
user1_answer = input()
print("%s Do you want to choose ROCK,PAPER or SCISSORS ?" % user2)
user2_answer = input()


def compare(u1, u2):
    if u1 == u2:
        return "It's a tie"
    elif u1 == "rock":
        if u2 == "scissors":
            return "Rock Wins"
        else:
            return "Paper Wins"

    elif u1 == "scissors":
        if u2 == "paper":
            return "Scissors Wins"
        else:
            return "Rock Wins"

    elif u1 == "paper":
        if u2 == "rock":
            return "Paper Wins"
        else:
            return "Scissors Wins"
    else:
        return "Invalid input! You have not entered rock, paper or scissors, try again."


print(compare(user1_answer, user2_answer))

sys.exit()

# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right

import random

number = random.randint(1, 9)
guess = 0
count = 0
print("Hello,What is You Name ?\nI Will Like To Play a Game With You\n Which is Guess The Number")
name = input()

while guess != number and guess != "exit":
    print(name + " What is Your Guess")
    guess = input()
    if guess == "exit":
        break

    guess = int(guess)
    count += 1

    if guess < number:
        print(name + " Your Guess is Too Low")
    elif guess > number:
        print(name + " Your Guess is Too High")

    else:
        print(name + " You Got it")
    print("And it Only Took You ", count, "Tries")

# This week’s exercise is going to be revisiting an old exercise (see Exercise 5)
# except require the solution in a different way.
#
# Take two lists, say for example these two:
#
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between
# the lists (without duplicates). Make sure your program works on two lists of different sizes

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
result = []
for i in b:
    if i in a:
        result.append(i)
print(result)


def get_integer(help_text):
    return int(input(help_text))


age = get_integer("Tell me your age ")
school_year = get_integer("What grade are you in ? ")
if age > 15:
    print("You are over the age of 15")
print("You are in Grade " + str(school_year))

num = int(input("Insert a Number "))
a = [x for x in range(2, num) if num % x == 0]


def is_prime():
    if num > 1:
        if len(a) == 0:
            print("Prime")
        else:
            print("Not a Prime")
    else:
        print("Not Prime")


is_prime()


# Write a program that asks the user how many Fibonacci numbers to generate
# and then generates them. Take this opportunity to think about how you can
# use functions. Make sure to ask the user to enter the number of numbers in
# the sequence to generate.(Hint: The Fibonacci sequence is a sequence of numbers
# where the next number in the sequence is the sum of the previous two numbers in
# the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

def fibonacci():
    global finac
    num1 = int(input("How many numbers to generates ? "))
    bah = 1
    if num1 == 0:
        finac = []
    elif num1 == 1:
        finac = [1]
    elif num1 == 2:
        finac = [1, 1]
    elif num1 > 2:
        finac = [1, 1]
        while bah < (num1 - 1):
            finac.append(finac[1] + finac[1 - 1])
            bah += 1
    return finac


print(fibonacci())
input()
