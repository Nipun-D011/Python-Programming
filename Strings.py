name  = "CodePRO LK"
""" C  o d e P R O   L K
    0  1 2 3 4 5 6 7 8 9
   -10-9-8-7-6-5-4-3-2-1"""

"""print(name[0])  # Output: C   This is indexing(positive indexing)
print(name[4:7])  # Output: PRO   This is slicing
print(name[-1])  # Output: K   This is indexing(negative indexing)
print(name[-3:])  # Output: LK   This is slicing with negative indexing"""

"""s1 = "Python"
s2 = "Programming"

print(s1 + " " + s2)  # Output: Python Programming"""

s1 = "Python"
s2 = "Programming"
s3 = 45

#print(s1 + " " + s2 + 45)  # This will raise an error because we cannot concatenate a string with an integer directly.
# To fix this, we need to convert the integer to a string first.
print(s1 + " " + s2 +" "+ str(s3))  # Output: Python Programming 45