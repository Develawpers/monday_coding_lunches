from datetime import datetime


def ask_name():
    _name = input("What's your name? ")
    return _name


def ask_dob():
    _dob = input("What's your date of birth? (dd/mm/yyyy) ")
    _dob_obj = datetime.strptime("%d/%m/%Y")