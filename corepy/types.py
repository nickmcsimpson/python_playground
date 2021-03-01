""" All types in Python are Objects

    Strongly types and not coerced

    Object names function like pointers

"""

import time

m = [9, 15, 24]

def modify(k):
    k.append(39)
    print("k= ", k)

def replace(g):
    g = [16, 3, 9]
    print("g= ", g)

def banner(message, border="-"):#Default params
    line = border * len(message)
    print(line)
    print(message)
    print(line)

def show_default(arg=time.ctime()): # Time is bound at runtime and will not progress when called again
    print(arg)

def add_spam(menu=[]): # empty list is created then will reference the same object when called again
    menu.append("spam")
    return menu
# Always use immutable types as default args

count = 0

def show_count():
    print(count)

def set_count1(c):
    count = c # This is a locally bound variable and doesn't modify the global var

def set_count(c):
    global count
    count = c # Now this will work

"""Built in collections


"""

#Tuples

#Strings

s = "New" + "found" + "land"

s += " city"# += creates temporaries

s.join('Do you know the way?')

"unforgetable".partition('forget')
# ('un', 'forget', 'able') Tuple

# Tuble unpacking
origin, _, destination = "Seattle-Boston".partition('-') # unpacked into unused variable

"{0} north of {1}".format(59.6, 888)
# inject variable into strings

"Galactic position x={pos[0]}, y={pos[1]}, z={pos[2]}".format(pos=(65.2, 23.1, 82.2))

# F strings embed expressions with minimal syntax
print(f'one plus one is {1+1}')

# Lists

r = [1, -4, 10, -16, 15]

# Negative indices count backwards from end
print(r[-1])
# gives you 15

print(r[-2])
# gives you -16

# Slice a list:
s = [14, 1555, 1690, 170, 189, 199]
print(s[1:3])
# [1555, 1690]
print(s[1:-1])
# [1555, 1690, 170, 189]
print(s[2:])
# [1690, 170, 189, 199]
print(s[:2])
# [14, 1555]
print(s[:])# shallow copy option
# [14, 1555, 1690, 170, 189, 199]
u = s.copy()

# index()
w = "the quick bronw fox jumps over the lazy dog".split()# default split on space

a = [ [1,2], [3,4] ]
b = a[:]
# results in a shallow copy and object references are the same


w = "the quick bronw fox jumps over the lazy dog".split()
print(w)
# ['the', 'quick', 'bronw', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
i = w.index('fox')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'builtin_function_or_method' object is not subscriptable
i = w.index('fox')
print(i)
# 3
print(w[i])
# 'fox'
# print(w.index('unicorn'))
# Traceback (most recent call last):
  # File "<stdin>", line 1, in <module>
# ValueError: 'unicorn' is not in list
w.count('the')
# result: 2
del w[3]
print(w)
# ['the', 'quick', 'bronw', 'jumps', 'over', 'the', 'lazy', 'dog']
w.remove('bronw')
print(w)
# ['the', 'quick', 'jumps', 'over', 'the', 'lazy', 'dog']


# Dictionaries
# Order can't be counted on
d = dict(a="ni")
movies = dict(a="Wolf of Wallstreet", b="Dark Knight", c="Mr Nobody")
print(movies)
# {'a': 'Wolf of Wallstreet', 'b': 'Dark Knight', 'c': 'Mr Nobody'}
# iterate through keys: movies.keys()
# iterate through values: movies.values()
for key, value in movies.items():
    print(f"{key} => {value}")

# a => Wolf of Wallstreet
# b => Dark Knight
# c => Mr Nobody


#  SET
x = {1, 2, 3, 4}

x.add(5)






