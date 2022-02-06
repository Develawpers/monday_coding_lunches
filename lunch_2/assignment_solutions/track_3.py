"""
TRACK 3

Given the list of tuples `data = [("name", "Max"), ("role", "prosecutor"), ("trial", "5/2022")]`
create a `dict` out of it using a for loop and unpacking.
"""

data = [("name", "Max"), ("role", "prosecutor"), ("trial", "5/2022")]

data_dict = dict()

for key, value in data:
    data_dict[key] = value

print(data_dict)