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
