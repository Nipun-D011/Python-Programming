"""name = "CodePRO LK"

print(name)
print(name.capitalize())  # Capitalizes the first letter
print(name.upper())  # Converts to uppercase
print(name.lower())  # Converts to lowercase
print(name.title())  # Capitalizes the first letter of each word"""

#find() and Index() methods
#find
# name = "CodePRO LK"
#print(name.find('o'))  # Returns the index of the first occurrence of 'o'
#print(name.find('LK',4,10))  # Returns the index of 'LK' starting from index 4 to 10
#print(name.rfind('o'))  # Returns the index of the last occurrence of 'o'

#index
"""name = "CodePro LK"
print(name.index("o",2,8))  # Returns the index of 'o' starting from index 2 to 8"""

#center() method
"""name = "codepro lk"
print(name.center(20))  # Centers the string in a field of 20 characters
print(name.center(20, '*'))  # Centers the string and fills with '*'"""


#justify() method
"""name = "codepro lk"
print(name.ljust(20))  # Left justifies the string in a field of 20 characters
print(name.rjust(20))  # Right justifies the string in a field of 20 characters
print(name.ljust(20, '*'))  # Left justifies and fills with '*'"""

#strip() method
"""name = "   codepro lk   "
print(name.strip())  # Removes leading and trailing whitespace
print(name.lstrip())  # Removes leading whitespace
print(name.rstrip())  # Removes trailing whitespace"""


#startswith() and endswith() methods
#startswith()
"""name = "CodePRO LK"
print(name.startswith("Code"))  # Returns True if the string starts with 'Code'
print(name.startswith("LK", 8))  # Returns True if the substring 'LK' starts at index 8"""

#endswith()
"""name = "CodePRO LK"
print(name.endswith("LK"))  # Returns True if the string ends with 'LK'
print(name.endswith("PRO", 4, 8))  # Returns True if the substring 'PRO' ends at index 8 and starts at index 4"""



#replace() method"
"""x = "Kamal, 22 , colombo"

print(x.replace("Kamal", "nipun"))  # Replaces 'Kamal' with 'nipun'
print(x.replace("22", "23"))  # Replaces '22' with '23'
print(x.replace(",", ":", 1))  # Replaces the first occurrence of ',' with ':'  """


#join() method
"""x = 'abc'
y = 'xyz'
print(x.join(y))  # Joins 'xyz' with 'abc' in between each character"""


#split() method
"""name ="nimal kamal saman\n 45 65 23"
print(name.split())  # Splits the string into a list of words
print(name.split(' ')) # Splits the string by spaces
print(name.split('\n'))  # Splits the string by newline character
print(name.split(' ', 2))  # Splits the string by spaces, but only splits at most 2 times"""