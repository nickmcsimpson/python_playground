def take(count, iterable):
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


def distinct(iterable):
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)


def run_pipeline():
    items = [3, 6, 2, 1, 1]
    for item in take(3, distinct(items)):
        print(item)


"""Generators are lazy and only evaluate the values they need to.

    itertools is a package with a bunch of iterable generators
"""

run_pipeline()
