# Lunch 1

## String basics

In `lunch_0` we've seen the variable basics. `int`, `float` and `str`. In this lunch, we will focus a bit on `str`: strings!

We will learn how to `format`, `manipulate` and `query` string variables.


## Assigning a variable a string value

As we've seen in the first lunch, the easiest way to create a string is using double quotes, like so:

```python
name = "Max"
```

You can also use single quotes, like so:

```python
name = 'Max'
```

My advice is to be consistent in your code. Python is agnostic, but it is a good practice to decide whether you want
to use single (`'`) or double (`"`) quotes and stick with it for the rest of your code.

However, you should also note that it is not possible to simply use the `"` or `'` character in the string
if you're using it to assign the value.

E.g.: if you want to assign to the variable `intro` the value `I'm Max`, you cannot use a single quote like this,
as you will get an error:

```shell
>>> intro = 'I'm Max'
  File "<stdin>", line 1
    intro = 'I'm Max'
               ^
SyntaxError: invalid syntax
```

You have two options:

1. Escape the character using a backslash `\`, like this:
```shell
>>> intro = 'I\'m Max'
```
2. Use double quotes:
```shell
>>> intro = "I'm Max"
```

The same goes if you want to use the `"` character in your string:

```shell
>>> intro = "The name is "Max""
  File "<stdin>", line 1
    intro = "The name is "Max""
                          ^^^
SyntaxError: invalid syntax
```

1. Either use the single quote to assign the variable:
```shell
>>> intro = 'The name is "Max"'
```
2. Or escape the `"` with a `\`:
```shell
>>> intro = "The name is \"Max\""
```


## String formatting

Sometimes you may want to create strings dynamically, using variables from your script.

In `lunch_0` we saw that with the `print()` method we can do so in this fashion:

```shell
>>> name = "Max"
>>> age = 29
>>> print("My name is", name, "and I'm", age, "years old")
My name is Max and I'm 29 years old
```

However, you might want to assign what we just printed as a vaule to a variable. There are many ways to do this.

### The F-String

With the `f-string` we can combine variables with strings using the `{}`, like so:

```shell
>>> intro = f"My name is {name} and I'm {age} years old"
>>> intro
"My name is Max and I'm 29 years old"
```

As you may have noticed, simply put an `f` before the quotes and wrap your variables in `{}`.

### .format()

Another way to achieve the same result, but more dynamically, is using the `.format()` method. The method can be used in many different ways:

#### Empty braces

To use this method, just put empty `{}` in the string, then, the end of the string, use `.format(your, variables, here)`.

Beware: there must be the same number of `{}` and variables. The `{}` will be replaced with the variable's value in the order they appear within `.format()`

```shell
>>> intro = "My name is {} and I'm {} years old".format(name, age)
>>> intro
"My name is Max and I'm 29 years old"
```

#### Numbered braces

The second method, allows you to put numbers in the `{}` placeholder so you can re-use the variables according to the order they appear in `.format()` (the first one is 0!), like so:

```shell
>>> intro = "My name is {0} and I'm {1} years old. {1} is the age and {0} is the name".format(name, age)
>>> intro
"My name is Max and I'm 29 years old. 29 is the age and Max is the name"
```

#### Named braces

The third method uses `keyword arguments` for `.format()` and allows you to use keywords within `{}`, like so:

```shell
>>> intro = "My name is {name} and I'm {age} years old. {age} is the age and {name} is the name".format(name="Max", age=29)
>>> intro
"My name is Max and I'm 29 years old. 29 is the age and Max is the name"
```

#### Format specifiers

The `{}` allows for some neat tricks while formatting strings, whether you use `f-strings` or `.format()`

Say you have a float variable `pi = 3.14159` and that you want to display only the first two digits. You can do so like this:

```shell
>>> pi = 3.14159
>>> info = f"Pi with a two-decimals precision is {pi:.2f}"
>>> info
'Pi with a two-decimals precision is 3.14'
>>> 
```

You can read more about format specifiers [here](https://www.python.org/dev/peps/pep-0498/#format-specifiers)

### String additions and multiplication

String can be concatenated using the `+` operator. Beware: no spaces ` ` are added when doing so!

```shell
>>> intro = "Hi, my name is " + name
>>> intro
'Hi, my name is Max'
```

But be mindful, you can only add string to other strings!

```shell
>>> intro = f"Hi, my name is {name} and I'm " + age
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

You can also do multiplications with strings:

```shell
>>> name * 10
'MaxMaxMaxMaxMaxMaxMaxMaxMaxMax'
```

### Special characters

Sometimes you might need or want to use special characters.

The most notable one is the `newline` character, or `\n`. It works like so:

```shell
>>> intro = f"Hi, my name is {name}.\nI'm {age}"
>>> intro
"Hi, my name is Max.\nI'm 29"
>>> print(intro)
Hi, my name is Max.
I'm 29
```

For a more comprehensive list of special characters, [go here](https://www.w3schools.com/python/gloss_python_escape_characters.asp)


## String manipulation and querying

Python has a huge set of built-in methods to manipulate and query strings. Let's go over the most important ones, or at least the ones you are more likely to use.

**Always keep in mind that when you use these methods, new values are returned. Strings are not changed in-place**

### len()

The `len()` method can be used also with strings to know how many characters they have. Like so:

```shell
>>> name = "Max"
>>> len(name)
3
```


### .lower()

Returns the string in lowercase:

```shell
>>> name = "Max"
>>> name.lower()
'max'
```

### .islower()

Returns `True` if the string is lowercase, else returns `False`

```shell
>>> name = "Max"
>>> name.islower()
False
>>> name = "max"
>>> name.islower()
True
```

### .upper()

Returns the string in UPPERCASE:

```shell
>>> name = "Max"
>>> name.upper()
'MAX'
```

### .isupper()

Returns `True` if the string is uppercase, else returns `False`

```shell
>>> name = "Max"
>>> name.isupper()
False
>>> name = "MAX"
>>> name.isupper()
True
```

### .title()

Returns the string in title case:

```shell
>>> intro = "my name is max"
>>> intro.title()
'My Name Is Max'
```

### .istitle()

Returns `True` if the string is titlecase, else returns `False`

```shell
>>> intro = "my name is max"
>>> intr.istitle()
False
>>> intro = "My Name Is Max"
>>> intro.istitle()
True
```

### .strip()

Returns a string, stripped of spaces, tabs and newline characters (`\n`, `\t`, `\n`), at the beginning and at the end of the string. Alternatively you can pass the character that you want to be stripped as an argument.

```shell
>>> "\n My name is Max   \n\n".strip("\n")
' My name is Max   '
>>> "   My name is Max   \n\n".strip()
'My name is Max'
>>> "   My name is Max   \n\n".strip("\n")
'   My name is Max   '
>>> "   My name is Max   \n\n".strip(" ")
'My name is Max   \n\n'
```

If you only want to strip characters from the right side, use `.rstrip()`; for the left side, use `.lstrip()`

```shell
>>> "   My name is Max   ".lstrip()
'My name is Max   '
```

### .isdigit()

Returns `True` if the string is only made of digits, else returns `False`

```shell
>>> name = "Max"
>>> age = "28"
>>> name.isdigit()
False
>>> age.isdigit()
True
```

### .swapcase()

Returns a new string with swapped case:

```shell
>>> intro = "My Name Is Max"
>>> intro.swapcase()
'mY nAME iS mAX'
```

### .startswith()

Returns `True` if the string starts with the specified value

```shell
>>> intro = "My name is Max"
>>> intro.startswith("My")
True
>>> 
```

### .endswith()

Returns `True` if the string ends with the specified value

```shell
>>> intro = "My name is Max"
>>> intro.endswith("Max")
True
>>> 
```

### .find() and .index()

`.find()` and `.index()` work in a similar way: they return the position of the value you're looking for.

However, if the value is not present in the string, `.find()` will return `-1`, `.index()` will raise an exception:

```shell
>>> intro = "My name is Max"
>>> intro.find("is")
8
>>> intro.index("is")
8
>>> intro.find("Joe")
-1
>>> intro.index("Joe")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found
```

**Note**: It will return the position of the first occurence of what you are looking for, starting from left to right. If you want to start from right to left, use `.rfind()` and `.rindex()`

### .count()

Returns the number of times a certain value is occurs in a string

```shell
>>> intro = "My name is Max, my age is 28"
>>> intro.count("is")
2
```

### .replace()

Returns a new string replacing the specified value with the other specified value.

```shell
>>> fruits = "Apple, orange, kiwi"
>>> fruits.replace("orange", "mango")
'Apple, mango, kiwi'
```

You can also limit the number of times this happens:

```shell
>>> fruits = "Apple, orange, kiwi, orange, banana, orange"
>>> fruits.replace("orange", "mango", 2)
'Apple, mango, kiwi, mango, banana, orange'
```

### The `in` operator

If you want to query a string to know wheter a substring is present or not, you can use the `in` operator, like so:

```shell
>>> fruits = "Apple, orange, kiwi"
>>> "orange" in fruits
True
>>> "banana" in fruits
False
```

### slicing

Slicing returns a substring of your string, given two positions, start and end. The sintax is `[start:end]`

**Note**: The first character is at position `0` the last character is at position `-1`


```shell
>>> intro = "My name is Max, my age is 28"
>>> intro[0:2]
'My'
```

If you omit the second position, it will go until the end of the string:

```shell
>>> intro[16:]
'my age is 28'
```

**Note**: When using slicing, the second position provided **is not included in the selection**

```shell
>>> intro[0:-1]
'My name is Max, my age is 2'
```

### .split()

The `.split()` method returns a `list` (we will address lists later on) splitting a list using the value provided. If no value is provided, it will use a space by default. Like so:

```shell
>>> intro = "My name is Max, my age is 28"
>>> intro.split()
['My', 'name', 'is', 'Max,', 'my', 'age', 'is', '28']
>>> intro.split(",")
['My name is Max', ' my age is 28']
```

### .join()

The `.join()` method joins a list of strings with the value its called from, like so:

```shell
>>> " ".join(['My', 'name', 'is', 'Max,', 'my', 'age', 'is', '28'])
'My name is Max, my age is 28'
>>> "-".join(['My', 'name', 'is', 'Max,', 'my', 'age', 'is', '28'])
'My-name-is-Max,-my-age-is-28'
```

### More on strings

You can find more info [here](https://www.w3schools.com/python/python_ref_string.asp)
