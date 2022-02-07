# Lunch 3

## Regular Expressions (regex)

Regular Expressions (regex) are, in their essence, a string of text describing a search pattern.

Say you have a long text and that you want to quickly extract all the email addresses.
Doing so with the usual tools we saw before is possible, but it would be quite painful.

So regex come to our help, with a whole different kind of pain.

Back to our example: you want to find ALL the email in a long text.

Simplifiyng a bit, an email is made of three components: a bunch of characters + `@` + domain. With regex we can describe the email pattern as follows:

`[a-z]+@[a-z]+\.[a-z]+` (oversimplified)

What this regex is telling to our `engine` is to look for a sequence of 1 or more (`+`) characters `a` to `z`, followed by a `@` followed by 1 or more (`+`) characters `a` to `z`, followed by a `.`, followed by 1 or more (`+`) characters `a` to `z`.

It would be pointless for me to re-write the documentation of regular expressions here.

When dealing with regex, your best allies are [regular-expressions.info](https://www.regular-expressions.info/)
and [regex101.com](https://regex101.com/).

This [quickstart guide](https://www.regular-expressions.info/quickstart.html) is excellent to start with. Fiddle around with that on [regex101.com](https://regex101.com/).

## The re library

Python comes with a built-in library called `re` that allows us to work with regular expressions.

We will not go into the details of the library; we will just use some basic stuff. [You can find extensive
documentation here](https://docs.python.org/3/library/re.html)

## The basics

To use the library in our code or in the interactive shell, we simply use the `import` statement. Like so:

```shell
>>> import re
```

As a good practice, we define regex patterns with `raw strings`, that are strings preceded by an `r`, like so:

```shell
>>> email_pattern = r"[a-z]+@[a-z]+\.[a-z]+"
```

### re.search()

To search for the pattern in our text, we use the `.search()` method.

The `.search()` method will return a `match` object, that can be `None` if nothing is found.

```shell
>>> email_pattern = r"[a-z]+@[a-z]+\.[a-z]+"
>>> text = "my email is biagio@example.com"
>>> m = re.search(email_pattern, text)
>>> m
<re.Match object; span=(12, 30), match='biagio@example.com'>
```

As you can see, the match object (saved in the variable `m`) contains some info. Let's dig a bit.

```shell
>>> m.group()
'biagio@example.com'
>>> m.span()
(12, 30)
>>> m.start()
12
>>> m.end()
30
```

Cool. Let's make use of the `.group()` method of match objects. Let's make our regex a bit better by grouping stuff.

```shell
>>> email_pattern = r"([a-z]+)@([a-z]+\.[a-z]+)"
```

Now we have a username group and a domain group. And, of course, the whole pattern group that counts as `group 0`

```shell
>>> m = re.search(email_pattern, text)
>>> m.group()
'biagio@example.com'
>>> m.group(0)
'biagio@example.com'
>>> m.group(1)
'biagio'
>>> m.group(2)
'example.com'
>>> m.span(1)
(12, 18)
>>> m.span(2)
(19, 30)
>>> m.groups()
('biagio', 'example.com')
```

Sexy. Now let's try with named groups.

```shell
>>> email_pattern = r"(?P<username>[a-z]+)@(?P<domain>[a-z]+\.[a-z]+)"
```

We still can use all previous methods, but now, we can query also with the name of the groups:

```shell
>>> m.group("username")
'biagio'
>>> m.group("domain")
'example.com'
>>> m.span("username")
(12, 18)
>>> m.span("domain")
(19, 30)
```

Cool, innit?

Plus, now that we have named groups, we can use the `.groupdict()` method:

```shell
>>> m.groupdict()
{'username': 'biagio', 'domain': 'example.com'}
```

#### To keep in mind

- `re.search()` will return only the first occurance of the pattern in the text. If you need all of them, see `re.findall()` or `re.finditer()`
- **FLAGS**: flags change the behaviour of the search function. There are many. [Check 'em out here](https://docs.python.org/3/library/re.html#module-contents). The one you will use the most is the `re.IGNORECASE` flag (or its shorthand: `re.I`), that will make the regex case-insensitive.

### re.match()

The `re.match()` method behaves similarly to the `re.search()` method. The difference is that it will return an object **if and only if** the search pattern matches **exactly** the text, in its **entirety**.

To make this more clear, having:

```shell
>>> email_pattern = r"(?P<username>[a-z]+)@(?P<domain>[a-z]+\.[a-z]+)"
>>> text = "my email is biagio@example.com"
```

`re.match()` will return `None`

```shell
>>> re.match(email_pattern, text)
>>> m = re.match(email_pattern, text)
>>> m is None
True
```

In other words, using `match` is equivalent to wrapping our regex with the start of string character at the beginning (`^`), and end of string character at the end (`$`).

### re.findall()

[Stolen from here](https://docs.python.org/3/library/re.html#re.findall)

The `re.findall()` method will return all non-overlapping matches of pattern in string, as a list of strings or tuples. The string is scanned left-to-right, and matches are returned in the order found. Empty matches are included in the result.

The result depends on the number of capturing groups in the pattern. If there are no groups, return a list of strings matching the whole pattern. If there is exactly one group, return a list of strings matching that group. If multiple groups are present, return a list of tuples of strings matching the groups. Non-capturing groups do not affect the form of the result.

```shell
>>> email_pattern = r"[a-z]+@[a-z]+\.[a-z]+"
>>> text = "my email is biagio@example.com, your email is max@example.com, their email is andrea@example.com"
>>> re.findall(email_pattern, text)
['biagio@example.com', 'max@example.com', 'andrea@example.com']
```

If we use groups:

```shell
>>> email_pattern = r"(?P<username>[a-z]+)@(?P<domain>[a-z]+\.[a-z]+)"
>>> re.findall(email_pattern, text)
[('biagio', 'example.com'), ('max', 'example.com'), ('andrea', 'example.com')]
```

### re.finditer()

`re.finditer()` will return an [iterator](https://docs.python.org/3/glossary.html#term-iterator)
yielding match objects over all non-overlapping matches for the RE pattern in string. The string is scanned left-to-right, and matches are returned in the order found. Empty matches are included in the result.

```shell
>>> for m in re.finditer(email_pattern, text):
...     print(m)
... 
<re.Match object; span=(12, 30), match='biagio@example.com'>
<re.Match object; span=(46, 61), match='max@example.com'>
<re.Match object; span=(78, 96), match='andrea@example.com'>
```