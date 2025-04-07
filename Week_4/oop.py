# Define a class

class Car:
  # class attributes

  wheels = 4
  vendor = "cfao"
  # constructor method
  # instance attributes
  def __init__(self,color,make,year):
    self.color = color
    self.make = make
    self.year = year


# instantiate an object

car1 = Car("Beige","Benz",1998)

car1.color

car2 = Car("Black","Jeep",2024)

car2.year

car1.wheels

car1.vendor

car2.wheels

# Define a class

class Car:
  # class attributes

  wheels = 4
  vendor = "cfao"
  # constructor method
  # instance attributes
  def __init__(self,color,make,year):
    self.color = color
    self.make = make
    self.year = year

  def describe(self):
    print(f"This is a {self.color}, {self.make}, {self.year}")
    
  # define new method

  def drive(self,task):
    print(f"This is a {self.color}, {self.make}, {self.year}, I {task}")

car1 = Car("Beige","Benz",1998)

car2 = Car("Black","Jeep",2024)

car1.describe()

car2.describe()

car1.drive("Drive smoothly")


# Inheritance : a class take on the methods and attributes of another class
class Car:

  wheels = 4
  vendor = "cfao"
  def __init__(self,color,make,year):
    self.color = color
    self.make = make
    self.year = year

  def describe(self):
    print(f"This is a {self.color}, {self.make}, {self.year}")

# subclass or derived class

class ElectricCar(Car):
  def __init__(self,color,make,year,battery):
    super().__init__(color,make,year)
    self.battery = battery
  
  def describe_electric(self):
    print(f"This is a {self.color}, {self.make}, {self.year}, with a {self.battery}")

car1 = ElectricCar("White","Range Rover",2020,1000)

car1.wheels

car1.battery

car1.color

car1.describe()

car1.describe_electric()