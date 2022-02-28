
def ask_name():
    return input("What is your name? ")


def ask_dob():
    _dob = input("What's your date of birth? (dd/mm/yyyy) ")
    _dob_obj = datetime.strptime(_dob, "%d/%m/%Y")
    return _dob_obj


def calculate_age(_dob):
    today = date.today()
    return today.year - _dob.year - ((today.month, today.day) < (_dob.month, _dob.day))


def can_drink(_age, location="EU"):
    if location == "EU":
        if age >= 18:
            return True
        else:
            return False
    elif location == "US":
        if age >= 21:
            return True
        else:
            return False
    return False


if __name__ == "__main__":
    name = ask_name()
    dob = ask_dob()
    age = calculate_age(dob)
    print(can_drink(age))