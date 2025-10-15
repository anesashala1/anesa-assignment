#print("Hello world!")
lambda_new = 1
print(lambda_new) # printing the lambda_new variable
# How to name our variables in Python

a = 3
print(type(a))
b = 1.2
print(type(b)) #in this case only the last "type()" is shown in the output window, for both of them to show, we should use the "print" command
c = 'a'
d = "abc"
e = "dsfs"

# Fundamental types
# integers, float, boolean, complex numbers
i = True
j = False
print(i+j)
print(i*j)

#Operators
# the power operator in python is ** => 2**3=8
# 10//6=1  => "//" loses the decimal points
# 2/1=2.0  => "/" this always returns a float type

 # for comparison
x = 2
y = 3
z = 3

# if we do z==y we are checking if these are equal
# if we do z=y we are overwriting the value of z to the value of y

#Strings

s = "Hello Monty!"
# the "len" command shows how manny characters are in a string variable

print(s.replace('Monty','Python'))

# command "s[0:5]" prints the first five characters
# command "s[-6:]" prints from the 6th character until the end
# command "s[:]" print the whole string
# command "s[::2]" prints every two characters of the string => 'HloMny'

s2 = "Hello Monty Python!"

# command "s2.split(' ')" splits the string word for word => 'Hello', 'Monty', 'Python!'
# command "s2.split(' ')[1]" => 'Monty' 
# command "s2.split('o')" => 'Hell', 'M', 'nty Pyth', 'n!'
# command "print('Hello \n world!')" => 
# Hello
# world!
# "\n" puts it in the next row 
# command "''.join(['Monthy', 'Python'])" => 'MonthyPython'

a = 4
print("The outcome of interest is", a)
print('The first outcome of interest is %.2f', a)