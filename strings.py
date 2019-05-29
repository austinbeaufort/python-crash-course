name = 'Austin'
age = 26

#Concatenate
# print('Hello, my name is ' + name + ' and I am ' + str(age))

#String Formatting

#Positional Arguments
# print('My name is {name} and I am {age}'.format(name=name, age=age))

#F-Strings 
# print(f'Hello, my name is {name} and I am {age}')

# String Methods
s = 'hello world'

#Capitalize string
print(s.capitalize())
print(s.upper()) #all upper
print(s.lower()) #all lower
print(s.swapcase()) #swaps cases
print(len(s)) # length of string
print(s.replace('world', 'everyone'))

#Count
sub = 'h'
print(s.count(sub)) # prints number of 'h' in a string

print(s.startswith('hello'))
print(s.endswith('d'))

#Split into a list
print(s.split())
print(s.find('r'))
print(s.isalnum()) # true if all values are nums and letters
print(s.isalpha())
print(s.isnumeric())
