"""
Normative references:
- art. 163-bis c.p.c. (terms of appearance)
- Article 165 c.p.c. (appearance of plaintiff)
- Article 166 c.p.c. (appearance of the defendant)
Subpoena:
- service: input
- hearing date: input (optional)
- foreign country: input (bool, default=False)
- first hearing: min 90 days from service (free)
- plaintiff appearance: 10 days after service
- appearance of the defendant: 20 days before the appearance hearing

According to law 27/5/1949, no. 260, modified by law 31/3/1954, no. 90 and law 5/3/1977, no. 54
are considered public holidays
- all Sundays
- January 1st
- 25th April
- the Monday after Easter
- 1 May,
- 15th August
- 1 November,
- 8, 25 and 26 December.
"""

import re
from datetime import datetime, timedelta


HOLIDAYS = [
    (1, 1), (6, 1), (25, 4), (1, 5), (2, 6), (15, 8), (1, 11), (8, 12), (25, 12), (26, 12)
]
# monday after easter


def is_holiday(date):
    if date.weekday() in (5, 6):  # saturday or sunday
        return True
    if (date.day, date.month) in HOLIDAYS:
        return True
    return False


def subpoena_deadlines():
    date_of_service_str = input("When was the subpoena serviced? (dd/mm/yyyy) ")
    foreign_country_str = input("Was the subpoena serviced abroad? (y/n) ")
    first_hearing_str = input("When is the first hearing set? (dd/mm/yyyy) ")

    date_of_service = datetime.strptime(date_of_service_str, "%d/%m/%Y")

    if re.match(r"y(es|eah)?", foreign_country_str, re.I):
        foreign_country = True
    else:
        foreign_country = False

    first_hearing = datetime.strptime(first_hearing_str, "%d/%m/%Y")

    if foreign_country:
        min_days = timedelta(days=152)
    else:
        min_days = timedelta(days=92)

    if first_hearing - date_of_service < min_days:
        print("The first hearing date is too soon. Calculating a new one")
        first_hearing = date_of_service + min_days

    while is_holiday(first_hearing):
        first_hearing += timedelta(days=1)

    plaintiff_appearance_date = date_of_service + timedelta(days=10)
    while is_holiday(plaintiff_appearance_date):
        plaintiff_appearance_date += timedelta(days=1)

    defendant_appearance_date = first_hearing - timedelta(days=20)
    while is_holiday(defendant_appearance_date):
        defendant_appearance_date += timedelta(days=1)

    print("Hearing date:", first_hearing.strftime("%d/%m/%Y"))
    print("Appearance of plaintiff,", plaintiff_appearance_date.strftime("%d/%m/%Y"))
    print("Appearance of defendant,", defendant_appearance_date.strftime("%d/%m/%Y"))


def arrest_order():
    print("Arrest order will be calculated soon")


DEADLINES = [
    ("Subpoena", subpoena_deadlines),
    ("Arrest order", arrest_order)
]


if __name__ == "__main__":
    print("Which deadlines would you like to calculate?")
    for i, (desc, func) in enumerate(DEADLINES):
        print(f"[{i}] {desc}")
    idx = int(input(">> "))
    func = DEADLINES[idx][1]
    func()