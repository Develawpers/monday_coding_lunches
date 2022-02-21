"""
Track 2
Ask a user to enter their date of birth in dd/mm/YYYY format, parse it into a datetime object,
then tell them how old they are in days and what day of the week they were born
"""
from datetime import datetime

user_date_str = input("What's your date of birth? (dd/mm/YYYY) ")

user_date = datetime.strptime(user_date_str, "%d/%m/%Y")

diffrence = datetime.today() - user_date
days = diffrence.days

print(f"You are {days} old")