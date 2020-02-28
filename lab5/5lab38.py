import re

# Search for an upper case "S" character in the beginning of a word, and print its position:

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
# Search for an upper case "S" character in the beginning of a word, and print its position:
print(x.span())
# The string property returns the search string:
print(x.string)
# Search for an upper case "S" character in the beginning of a word, and print the word:
print(x.group())
