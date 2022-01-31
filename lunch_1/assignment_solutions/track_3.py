"""
TRACK 3

Ask a user to write a short bio about themselves.
Sanitize the input making sure that there are no extra spaces at the beginning and at the end of the string.
Sanitize further the string, making sure that all the words are single spaced from one another using `.split()` and `.join()`.
Use `.count()` to determine the number of *words* and print it out.
"""

# There are many valid ways to solve this one!

bio = input("Describe yourself:\n").strip()

single_spaced_bio = " ".join(bio.split())

number_of_spaces = single_spaced_bio.count(" ")
number_of_words = number_of_spaces + 1

print(f"There are {number_of_words} words in your bio")