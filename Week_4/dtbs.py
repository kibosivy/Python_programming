# a systematic and organized collection of data stored &managed for efficient retrival
# relational - tabular data model
# schema - define structure of data(data types, constraints, relationships)
# query language - sql
# non relational data - allows flexibility (documents,key-value pairs,graphs)
# schema-less
# entity relationship
# entity, attribute, relationship
# SQL
# C-create table and populate
# R-retrieve-select from
# U-update set
# D-delete from

import sqlite3

# connecting to a database(crreate one)

students = sqlite3.connect("students.db")

students

# cursor object

cursor = students.cursor()

# create a table

cursor.execute("""
create table wanafunzi(
  name TEXT,
  gender TEXT,
  age INTEGER
  )""")

# print out

cursor.execute("select * from wanafunzi")

# populate

cursor.execute("""
insert into wanafunzi (name,gender,age)
values ("James","male",60)""")

students.commit()

# select
cursor.execute("select * from wanafunzi")

rows = cursor.fetchall()

for row in rows:
  print(row)

# insert many records

users = [
    ("Kelvin","male",30),
    ("Gladys","female",22)
]

cursor.executemany("""
insert into wanafunzi (name,gender,age)
values(?,?,?)""",users)

cursor.execute("select * from wanafunzi")

rows = cursor.fetchall()

for row in rows:
  print(row)