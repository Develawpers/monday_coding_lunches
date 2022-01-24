"""
Ask a user for their name
Ask a user where they live
Ask a user for their age
If they live in "USA" *and* they are below 21, tell them that they cannot drink, but they can have a gun instead
Else, if they live in "USA" *and* their age is greater than or equal to 21, tell them that they can have both a gun and a beer
Else, if they do not live in "USA" *and* their age is greater than or equal to 18, tell them that they can have a beer, but not a gun
Else, tell them that they can have neither

PRO TIP: you can combine `if` statements using the `and` clause, like so: `if a == 10 and b > 5:`
"""

# There are many valid ways to solve this one!

name = input("What is your name? ")
location = input("Where do you live? ")
age = int(input("What is your age? "))

if location == "USA":
    if age < 21:
        print(name, ", you cannot drink, but you can have a gun instead!")
    else:
        print(name, ", you can have both a beer and a gun!")
elif age >= 18:
    print(name, ", you can have a beer, but not a gun!")
else:
    print(name, ", you can have neither a beer, nor a gun!")