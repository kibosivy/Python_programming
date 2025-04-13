fruits = ['banana', 'mango', 'apple']
print(fruits)

print('banana' not in fruits)

x = int(input("Enter a number :"))
if x < 0:
  print("Negative Number")
else:
  print("Positive Number")

x = int(input("Enter a number :"))
if x == 1:
  print("Number 1")
elif x == 2:
  print("Number 2")
elif x == 3:
  print("Number 3")
else:
  print("Invalid Entry")


# Nested Conditionals

score = 45

if score >= 50:
  print("Above Average")
  if score >= 80:
    print("Excellent")
  else:
    print("Above but not excellent")
else:
  print("You failed")

age = 22
income = 90000

if age >= 18 and income >= 100000:
  print("Eligible for loan")
else:
  print("Not eligible for loan")

numbers = [1,2,3,4,5]

for number in numbers:
  new_number = number + 2
  print(new_number)


# loop through a list of floats and return the modulus of each element

# modulus of 2

numbers = [2.2,3.3,4.4,5.5]

for i in numbers:
  j = i % 2
  print(j)

# divide by 2

numbers = [2,3,4,5]

for i in numbers:
  j = i / 2
  print(j)

# nested loops

months = ['jan', 'feb', 'mar', 'apr']
days = [1,2,3,4]

for month in months:
  for day in days:
    print(month,day)

# statements within loops

# continue

numbers = [1,2,3,4,5]

for number in numbers:
  if number == 3:
    continue
  print(number)

for letter in 'Python':
  if letter == 'h':
    continue
  print(letter)

# pass statement
numbers = [1,2,3,4,5]

for number in numbers:
  if number == 3:
    pass
    print('pass this')
  print(number)

