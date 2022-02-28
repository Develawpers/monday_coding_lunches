from datetime import datetime


def ask_name():
    return input("What is your name? ")


def ask_dob():
    _dob = input("What's your date of birth? (dd/mm/yyyy) ")
    _dob_obj = datetime.strptime(_dob, "%d/%m/%Y")
    return _dob_obj


def calculate_age(_dob):
    today = datetime.today()
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


def gather_data(_name, _age, _dob, _can_drink, **kwargs):
    data = dict(
        name=_name,
        age=_age,
        dob=_dob.strftime("%d/%m/%Y"),
        can_drink=str(_can_drink),
        **{k: str(v) for k, v in kwargs.items()}
    )
    return data


if __name__ == "__main__":
    name = ask_name()
    dob = ask_dob()
    age = calculate_age(dob)
    all_data = gather_data(name, age, dob, can_drink(age), location="EU", eyes="Brown", height=1.80)
    print(all_data)