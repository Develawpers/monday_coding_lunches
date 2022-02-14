"""
TRACK 3

Write a code that finds all the dates in ISO-8601 format (YYYY-MM-DD) in a given text. Then, use a `for loop`, `re.finditer()` and `.format()` to print out all the dates like this:
`year: yyyy, month: mm, day: dd`.

Use this text to test your code:

```
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non consequat leo. Pellentesque et enim enim 2022-02-07. Etiam et enim id justo dapibus faucibus eu quis massa. Praesent ac molestie dolor. Etiam urna neque, interdum ut finibus et, tristique ut nisl. Vivamus interdum ipsum vitae elementum facilisis. Proin tellus dolor, ultrices sed magna sed, facilisis convallis lorem 1996-05-12. Fusce accumsan ante vitae metus vestibulum fringilla. Nulla vel tellus nec est euismod volutpat. Praesent sed pretium diam. Morbi eget lacinia ligula. In libero metus, euismod ut pretium a, maximus eu sapien 1985-10-20. Quisque at enim elementum, interdum nisl nec, porta mi. Aliquam facilisis, neque sit amet pulvinar condimentum, velit quam ultrices eros, non convallis justo arcu non quam. Cras est nunc, scelerisque in enim ut, auctor mollis leo. Integer egestas, nisi at finibus vehicula, orci erat maximus urna, a porttitor odio felis vel odio. Nulla eu turpis 2021-12-01 id neque ultricies suscipit vitae nec nulla. Curabitur vel justo est. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Vestibulum dapibus ligula sit amet velit venenatis, nec tempor lorem imperdiet."
"
"""

import re

iso_8601_pattern = r"(?P<year>[0-9]{4})-(?P<month>1[0-2]|0[1-9])-(?P<day>3[01]|0[1-9]|[12][0-9])"

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non consequat leo. Pellentesque et enim enim 2022-02-07. Etiam et enim id justo dapibus faucibus eu quis massa. Praesent ac molestie dolor. Etiam urna neque, interdum ut finibus et, tristique ut nisl. Vivamus interdum ipsum vitae elementum facilisis. Proin tellus dolor, ultrices sed magna sed, facilisis convallis lorem 1996-05-12. Fusce accumsan ante vitae metus vestibulum fringilla. Nulla vel tellus nec est euismod volutpat. Praesent sed pretium diam. Morbi eget lacinia ligula. In libero metus, euismod ut pretium a, maximus eu sapien 1985-10-20. Quisque at enim elementum, interdum nisl nec, porta mi. Aliquam facilisis, neque sit amet pulvinar condimentum, velit quam ultrices eros, non convallis justo arcu non quam. Cras est nunc, scelerisque in enim ut, auctor mollis leo. Integer egestas, nisi at finibus vehicula, orci erat maximus urna, a porttitor odio felis vel odio. Nulla eu turpis 2021-12-01 id neque ultricies suscipit vitae nec nulla. Curabitur vel justo est. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Vestibulum dapibus ligula sit amet velit venenatis, nec tempor lorem imperdiet."

for m in re.finditer(iso_8601_pattern, text):
    print("year: {year}, month: {month}, day: {day}".format(**m.groupdict()))