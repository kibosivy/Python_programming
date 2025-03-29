t = ['a', 'b', 'c',]
print(t)

t = ['a', 'b', 'c',]
t.append('d')
print(t)

t1 = ['a', 'b', 'c',]
t2 = ['d', 'e']
t1.extend(t2)
print(t1)

t = ['d', 'a', 'e', 'b', 'c',]
t.sort()
print(t)

t = ['a', 'b', 'c',]
x = t.pop(1)
print(t)

t = ['a', 'b', 'c',]
del t[1]
print(t)

t = ['a', 'b', 'c',]
t.remove('c')
print(t)

t = ['a', 'b', 'c', 'd', 'e']
del t[1:4]
print(t)


names = ("Ivy", "Berlin")
numbers = (1, 2, 3)
nested = (names, numbers)
print(nested)

tree = ("oranges", "mangoes", 34, 0.5)
print(tree)

flowers = ["roses", "lillies", "tulips"]
b = tuple(flowers)
print(b)

a = ()
print(a)

size = len(flowers)
print(len(flowers))
print(size)

# dictionaries use curly brackets

# -- key, value pairs -- using colon to seperate key value pair

person = {"name":"John"}
print(person)

print(type(person))

John = {"l_name":"Doe","age":31}

print(John["age"])

John["age"] = 41

print(John)

John = {"l_name":"Doe","age":31,"country":"Kenya"}

print(John)

print(John.get("age"))
print(John["age"])

print(John.items())

for i,j in John.items():
    print(f"The details are : {i} : {j}")



# # list of numbers
numbers = [5, 2, 9, 1, 7]

# ascending order
numbers.sort()
print(numbers)

# # descending order
numbers.sort(reverse=True)
print(numbers)

# # largest number
l1 = [43, 89, 67, 56, 12]
print(max(l1))

# # sum all the items
list1 = [10, 20, 30, 40, 50]
print(sum(list1))

# # list of numbers: enumerate() function useful when you need both the index and value while looping through a list
numbers = [10, 20, 30, 40, 50]
for index, value in enumerate(numbers):
    print(f"Index {index}: {value}")

# # tuple with student details
student_details = ("Ivy Kibos", 25, "A")
print(student_details)

# tuple to store mathematical operators
operators = ("+", "-", "*", "/")

# print(operators)
# choose an operator
operator = input("Choose an operator (+, -, *, /): ")

# input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# calculation based on the chosen operator
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
  if num2 != 0:
        result = num1 / num2
  else:
        result = "Error"
else:
    result = "Invalid operator"
print("Result:", result)