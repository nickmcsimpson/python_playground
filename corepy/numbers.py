def square(x):
    return x*x

def even_or_odd(n):
    if n % 2 == 0:
        print('even')
        return
    print('odd')
    # no return so automatically None

def nth_root(radicand, n):
    return radicand ** (1/n)

def ordinal_suffix(value):
    s = str(value)
    if s.endswith('11'):
        return 'th'
    elif s.endswith('12'):
        return 'th'
    elif s.endswith('13'):
        return 'th'
    elif s.endswith('1'):
        return 'st'
    elif s.endswith('2'):
        return 'nd'
    elif s.endswith('3'):
        return 'rd'
    return 'th'

def ordinal(value):
    return str(value) + ordinal_suffix(value)

def display_nth_root(radicand, n):
    root = nth_root(radicand, n)
    message = "The " + ordinal(n) + " root of " \
        + str(radicand) + " is " + str(root)
    print(message)
