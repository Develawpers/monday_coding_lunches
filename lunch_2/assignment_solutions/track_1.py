"""
TRACK 1
Ask the user for their name, making sure that the value is assigned in Title Case
Ask the user for their age, and if they don't enter a valid digit, tell them so and that they have to start over
Ask the user for their location, and make it in upper case. 

Save the info in a dict and print it out
"""

info = dict()

info["name"] = input("What is your name? ").title()
info["age"] = input("What is your age? ")

if info["age"].isdigit():
    info["location"] = input("What is your location? ").upper()
    print("Here's your info:", info)
else:
    print("age is not a valid digit. Please start over!")
