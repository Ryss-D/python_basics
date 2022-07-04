Class Person:
	## This is the initilizacer or constructor on class
	def __init__(self,name, age):
		self.name = name
		self.age = age
	## This is the default way our application convers our object to string
	## ieg when we pass it to a print
	def __str__(self):
		return f"Person {self.name}, {self.age} years old"
	## This the default way our object will appear in debugger or
	## things llike that if no __str__ methos is passed the __repr__
	## methos will thake their place 
	def __repr__(self):
		return f"<Person({self.name}, {self.age}>"

bob = Person("Bob", 35)
print(bob)
