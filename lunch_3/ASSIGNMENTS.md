# ASSIGNMENTS

To practice what we've learned on our fourth lunch, try and write one or more Python scripts (a `*.py` file, using whatever editor of your choice) according to the following tracks:

## track 1

Use regex to validate a user-input email that can contain letters, numbers and the special characters `.-+`

## track 2

Given a text containing many emails, use `re.findall()` and unpacking to print out only the domains of all the emails.

Use this text to test your code:

```
"""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non consequat leo. Pellentesque et enim enim auloagerio@gmail.com. Etiam et enim id justo dapibus faucibus eu quis massa. Praesent ac molestie dolor. Etiam urna neque, interdum ut finibus et, tristique ut nisl numerionegidio@hotmail.eu. Vivamus interdum ipsum vitae elementum facilisis. Proin tellus dolor, ultrices sed magna sed, facilisis convallis lorem mevio@justice.eu."""
```

## track 3

Write a code that finds all the dates in ISO-8601 format (YYYY-MM-DD) in a given text. Then, use a `for loop`, `re.finditer()` and `.format()` to print out all the dates like this:
`year: yyyy, month: mm, day: dd`.

Use this text to test your code:

```
text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non consequat leo. Pellentesque et enim enim 2022-02-07. Etiam et enim id justo dapibus faucibus eu quis massa. Praesent ac molestie dolor. Etiam urna neque, interdum ut finibus et, tristique ut nisl. Vivamus interdum ipsum vitae elementum facilisis. Proin tellus dolor, ultrices sed magna sed, facilisis convallis lorem 1996-05-12.

Fusce accumsan ante vitae metus vestibulum fringilla. Nulla vel tellus nec est euismod volutpat. Praesent sed pretium diam. Morbi eget lacinia ligula. In libero metus, euismod ut pretium a, maximus eu sapien 1985-10-20. Quisque at enim elementum, interdum nisl nec, porta mi. Aliquam facilisis, neque sit amet pulvinar condimentum, velit quam ultrices eros, non convallis justo arcu non quam. Cras est nunc, scelerisque in enim ut, auctor mollis leo. Integer egestas, nisi at finibus vehicula, orci erat maximus urna, a porttitor odio felis vel odio. Nulla eu turpis 2021-12-01 id neque ultricies suscipit vitae nec nulla. Curabitur vel justo est. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Vestibulum dapibus ligula sit amet velit venenatis, nec tempor lorem imperdiet.
"""
```