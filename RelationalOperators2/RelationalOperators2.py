"""
Control Flow
Relational Operators II

Now that we’ve added conditional statements to our toolkit for building control flow, let’s explore more ways to create
boolean expressions. So far we know two relational operators, equals and not equals, but there are a ton (well, four)
more:

    > greater than
    >= greater than or equal to
    < less than
    <= less than or equal to

Let’s say we’re running a movie streaming platform and we want to write a program that checks if our users are over 13
when showing them a PG-13 movie. We could write something like:
"""
age =12
if age <= 13:
  print("Sorry, parental control required")

"""
This function will take the user’s age and compare it to the number 13. If age is less than or equal to 13, it will
print out a message.

Let’s try some more!
Instructions
1.

Create an if statement that checks if x and y are equal, print the string below if so:

"These numbers are the same"

Did you create an if statement that looks like:
"""
a=2
b=4
if a == b:
  print("some message")

"""
Also, make sure you copy the string response exactly.
2.

The nearby college, Calvin Coolidge’s Cool College (or 4C, as the locals call it) requires students to earn 120 credits
to graduate.

Write an if statement that checks if the student has enough credits to graduate. If they do, print the string:

"You have enough credits to graduate!"

Can a student with 120 credits graduate from Calvin Coolidge’s Cool College?

Make sure to use >= as the relational operator.

Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
https://www.codecademy.com/learn/learn-python-3/modules/learn-python3-control-flow/cheatsheet

########################################################################################################################
exercise :
x = 20
y = 20

# Write the first if statement here:
if x == y :  print ("These numbers are the same")


credits = 120

# Write the second if statement here:
if credits >= 120 : print("You have enough credits to graduate!")
else : print("try again next year")


"""
