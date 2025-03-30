# A set is a collection of unique data

a = {1,2,3,4}
c = [1,2,3,4]
b = set(c)

print(a)
print(type(a))

# set method

b = [1,2,3,4,5,5]

c = set(b)
print(c)
print(type(c))

d = list(c)
print(d)
print(type(d))

print(c)

d = c.remove(5)

print(c.remove(1))

# intersections

a = {1,2,3,4}
b = {3,4,5,6}

print(a & b)

# unions

c = a | b
print(c)
d = a.union(b)
print(d)

# difference

e = a - b
print(e)

# create a set of integer type
student_id = {10, 12, 14, 13, 11}
print('Student ID:', student_id)

# create a set of string type
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print('Vowel Letters:', vowel_letters)

# create a set of mixed data types
mixed_set = {'Hello', 101, -2, 'Bye'}
print('Set of mixed data types:', mixed_set)

# Create an empty Set
empty_set = set()

# Add Items to a Set
numbers = {1, 2, 3, 4}

print('Initial Set:',numbers)

# using add() method
numbers.add(5)

print('Updated Set:', numbers)

# Update Items in a Set - indexing has no meaning
companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = ['apple', 'google', 'apple']

# using update() method
companies.update(tech_companies)

print(companies)

# Remove an Element from a Set
languages = {'Swift', 'Java', 'Python'}

print('Initial Set:',languages)

# remove 'Java' from a set
removedValue = languages.discard('Java')

print('Updated Set:', languages)

# Iterate Over a Set
fruits = {"Apple", "Peach", "Mango"}

# for loop to access each fruits
for fruit in fruits: 
    print(fruit)

# Find the Number of Set Elements
even_numbers = {2,4,6,8}
print('Set:',even_numbers)

# find the number of elements
print('Total Elements:', len(even_numbers))

# Union of Two Sets
# first set
A = {1, 3, 5}

# second set
B = {0, 2, 4}

# perform union operation using |
print('Union using |:', A | B)

# perform union operation using union()
print('Union using union():', A.union(B))

# Set Intersection- common elements between set A and B
# first set
A = {1, 3, 5}

# second set
B = {1, 2, 3}

# perform intersection operation using &
print('Intersection using &:', A & B)

# perform intersection operation using intersection()
print('Intersection using intersection():', A.intersection(B))

# Difference between the two sets
# first set
A = {2, 3, 5}

# second set
B = {1, 2, 6}

# perform difference operation using -
print('Difference using -:', A - B)

# perform difference operation using difference()
print('Difference using difference():', A.difference(B))

# Set Symmetric Difference
# first set
A = {2, 3, 5}

# second set
B = {1, 2, 6}

# perform difference operation using &
print('using ^:', A ^ B)

# using symmetric_difference()
print('using symmetric_difference():', A.symmetric_difference(B))

# Check if two sets are equal
# first set
A = {1, 3, 5}

# Define two sets
A = {2, 4, 6, 8}  
B = {3, 5, 1}

# Compare sets using '=='
if A == B:
     print('Set A and Set B are equal')
else:
   print('Set A and Set B are not equal')


# EXERCISE
# 1. Python program to sum up all the items in a dictionary
# Create a dictionary with numbers
numbers = {'a': 10, 'b': 20, 'c': 30}

# Find the sum of all values
total = sum(numbers.values())

print("Total sum:", total)

# 2. dictionary to store product information (name, price, quantity)
# Create an empty dictionary to store products
inventory = {}

# Function to add a product
def add_product(name, price, quantity):
    inventory[name] = {'price': price, 'quantity': quantity}

# Function to update a product
def update_product(name, price=None, quantity=None):
    if name in inventory:
        if price is not None:
            inventory[name]['price'] = price
        if quantity is not None:
            inventory[name]['quantity'] = quantity
    else:
        print("Product not found.")

# Function to remove a product
def remove_product(name):
    if name in inventory:
        del inventory[name]
    else:
        print("Product not found.")

# Adding products
add_product('Laptop', 1000, 5)
add_product('Mouse', 20, 50)

# Updating product quantity
update_product('Mouse', quantity=45)

# Removing a product
remove_product('Laptop')

# Print final inventory
print(inventory)

# 3. dictionary where keys are departments in a company and values are nested dictionaries containing employee information (name, role)
# Create a dictionary with departments
company = {
    'HR': {'Alice': 'Manager', 'Bob': 'Recruiter'},
    'IT': {'Charlie': 'Developer', 'David': 'System Administrator'},
    'Marketing': {'Emma': 'Content Creator'}
}

# Print department details
for department, employees in company.items():
    print("\nDepartment:", department)
    for name, role in employees.items():
        print(f"{name} - {role}")

# 4. function to create a new set that contains the identical items
# Define two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Find common elements
common_items = set1 & set2  # The '&' operator finds common values

print("Common items:", common_items)