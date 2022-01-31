"""
TRACK 2
Ask a user to write a short bio of themselves.
Sanitize the bio so that there are no spaces or special characters at the beginning or at the end.
Print out the length of the bio in number of characters and the number of times that each punctuation character `.,;` appears using `.format()` with keyword arguments, so that the output looks like this:

"
total length: 26
fullstop: 3
comma: 2
semicolon: 0
"
"""

bio = input("Describe yourself:\n").strip()
total_length = len(bio)
fullstops = bio.count(".")
commas = bio.count(",")
semicolons = bio.count(";")

info = "total length: {total_length}\nfullstops: {fullstops}\ncommas: {commas}\nsemicolons: {semicolons}"

print(info.format(total_length=total_length, fullstops=fullstops, commas=commas, semicolons=semicolons))