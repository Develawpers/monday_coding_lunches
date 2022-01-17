# Lunch 0

## What is Python?

Python is a clear and powerful object-oriented programming language. You can find an [overview here.](https://wiki.python.org/moin/BeginnersGuide/Overview)

You can find more information on their [official website](https://www.python.org/) and on their [Beginner's Guide](https://wiki.python.org/moin/BeginnersGuide).

To install Python, simply visit the [download section](https://www.python.org/downloads/) of the Python.org website and follow the easy instructions. Just make sure you download the latest version for your Operating System (MacOS, Windows, any Linux distro).

For our purposes, Python behaves exactly the same in all operating systems. The only small difference that we might encounter is with the creation and sourcing of `virtual environments`, that we will deal with later on.


## How can we use Python?

To keep it simple, there are two main ways for you to use or interact with Python.


### The interactive way: Terminal and IDLE

You can access the interactive way either via the Terminal (in MacOS and Linux) or Command Prompt (in Windows); or the IDLE, that comes installed with Python. The IDLE is Python’s Integrated Development and Learning Environment.
    
- To access the Command Prompt or Terminal, open it from your computers apps. Then just type `python3.10` (or whatever version you have installed)
- To access the IDLE, just open it from your apps after having installed Python


### The script way

The script way consists of writing files with a `.py` extensions that then get executed by the Python Interpreter.

 - You can write `.py` files in many ways; Note Pad or TextEdit are usually sufficient. However, commonly, developers use Integrated Development Environments (IDEs) such as [Visual Studio Code](https://code.visualstudio.com/) or [PyCharm](https://www.jetbrains.com/pycharm/), as they often come with type hinting and linting (a kind of auto-correct for programmers) and a built-in terminal to fiddle with and test your code as you write it.

## The basics

Today, let's tackle some basics of Python. We will deal with:

- `print()`
- variables and types
- `input()`
- `if-else`

But first of all, let's fire up Python interactively to start playing with it.

On your machine, search for either the Terminal (MacOS/Linux) or the Command Prompt (Windows); or, if you prefer, open the IDLE app that came installed when installing Python. (From now on, when I use `Terminal` I mean both `Terminal` and `Command Prompt`).

In this example, you'll see what happens on a MacOS computer; but it's relatively similar to Windows. Fire up a terminal and type `python3`. You'll see something like this:

```
biagio@Biagios-MacBook-Pro % python3
Python 3.10.1 (v3.10.1:2cd268a3a9, Dec  6 2021, 14:28:59) [Clang 13.0.0 (clang-1300.0.29.3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

The `>>>` is not something we type; it's the Terminal telling us that it's ready to receive our code. This is also called an `interactive shell`.

In the interactive shell, whatever command we type, gets executed immediately and we will have the returned value on screen.

Let's start fiddling.

## print()

The easiest way to have our code communicate with users, is the `print` statement.

In programming, when we say `print`, we don't mean with a printer; what we mean is to display some text on the screen of our users. Where? In the Terminal. It works like this:

```shell
>>> print("Hello, World!")
Hello, World!
```

Brilliant. Now we know the basic way to display information to our users. We'll make use of this later on.

## Variables

Variables are containers for storing data values. Variables have names and can be of different `types`.

The name of the variable is arbitrary. It is good practice to give variables a meaningful name.

Let's see some examples of the basic variable types: `int`, `str`, `float`.

To assign a variable, we simply use the `=` operator after the name of the variable, like this:

```shell
>>> name = 'Max'
>>> age = 28
>>> height = 180.5
```

The variables above are respectively of the types `str` (string) for `name` (notice the double quotes), `int` for age (an integer number) and `float` for `height` (floating point number).

Now, in our interactive shell, if we type the name of the variable we just assigned, we will be returned it's value. Like so:

```shell
>>> name
'Max'
>>> age
28
>>> height
180.5
```

We can also use the `type()` method to ask for the type of a variable, like so:

```shell
>>> type(name)
<class 'str'>
>>> type(age)
<class 'int'>
>>> type(height)
<class 'float'>
```

Excellent! Now we can do something with this and `print()`. Let's see how:

```shell
>>> print("Hi! My name is", name)
>>> print("I'm", age, "years old")
>>> print("And I'm", height, "cm tall")
```

As you can see, we can combine variables with other text in our `print()` statement to create dynamic output.

One more thing that you should be aware of regarding types, is that variables can be `cast` (converted) to or from other types. And things that look similar, sometimes are very different. Take this for example:

```shell
>>> a = 10
>>> b = '10'
```

`a` and `b` might look the same, but while `a` is of type `int`, `b` is of type `str`, so they behave in very different ways, as we will see shortly up next.

```shell
>>> a
10
>>> b
'10'
>>> type(a)
<class 'int'>
>>> type(b)
<class 'str'>
>>> a + 5
15
>>> b + 5
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

Let's try to cast our variables to a different type:

```shell
>>> str(a)
'10'
>>> int(b)
10
```

Keep in mind, that this operation did not `convert` the variables, as we have not re-assigned the value. The output is just that, an output. `a` is still of type `int` and `b` is still of type `str`. See:

```shell
>>> a
10
>>> b
'10'
>>> type(a)
<class 'int'>
>>> type(b)
<class 'str'>
```

If we want to convert them, we need to **reassign** them, like so:

```shell
>>> a = str(a)
>>> b = int(b)
>>> a
'10'
>>> b
10
>>> type(a)
<class 'str'>
>>> type(b)
<class 'int'>
```

So if we not try to add `5` to `a`, we will get the same error we got above with `b`:

```shell
>>> a + 5
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

Beware: not everything can be cast to everything. If we try to cast our variable `name`, that is not made of `digits`, to `int`, we will get an error:

```shell
>>> int(name)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'Max'
```

## input()

So far, so good. But as of now we could only hard code variables ourselves -- we didn't get them from our user.

Let's see how to do that with `input()`

```shell
>>> name = input("What is your name? ")
What is your name? 
```

With `input`, our user will be prompted with the (exact) text in the parenthesis (notice the space after the '?') and return the value as a `str`. With the syntax above, we assign the variable `name` to the returned value of `input()`.

We can now do the same with `age` and `height`, but as we just said, the default type will be `str`, and we want those in, respectively, `int` and `float`.

To fix this, we can use a little trick. We can wrap our `input()` statement into the type casting statement, like so:

```shell
>>> age = int(input("What is your age? "))
What is your age? 28
>>> height = float(input("What is your height? "))
What is your height? 180.5
```

(The user's input will be typed right next to the prompt, in this case).

Great. Now we know the basics of variables and their types, displying info in our terminal and prompting the user for input. Let's do something more dynamic with it.

## if-else

To understand the `if-else` statements, we first need to briefly talk about comparison operators.

Above we saw the assignment operator `=` that we used to assign a value to a variable. There are many more, but let's not think about those for now.

The comparison operators in Python are the following:

|Operator   |Name           |Example|
|-----------|---------------|-------|
| ==        |Equal          | x == y|
| !=        | Not equal     | x != y|
| >         |Greater than   | x > y |
| <         |Less than      | x < y |
| >=        | Greater than or equal| x >= y|
| <=        | Less than or equal to| x <= y|

These operators will return either `True` or `False` (values of `bool` [boolean] type!) that will help us with our conditional `if-else` statements.

Let's see how they work

```shell
>>> x = 10
>>> y = 20
>>> x == y
False
>>> x != y
True
>>> x > y
False
>>> x < y
True
>>> y >= x
True
>>> y <= x
False
```

Before we move to if-else, you need to know that in Python, logic
blocks are determined by indentation. This helps us have a clean and neat code.

You can indent your code either with `four spaces` unit or with `tab`. There's a never ending fight in the coding community about what's best. Just don't use an odd number of spaces and **be consistent**.
Some editors might automatically convert tabs to spaces.

Now, let's see an `if-else` logic block:

```shell
>>> if x == y:
...     print('x and y are equal!')
... else:
...     print('x and y are not equal!')
... 
x and y are not equal!
```

Perfect. Now let's try with another operator:

```shell
>>> if x > y:
...     print('x is greater than y!')
... else:
...     print('x is not greater than y!')
... 
x is not greater than y!
```

Nice, uh?

## bringing everything together

Now let's try to bring everything together, and write a simple set of instructions that will ask our user their name and age, and determine whether or not they can have a beer. You know, `legal stuff`.

```shell
>>> name = input("What is yout name? ")
What is yout name? Max
>>> age = int(input("How old are you? "))
How old are you? 25
>>> if age >= 18:
...     print("Very well,", name, ", you can have a beer!")
... else:
...     print("I'm sorry,", name, ", you are not of legal age, yet!")
... 
Very well, Max , here's your beer!
```

Now, this was all done in an interactive shell. Let's put it in a `*.py` file so that we can re-use it as many times as we want.

Open your preferred editor (VS Code, Pycharm, TextEdit, NotePad) and create a new file (I'll name it `lunch_0.py`) and put the content above in it and save it. It should look something like this:

```python
name = input("What is yout name? ")
age = int(input("How old are you? "))

if age >= 18:
    print("Very well,", name, ", you can have a beer!")
else:
    print("I'm sorry,", name, ", you are not of legal age, yet!")
```

Now, from your teminal, be sure to be in the same location of the file ([how do I do this on Windows?](https://www.howtogeek.com/659411/how-to-change-directories-in-command-prompt-on-windows-10/#:~:text=Change%20Directories%20Using%20the%20Drag,window%2C%20and%20then%20press%20Enter.) [How do I do this on MacOS/Linux](https://www.cyberciti.biz/faq/how-to-change-directory-in-linux-terminal/)), then run:

`python3 lunch_0.py`

Have fun!