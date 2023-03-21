"""
Control Flow
Else If Statements

We have if statements, we have else statements, we can also have elif statements.

Now you may be asking yourself, what the heck is an elif statement? It’s exactly what it sounds like, “else if”. An elif
statement checks another condition after the previous if statements conditions aren’t met.

We can use elif statements to control the order we want our program to check each of our conditional statements. First,
the if statement is checked, then each elif statement is checked from top to bottom, then finally the else code is
executed if none of the previous conditions have been met.

Let’s take a look at this in practice. The following if statement will display a “thank you” message after someone
donates to a charity; there will be a curated message based on how much was donated.
"""

print("Thank you for the donation!")

if donation >= 1000:
  print("You've achieved platinum status")
elif donation >= 500:
  print("You've achieved gold donor status")
elif donation >= 100:
  print("You've achieved silver donor status")
else:
  print("You've achieved bronze donor status")

"""
Take a second to think about this function. What would happen if all of the elif statements were simply if statements?
If you donated $1100.00, then the first three messages would all print because each if condition had been met.

But because we used elif statements, it checks each condition sequentially and only prints one message. If I donate
$600.00, the code first checks if that is over 1000, which it is not, then it checks if it’s over 500, which it is, so
it prints that message, then because all of the other statements are elif and else, none of them get checked and no more
messages get printed.

Try your hand at some other elif statements.
Instructions
1.

Calvin Coolidge’s Cool College has noticed that students prefer to get letter grades.

Write an if/elif/else statement that:

    If grade is 90 or higher, print "A"
    Else if grade is 80 or higher, print "B"
    Else if grade is 70 or higher, print "C"
    Else if grade is 60 or higher, print "D"
    Else, print "F"

The code should look something like:
"""

grade = 86

if grade >= 90:
  print("something")
elif grade >= 80:
  print("something else")
elif grade >= 70:
  print("something else")
elif grade >= 60:
  print("something else")
else:
  print("something else")

"""
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
########################################################################################################################

exo :

grade = 86

if grade >= 90:
  print("A")
elif grade >= 80:
  print("B")
elif grade >= 70:
  print("C")
elif grade >= 60:
  print("D")
else:
  print("F")
"""
