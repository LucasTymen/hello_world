"""
Control Flow
Boolean Variables

Before we go any further, let’s talk a little bit about True and False. You may notice that when you type them in the code editor (with uppercase T and F), they appear in a different color than variables or strings. This is because True and False are their own special type: bool.

True and False are the only bool types, and any variable that is assigned one of these values is called a boolean variable.

Boolean variables can be created in several ways. The easiest way is to simply assign True or False to a variable:
"""
set_to_true = True
set_to_false = False

"""
You can also set a variable equal to a boolean expression.
"""
bool_one = 5 != 7
bool_two = 1 + 1 != 2
bool_three = 3 * 3 == 9

"""
These variables now contain boolean values, so when you reference them they will only return the True or False values of the expression they were assigned.
"""
print(bool_one)    # True

print(bool_two)    # False

print(bool_three)  # True

"""Instructions
1.

Create a variable named my_baby_bool and set it equal to "true".

It should look something like:

variable_name = "some string"

2.

Check the type of my_baby_bool using type(my_baby_bool).

You’ll have to print it to get the results to display in the terminal.

You can print the type of a variable by running:

print(type(variable_name))

3.

It’s not a boolean variable! Boolean values True and False always need to be capitalized and do not have quotation marks.

Create a variable named my_baby_bool_two and set it equal to True.

Don’t forget to take out the double-quotes.
4.

Check the type of my_baby_bool_two and make sure you successfully created a boolean variable.

You’ll have to print it to get the results to display in the terminal.

You can print the type of a variable by running:

print(type(variable_name))

Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
"""
