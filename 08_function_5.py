def g(y, x=0): #when keyword arguement is written first python gives a default error; therefore the required arguement(y) is written first in here
	return x+y

print(g(5)) #if you do not provide a value for the keyword arguement (x), the default value is used. Providing a value for keyword arguement is optional.

print(g(4, x=3))
