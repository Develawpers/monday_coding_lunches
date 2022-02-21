"""
Track 3
Ask a user to enter their date of birth in a format of your choosing, different from dd/mm/YYYY,
then tell them how many days are left until their next birthday
"""
from datetime import datetime

user_date_str = input("What's your date of birth? (dd/mm/YYYY) ")

user_date = datetime.strptime(user_date_str, "%d/%m/%Y")

today = datetime.today()

this_years_bday = user_date.replace(year=today.year)

if this_years_bday > today:
    diffrence = this_years_bday - today
    days = diffrence.days
else:
    next_bday = user_date.replace(year=today.year + 1)
    diffrence = next_bday - today
    days = diffrence.days

print(f"There are {days} days until your next birthday")