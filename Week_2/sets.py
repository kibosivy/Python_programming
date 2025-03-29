# sets = unique

a = {1,2,3,4}
c = [1,2,3,4]
b = set(c)

print(a)
print(type(a))

# # set method

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