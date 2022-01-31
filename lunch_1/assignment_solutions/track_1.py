"""
TRACK 1
Ask the user for their name, making sure that the value is assigned in Title Case
Ask the user for their age, and if they don't enter a valid digit, tell them so and that they have to start over
Ask the user for their location, and make it in upper case. 

Print out their info using an f-string, so that the output looks like this:
"
Here's your info:
name: Max
age: 28
location: VIENNA
"
"""

name = input("What is your name? ").title()
age = input("What is your age? ")

if age.isdigit():
    location = input("What is your location? ").upper()
    info = f"Here's your info:\nname: {name}\nage: {age}\nlocation: {location}"
    print(info)
else:
    print("age is not a valid digit. Please start over!")
