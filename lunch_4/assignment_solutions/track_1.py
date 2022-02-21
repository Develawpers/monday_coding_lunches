"""
Track 1
Ask a user to enter their date of birth in dd/mm/YYYY format,
parse it into a datetime object, then print it again in the format equivalent to this:
`Monday, 14 of February 2022`
"""
from datetime import datetime

user_date_str = input("What's your date of birth? (dd/mm/YYYY) ")

user_date = datetime.strptime(user_date_str, "%d/%m/%Y")

print("Your date of birth is", user_date.strftime("%A, %d of %B %Y"))