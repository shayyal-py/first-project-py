#!/usr/bin/python3.5

# Slicing allows you to obtain substring
# Note: Start is always included, and the end always excluded

str = 'Hello World'
print("After slicing string 'Hello World' as [2:4] : ", str[2:4])

print ("After slicing string 'Hello World' as [3:7] : ", 'Hello World'[3:7])

print("After slicing string 'Hello World' as [2:] : ", str[2:])
print("After slicing string 'Hello World' as [:4] : ", str[:4])

print("After slicing string 'Hello World' as [:3] + [3:] : ", str[:3] + str[3:])

print("After slicing string 'Hello World' as [:80] : ", str[:80])
print("After slicing string 'Hello World' as [80:] : ", str[80:])
print("After slicing string 'Hello World' as [:] : ", str[:])
