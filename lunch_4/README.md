# Lunch 4

## Date Manipulation

Python offers the built-in datetime library to deal with date and time objects.

See the full documentation [here](https://docs.python.org/3/library/datetime.html)

To use the library, we need to import it. In this case, unlike in the previous lunch,
it is more conveniente to import specific sub-modules, funcions and classes of the library

We do like this:

```shell
>>> from datetime import date
```

Say we want to create a date object that represent's the 14th of February 2022

```shell
>>> today = date(2022, 2, 14)
>>> today
datetime.date(2022, 2, 14)
```

We can access some properties and methods of this object.

```shell
>>> today.year
2022
>>> today.month
2
>>> today.day
14
>>> today.isoformat()
'2022-02-14'
>>> today.weekday()
0   # <--- it's Monday!
>>> 
```

We can play around with dates using the `timedelta` object:

```shell
>>> from datetime import timedelta
>>> td = timedelta(days=1)
>>> tomorrow = today + td
>>> tomorrow
datetime.date(2022, 2, 15)
```

You can query timedelta objects:

```shell
>>> td.days
1
```

Date objects can be used with the `==`, `<` and `>` operators.

```shell
>>> today == date(2022, 2, 14)
True
>>> today < tomorrow
True
>>> today > tomorrow
False
```

You can also `subtract` dates; a timedelta will be returned:

```shell
>>> today = date(2022, 2, 14)
>>> tomorrow = date(2022, 2, 15)
>>> tomorrow - today
datetime.timedelta(days=1)
>>> today - tomorrow
datetime.timedelta(days=-1)
```

However, you cannot add dates:

```shell
>>> today + tomorrow
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'datetime.date' and 'datetime.date'
```

### Date formatting
We can format `date` and `datetime` objects into strings using `.strftime()`

You can read the [full documentation here](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)

A brief example:

```shell
>>> today = date(2022, 2, 14)
>>> today.strftime("%d/%m/%Y")
'14/02/2022'
>>> today.strftime("%A, %dth of %B %Y")
'Monday, 14th of February 2022'
```

### Date parsing
Vice-versa, we can parse strings into `datetime` objects

You can read the [full documentation here](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)

A brief example:

```shell
>>> today_str = "14/02/2022"
>>> datetime.strptime(today_str, "%d/%m/%Y")
datetime.datetime(2022, 2, 14, 0, 0)
>>> today_str_fancy = "Monday, 14th of February 2022"
>>> datetime.strptime(today_str_fancy, "%A, %dth of %B %Y")
datetime.datetime(2022, 2, 14, 0, 0)
```
