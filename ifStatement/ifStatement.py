"""
Control Flow
If Statement

“Okay okay okay, boolean variables, boolean expressions, blah blah blah, I thought I was learning how to build control
flow into my code!”

You are, I promise you!

Understanding boolean variables and expressions is essential because they are the building blocks of conditional
statements.
https://www.codecademy.com/resources/docs/python/conditionals?page_ref=catalog

Recall the waking-up example from the beginning of this lesson. The decision-making process of “Is it raining? If so,
bring an umbrella” is a conditional statement.

Here it is phrased in a different way:

If it is raining, then bring an umbrella.

Can you pick out the boolean expression here?

Right, "it is raining" is the boolean expression, and this conditional statement is checking to see if it is True.

If "it is raining" == True then the rest of the conditional statement will be executed and you will bring an umbrella.

This is the form of a conditional statement:

If [it is raining], then [bring an umbrella]

In Python, it looks very similar:
"""

if is_raining:
  print("bring an umbrella")


"""
You’ll notice that instead of “then” we have a colon, :. That tells the computer that what’s coming next is what should
be executed if the condition is met.

Let’s take a look at another conditional statement:
"""

if 2 == 4 - 2:
  print("apple")

"""
Will this code print apple to the terminal?

Yes, because the condition of the if statement, 2 == 4 - 2 is True.

Let’s work through a couple more together.
Instructions
1.

In script.py, there is an if statement. I wrote this because my coworker Dave kept using my computer without permission
and he is a real doofus. If the user_name is Dave, it tells him to stay off my computer.

Enter a user name in the field for user_name and try running the program.

On line 2, give user_name a string value:


user_name = "sonnynomnom"


2.

Oh no! We got a SyntaxError! This happens when we make a small error in the syntax of the conditional statement.

Read through the error message carefully and see if you can find the error. Then, fix it, and run the code again.

There should be an error message that looks like this:

 File "script.py", line 4
    if user_name = "Dave":
                 ^
SyntaxError: invalid syntax

Take a close look at the relational operator in the if statement. Is it correct?

Remember, in Python = is used to assign a value to a variable, where == is a relational operator used to see if two
items are equal to each other.

Note: If you set user_name to something other than "Dave", you’ll notice that nothing is printed in the terminal.
3.

Ugh! Dave got around my security and has been logging onto my computer using our coworker Angela’s user name,
angela_catlady_87.

Set your user_name to be angela_catlady_87.

Update the program with a second if statement so it checks for Angela’s user name as well and prints

"I know it is you, Dave! Go away!"

in response. That’ll teach him!

This should have the form:
"""

if user_name == "Dave":
  print("Get off my computer Dave!")

if user_name == "blah":
  print("A different message")

"""
Don’t forget the double equal sign == and the colon :.
#################################################################
"""
