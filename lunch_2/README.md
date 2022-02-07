# Lunch 2

## Iterables

To put it simply, `iterables` are Python `objects` capable of returning their members one at a time (looping through them).

Iterables have some specific methods and properties that are key to understand to write proper python code.

Python's iterables are:

- lists: `list`
- dictionaries: `dict`
- tuples: `tuple`
- sets: `set`
- strings: `str`

We can loop through iterables with the `for` operator; the so-called `for loop`.

## Lists

Without going into the details of the magic behind it, a list in python is just that -- a list of values, defined using square brackets, like so:

```shell
>>> people = ["judge", "lawyer", "defendant"]
```

Even though it's not always best practice, lists can have mixed types within them:

```shell
>>> elements = ["apple", "banana", 127, "mango", 8.95]
```

You can add elements to a list using the `.append()` method:

```shell
>>> people.append("plaintiff")
>>> people
['judge', 'lawyer', 'defendant', 'plaintiff']
```

Unlike the methods of `str` objects, `list` methods work `in-place`. They will change the list itself and not return a new list.

The opposite of `.append()` is `.pop()`. It will remove the last element of the list, returning its value, like so:

```shell
>>> people.pop()
'plaintiff'
>>> people
['judge', 'lawyer', 'defendant']
>>>
```

You can also `.remove()` specific elements, like so:

```shell
>>> people.remove("lawyer")
>>> people
['judge', 'defendant']
>>> 
```

But if the element you want to remove is not there, it will raise an error:

```shell
>>> people.remove("plaintiff")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
>>> 
```

List elements are accessible via their index, like we saw with strings:

```shell
>>> people = ["judge", "lawyer", "defendant", "plaintiff"]
>>> people[2]
'defendant'
>>> people[-1]
'plaintiff'
```

Same goes for slicing:

```shell
>>> people[1:3]
['lawyer', 'defendant']
```

Slicing will return a new list.

## The for loop

Let's say that we want to access every member of the list one by one. We do so using the `for loop`:

```shell
>>> for person in people:
...     print(person)
... 
judge
lawyer
defendant
plaintiff
```

It is possible to check ownership with the `in` operator, like so:

```shell
>>> "lawyer" in people
True
>>> "prosecutor" in people
False
```

Sometimes you might want to loop through numbers from a certain to another. We can do that using a
`for loop` with the `range()` method:

```shell
>>> for number in range(5):
...     print(number)
... 
0
1
2
3
4
```

or:

```
>>> for number in range(5, 10):
...     print(number)
... 
5
6
7
8
9
```

### Sort

Lists have a built-in `.sort()` method. It is very powerful in terms of its handiness (not necessarily performance-wise) and it is possible to customise it. As of now, just take it as it is:

```shell
>>> numbers = [5, 1, 3, 2, 0, 4]
>>> numbers.sort()
>>> numbers
[0, 1, 2, 3, 4, 5]
```

## Dictionaries

A dictionary is a python built-in type that is used to save data in `key:value` pairs.

NOTE: As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

A dictionary can be declared in many ways, such as:

```shell
>>> person = {"name": "Max", "role": "prosecutor", "trial": "5/2022"}
```

or:

```shell
>>> person = dict(name="Max", role="prosecutor", trial="5/2022")
```

We can create new `key:value` pairs or overwrite existing like so:

```
>>> person["age"] = 30
```

To access a value given its key, we do like so:

```shell
>>> person["name"]
'Max'
```

However, if the `person` dictionary does not have the key we're looking for, it will raise an exception:

```shell
>>> person["age"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'age'
```

We can check if a `dict` has a specific key using the `in` operator:

```shell
>>> "age" in person
False
>>> "name" in person
True
```

If we want to access a value, but we're not sure if the `dict` has a certain key, we can use the `.get()` method:

```shell
>>> person.get("age")
>>> person.get("role")
'prosecutor'
```

if the key is not present, it will return `None` (or the default value provided: `.get("key", "default value")`)

Dictionaries have some useful built-in methods, such as `.keys()` and `.values()`, that will return respectively an iterable of its keys and values.

```shell
>>> person.keys()
dict_keys(['name', 'role', 'trial'])
>>> person.values()
dict_values(['Max', 'prosecutor', '5/2022'])
```

Another neat method is `.items()` that will return a list of tuples of the key:value pairs:

```shell
>>> person.items()
dict_items([('name', 'Max'), ('role', 'prosecutor'), ('trial', '5/2022')])
```

of course, you can loop through them:

```shell
>>> for key in person.keys():
...     print(key, person[key])
... 
name Max
role prosecutor
trial 5/2022
```

or:

```shell
>>> for value in person.values():
...     print(value)
... 
Max
prosecutor
5/2022
```

or:

```shell
>>> for key, value in person.items():
...     print(key, value)
... 
name Max
role prosecutor
trial 5/2022
```

Here in the last example we use unpacking, that we'll see better in a bit.

## Tuples

A `tuple` is similar to a list, except it is immutable:

```shell
>>> people_tuple = ('judge', 'lawyer', 'defendant', 'plaintiff')
```

You can create a tuple from another iterable:

```shell
>>> people = ['judge', 'lawyer', 'defendant', 'plaintiff']
>>> tuple(people)
('judge', 'lawyer', 'defendant', 'plaintiff')
```

(you can also do this the other way around: `people_list = list(people_tuple)`)

## Sets

Sets are a bit different from lists and tuples. Again, without going into the details of a `set`, you should just know that sets are somewhat like lists, but with unique values.

You can create sets from other iterables using `set()` or declare them with `{}`, but with no `key:value` syntax:

```shell
>>> people_set = {'lawyer', 'defendant', 'judge', 'plaintiff'}
```

or:

```shell
>>> people_set = set(people)
```

you can use `.add()` to add items to a set. Only new items will be added:

```shell
>>> people_set.add("prosecutor")
>>> people_set
{'lawyer', 'defendant', 'judge', 'plaintiff', 'prosecutor'}
>>> people_set.add("lawyer")
>>> people_set
{'lawyer', 'defendant', 'judge', 'plaintiff', 'prosecutor'}
```

Sets are faster than lists when using the `in` operator. But sets are `unordered` and are not subscriptable:

```shell
>>> people_set[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object is not subscriptable
```

But you can loop through sets with a `for loop`


## Unpacking

Above we saw how to iterate through the `key:value` pair of a dict using the `.items()` method. As mentioned, we used `unpacking`.

Unpacking is a neat little trick to assign at once many values to as many variables.

Let's say we have a tuple like this: `data = ("Max", "prosecutor", "5/2022")` and that we want to extract
from this three different variables, `name`, `role`, `trial`.

Given what we learned, we could do like this:

```shell
>>> data = ("Max", "prosecutor", "5/2022")
>>> name = data[0]
>>> role = data[1]
>>> trial = data[2]
>>> name
'Max'
>>> role
'prosecutor'
>>> trial
'5/2022'
```

But there's a more efficient method: `unpacking`

```shell
>>> data = ("Max", "prosecutor", "5/2022")
>>> name, role, trial = data
>>> name, role, trial = data
>>> name
'Max'
>>> role
'prosecutor'
>>> trial
'5/2022'
```

# Objects' behaviour

Something you must pay attention to is these objects (but python's objects in general) behaviours.

Unlike `int`, `str` and `float` variables, `list`, `tuple`, `set` and `dict` variables are not simply copied from one variable to another. Rather, they are referenced. This might look counter intuitive, but it is very important that you are aware of this to avoid losing your mind on buggy code.

Check this out:

```shell
>>> people_2 = people
>>> people_2
['judge', 'lawyer', 'defendant', 'plaintiff']
>>> people_2.append("prosecutor")
>>> people_2
['judge', 'lawyer', 'defendant', 'plaintiff', 'prosecutor']
>>> people
['judge', 'lawyer', 'defendant', 'plaintiff', 'prosecutor']
```

As you might have notice, if we change `people_2`, the variable `people` is changed as well! This is because in reality, `people_2` and `people` are not two different variables, they are referencing the same object in the interpreter's memory. The same goes for dicts, tuples and sets!

There are different ways to actually copy these objects. But you can just use `.copy()` for now:

```shell
>>> people_2 = people.copy()
```