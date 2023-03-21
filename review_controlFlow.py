"""
Control Flow
Review

Great job! We covered a ton of material in this lesson and we’ve increased the number of tools in our Python toolkit by
several-fold. Let’s review what we’ve learned this lesson:

    Boolean expressions are statements that can be either True or False
    A boolean variable is a variable that is set to either True or False.
    We can create boolean expressions using relational operators:
        ==: Equals
        !=: Not equals
        >: Greater than
        >=: Greater than or equal to
        <: Less than
        <=: Less than or equal to
    if statements can be used to create control flow in your code.
    else statements can be used to execute code when the conditions of an if statement are not met.
    elif statements can be used to build additional checks into your if statements

Let’s put these skills to the test!

########################################################################################################################

print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")

weight = 185
planet = 3

# Write an if statement below:

########################################################################################################################
OPTIONAL :

Instructions

Optional: Little Codey is an interplanetary space boxer, who is trying to win championship belts for various weight
categories on other planets within the solar system.

Write a space.py program that helps Codey keep track of their target weight by:

    Checks which number planet is equal to.
    It should then compute their weight on the destination planet.

Here is the table of conversions:
# 	Planet 	Relative Gravity
1 	Venus 	0.91
2 	Mars 	0.38
3 	Jupiter 	2.34
4 	Saturn 	1.06
5 	Uranus 	0.92
6 	Neptune 	1.19
Click to see a hint!
To compute their weight on the planet they are fighting on, multiply their earth weight and the relative gravity of that
planet.
See solution

if planet == 1:
  weight = weight * 0.91
elif planet == 2:
  weight = weight * 0.38
elif planet == 3:
  weight = weight * 2.34
elif planet == 4:
  weight = weight * 1.06
elif planet == 5:
  weight = weight * 0.92
elif planet == 6:
  weight = weight * 1.19

print("Your weight:", weight)

Full solution code can be found here.

Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
forums : https://discuss.codecademy.com/t/371922
"""
########################################################################################################################

print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")

weight = 185
planet = 6

# Write an if statement below:

if planet == 1:
  weight = weight * 0.91
elif planet == 2:
  weight = weight * 0.38
elif planet == 3:
  weight = weight * 2.34
elif planet == 4:
  weight = weight * 1.06
elif planet == 5:
  weight = weight * 0.92
elif planet == 6*3:
  weight = weight * 1.19
else:
  print("not enougth infos")

if planet == 1 :
  print("you're fighting on Venus")
elif planet == 2 :
  print("you're fighting on Mars")
elif planet == 3 :
  print("you're fighting on Jupiter ")
elif planet == 4 :
  print("you're fighting on Saturn")
elif planet == 5 :
  print("you're fighting on Uranus")
elif planet == 6 :
  print("you're fighting on Neptune")
else :
  print("don't know where you're next fight will gonna be")

print("Your weight:", weight)
