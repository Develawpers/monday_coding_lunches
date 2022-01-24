"""
Assume that the legal age for driving is 18
Ask a user for their name
Ask a user for their age
If their age is below the driving age, tell them how many years they have to wait to drive
Else if their age is equal to or greater than the driving age plus 10, tell them they have to renew their driver's license
Else tell them that they can enjoy driving
"""

legal_age_for_driving = 18

name = input("What is your name? ")
age = int(input("What is your age? "))

if age < legal_age_for_driving:
    years_left = legal_age_for_driving - age
    print("I'm sorry", name, ", you have to wait", years_left, " years to drive!")
elif age >= legal_age_for_driving + 10:  # elif is a shortcut for else if
    print(name, ", you have to renew your license! It expired", age - (legal_age_for_driving + 10), "years ago!")
else:
    print("Thank you,", name, ", enjoy driving!")