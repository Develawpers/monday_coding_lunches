"""
TRACK 1
Use regex to validate a user-input email that
can contain letters, numbers and the special characters `.-+`
"""

import re

email_pattern = r"(?P<username>([a-z0-9]+[-+.]?)+[a-z0-9])@(?P<domain>([a-z0-9]+\.?)+\.[a-z]{2,4})"

email = input("What is your email? ")

if re.match(email_pattern, email):
    print("The email is valid")
else:
    print("The email is NOT valid")


# however, take into account this:
# https://stackoverflow.com/questions/201323/how-can-i-validate-an-email-address-using-a-regular-expression

