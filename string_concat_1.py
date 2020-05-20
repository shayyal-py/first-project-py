#!/usr/bin/python3.5

# Strings can be concatenated (glued together) with the + operator

print ("String concatenated using 'Py' + 'thon' : ", 'Py' + 'thon')

# Two or more string literals (i.e. the ones enclosed between quotes) 
# next to each other are automatically concatenated.

print("String concatenated using 'Py' 'thon' : ", 'Py' 'thon')

text = ('Put several strings within parentheses '
        'to have them joined together.')

print (text)

# If you want to concatenate variables or a variable and a literal, use +
prefix = 'Py'
print ("String concatenated using variable : ", prefix + 'thon')

# This only works with two literals though, not with variables or expressions
# Below line will throw an error
#print ("String concatenated using variable iwill not work: ", prefix 'thon')
