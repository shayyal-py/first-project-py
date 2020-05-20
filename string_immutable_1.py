#!/usr/bin/python3.5

# Python strings cannot be changed — they are immutable

myStr = 'Python'

# Below statement will throw an error
# TypeError: 'str' object does not support item assignment
#myStr[0] = 'J'

# If you need a different string, you should create a new one
print ('New string created after \'J\' + [1:] : ', 'J' + myStr[1:])
 
