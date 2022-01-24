"""
TRACK 1
Ask a user for their name
Ask a user where they live
If the answer is "USA", tell them that the drinking age is 21
Else, tell them that the drinking age is 18
"""

name = input("What is your name? ")
location = input("Where do you live? ")

if location == "USA":
    print("Hello, ", name, ", the drinking age where you live is 21")
else:
    print("Hello, ", name, ", the drinking age where you live is 18")