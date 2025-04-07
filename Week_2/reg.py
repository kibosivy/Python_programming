# re.findall(pattern, string): Returns a list of all matches in the string
# re.search(pattern, string): Returns a match object if the pattern is found, otherwise None
# re.split(pattern, string): Splits the string at each match of the pattern
# re.sub(pattern, replacement, string): Replaces all matches of the pattern with the replacement string
# re.compile(pattern): Compiles the regex pattern for later use

import re

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
pattern = "a.b"

import re
matches = re.findall(pattern, text)
print(matches)

# text = "Hello World"
# pattern = r"World$"

# matches = re.findall(pattern, text)
# print(matches)

# match = re.search(pattern,text)
# print(match.group())


# # character classes
# # [abc]
# # [a-z] - any lowercase character
# # [A-Z] - any uppercase
# # [0-9] - any digit
# # [a-zA-Z0-9] -alphanumeric
# # \d - any digit
# #  \w - any word
# # \s - whitespace

# text = "My pone number is 123-456-7890"
# pattern = r"\d+"

# matches = re.findall(pattern,text)
# print(matches)

# REGEX EXERSICE
# string contains only a certain set of characters (in this case a-z, A-Z and 0-9)
import re

def is_valid_string(s):
    pattern = r'^[a-zA-Z0-9]+$'  # Only letters and numbers allowed
    return bool(re.match(pattern, s))  # Returns True if it matches, False otherwise

print(is_valid_string("Hello123"))   # True
print(is_valid_string("Hello@123"))  # False (contains @)
print(is_valid_string("Hello 123"))  # False (contains space)

# Python program that matches a string that has an ‘a’ followed by anything, ending in ‘b’
import re

def match_pattern(s):
    pattern = r"^a.*b$"  # Starts with 'a', followed by anything (.*), and ends with 'b'
    return bool(re.match(pattern, s))

# Test cases
print(match_pattern("acb"))      # True
print(match_pattern("a123b"))    # True
print(match_pattern("ab"))       # True
print(match_pattern("bca"))      # False (doesn't start with 'a')
print(match_pattern("abc"))      # False (doesn't end with 'b')

# Extract all email addresses from the following text:
import re
text = "Contact us at support@email.com, info@website.org, or sales@shop.net."

# Regular expression pattern for email addresses
pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

# Find all email addresses
emails = re.findall(pattern, text)
print("Emails found:", emails)

# Check if a string is a valid phone number in the format 123-456-7890
import re

# Sample text containing a phone number
text = "My number is 987-654-3210."

# Define the regex pattern
pattern = r"\d{3}-\d{3}-\d{4}"

# Search for a phone number in the text
match = re.search(pattern, text)

# Check if a match is found
if match:
    print("Valid phone number found:", match.group())
else:
    print("No valid phone number found.")

# Extract Dates in Different Formats
import re

text = "The events are on 12/08/2023 and 07-15-2024."

# Define the regex pattern for both formats
pattern = r"\d{2}/\d{2}/\d{4}|\d{2}-\d{2}-\d{4}"

# Find all matching dates in the text
dates = re.findall(pattern, text)

# Print the extracted dates
print("Dates found:", dates)

# Check if a Password is Strong
password = "StrongP@ss1"

# pattern
def is_strong_password(password):
  pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$"

  return bool(re.match(pattern, password))

# Test password
password = "StrongP@ss1"

# Check and print result
if is_strong_password(password):
    print("Valid strong password")
else:
    print("Invalid password")

# Find All URLs
import re

text = "Visit https://www.google.com or http://example.org for more info."

pattern = r"https?://\S+"

urls = re.findall(pattern, text)
print("URLs found: ", urls)

# Python program that extracts all hashtags (words starting with #) from a given tweet
import re

# text
tweet = "Learning #Python is fun! #Coding #100DaysOfCode"

# pattern
pattern = r"#\w+"

hashtag = re.findall(pattern, tweet)
print("Hashtags found", hashtag)

# Extract Mentions from a Tweet
import re

tweet = "Hey @John, have you seen @Alice's latest post? @dev_team is doing great!"

pattern = r"@\w+"

mentions = re.findall(pattern, tweet)
print("Mentions found: ", mentions)