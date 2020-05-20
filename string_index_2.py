#!/usr/bin/python3.5

# Indices may also be negative numbers, to start counting from the right
# Note that since -0 is the same as 0, negative indices start from -1

str = 'Python'
print ("Indexing string 'Python' and value of [-1] is : ", str[-1])
print ("Indexing string 'Python' and value of [-6] is : ", 'Python'[-6])

# Below line will throw an error "IndexError: string index out of range"
#print ("Indexing string 'Python' and value of [-80] is : ", 'Python'[-80])
