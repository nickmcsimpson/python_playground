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

"{0} north of {1}".format(59.6, 888)# inject variable into strings

"Galactic position x={pos[0]}, y={pos[1]}, z={pos[3]}".format(pos=(65.2, 23.1, 82.2))

# F strings embed expressions with minimal syntax
f'one plus one is {1+1}'
