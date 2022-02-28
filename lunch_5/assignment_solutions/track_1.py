from datetime import datetime


def ask_age():
    _age = int(input("What's your age? "))
    return _age


def ask_dob():
    _dob = input("What's your date of birth? (dd/mm/yyyy) ")
    _dob_obj = datetime.strptime(_dob, "%d/%m/%Y")
    return _dob_obj


def calc_age_in_days(_dob):
    td = datetime.now() - _dob
    return td.days


if __name__ == "__main__":
    age = ask_age()
    dob = ask_dob()
    age_in_days = calc_age_in_days(dob)
    declared_age_in_days = age * 365  # not super precise, but we don't care for now
    treshold = 180  # let's set a lying treshold at 6 months
    if abs(declared_age_in_days - age_in_days) > treshold:
        print("You're lying!")
    else:
        print("All good")

