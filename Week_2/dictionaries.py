# dictionary- the indices can be (almost) any type
# curly brackets, {}, represent an empty dictionary. To add items to the dictionary, you can use square brackets
# The function dict creates a new dictionary with no items.
# eng2sp = dict()
# print(eng2sp)

# # to add to dictionary
# eng2sp['one'] = 'uno'
# print(eng2sp)

# eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
# print(eng2sp)

# print(eng2sp['two'])

# print(eng2sp['four'])

# len function- returns the number of key-value pairs
# print(len(eng2sp))

# in operator - tells you whether something appears as a key in the dictionary
# print('one' in eng2sp)

# method values - see whether something appears as a value in a dictionary
# vals = list(eng2sp.values())
# print('uno' in vals)

# set of counters
# implementation is a way of performing a computation
# word = 'brontosaurus'
# d = dict()
# for c in word:
#     if c not in d:
#         d[c] = 1
#     else:
#         d[c] = d[c] + 1
# print(d)

# get - takes a key and a default value
# counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
# print(counts.get('jan', 0))

# print(counts.get('tim', 0))

# word = 'brontosaurus'
# d = dict()
# for c in word:
#     d[c] = d.get(c,0) + 1
# print(d)


# Looping and dictionaries
# counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
# for key in counts:
#     print(key, counts[key])

# find all the entries in a dictionary with a value above ten
# counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
# for key in counts:
#     if counts[key] > 10 :
#         print(key, counts[key])

# print the keys in alphabetical order
counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
lst = list(counts.keys())
# print(lst)
lst.sort()
for key in lst:
    print(key, counts[key])