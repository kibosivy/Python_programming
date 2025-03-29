# import re

text = "We are learning regular expressions in Python"

pattern = "Python"

match = re.search(pattern,text)

print(match.group())

if match:
    print(f"match found : {match.group()}")
else:
    print("match not found")

# characters
# . - match/take a place of a single character
# ^ - match start of a string
# $ - end of a string
# * - match 0 or repetitions

text = "accb a1b aab axb"
pattern = "a*b"

import re
matches = re.findall(pattern, text)
print(matches)

text = "Hello World"
pattern = r"World$"

matches = re.findall(pattern, text)
print(matches)

match = re.search(pattern,text)
print(match.group())


# character classes
# [abc]
# [a-z] - any lowercase character
# [A-Z] - any uppercase
# [0-9] - any digit
# [a-zA-Z0-9] -alphanumeric
# \d - any digit
#  \w - any word
# \s - whitespace

text = "My pone number is 123-456-7890"
pattern = r"\d+"

matches = re.findall(pattern,text)
print(matches)