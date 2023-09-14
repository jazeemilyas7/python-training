a=5 
result=100/700
b="abcdefg"
name="Jazeem"
c= "Hello, How are you?"
print (type(a)) # Data Type
print (len("abcd")) # String Length
print (b[0])  #Indexing
print (b[-1]) #Negative Indexing to get last letter in a string
print (b[2:5]) #Slicing, stop index upto 5, 5 not included
print (b[2:5]) #Slicing
print (b[::2]) #Slicing with step size
print (b[::-1]) #Slicing with step size to reverse a string
print (b + " add") # string concatination | string interpolation
print (b * 10) # string multiplication
print (b.upper()) #Inbuilt string methods
print (c.split()) #Inbuilt string methods
print ("This is a string {}".format("Inserted")) # string int   erpolation
print ("The {1} {0} {2}".format("brown","quick","fox"))
print ("The result is {r:20.3f}".format(r=result)) # Float formatting
print (f"Name is {name}") # f string python 3.6