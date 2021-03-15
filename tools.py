from typing import Optional


def get_nested(obj, path, divider='.'):
    if divider in path:
        first_step = path.split(divider)[0]
        new_key = path.removeprefix(f"{first_step}{divider}")
        return get_nested(obj.get(first_step), new_key)
    else:
        return obj.get(path)


obj = dict(outer=dict(inner='result', empty={}))

print(get_nested(obj, 'outer.inner'))
print(get_nested(obj, 'outer.empty'))

# dotted = DotFindString(obj)
