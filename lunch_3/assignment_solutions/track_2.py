"""
TRACK 2
Given a text containing many emails, use `re.findall()` and unpacking to print out only the domains of all the emails.

Use this text to test your code:

```
text = \"""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non consequat leo. Pellentesque et enim enim auloagerio@gmail.com. Etiam et enim id justo dapibus faucibus eu quis massa. Praesent ac molestie dolor. Etiam urna neque, interdum ut finibus et, tristique ut nisl numerionegidio@hotmail.eu. Vivamus interdum ipsum vitae elementum facilisis. Proin tellus dolor, ultrices sed magna sed, facilisis convallis lorem mevio@justice.eu.\"""
```
"""

import re

email_pattern = r"(?P<username>([a-z0-9]+[-+.]?)+[a-z0-9])@(?P<domain>([a-z0-9]+\.?)+\.[a-z]{2,4})"

text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non consequat leo. Pellentesque et enim enim auloagerio@gmail.com. Etiam et enim id justo dapibus faucibus eu quis massa. Praesent ac molestie dolor. Etiam urna neque, interdum ut finibus et, tristique ut nisl numerionegidio@hotmail.eu. Vivamus interdum ipsum vitae elementum facilisis. Proin tellus dolor, ultrices sed magna sed, facilisis convallis lorem mevio@justice.eu."""

# the regex we're using is a bit more advanced, and it has four groups. We want the third one (#2)

for username, username0, domain, domain0 in re.findall(email_pattern, text):
    # [('auloagerio', 'auloageri', 'gmail.com', 'gmail'), ...]
    print(domain)
