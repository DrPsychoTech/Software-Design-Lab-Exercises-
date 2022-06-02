"Exercise Item No.3"
"Class B extends class A. Class B defines an __str__ method that returns the string"
"representation of its instance variables. Class B defines a single instance variable"
"named age, which is an integer. Write the code to define the __str__ method for"
"class B. This method should return the combined string information from both"
"classes. Label the data for age with the string age:"

class A:
  def __init__(self, age,ok):
    self.age = age
    self.ok = ok

  def __str__(self):
    return f'Age is {self.age}'

  def age(self):
    return f'Age is {self.ok}'

class B:
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

p=A(19,"Age")

print(p.__str__())
print(p.ok)
