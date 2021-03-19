"""When ran, times the result of another function"""
import sys
import time
from functools import wraps


def time_sequence(function):
    @wraps(function)
    def timer(*args, **kwargs):
        start = time.time()
        # run function
        function(*args, **kwargs)
        end = time.time()

        elapsed = end - start
        print("%.3f" % elapsed)
    return timer


@time_sequence
def count_to(value):
    count = 0
    while count < int(value):
        count += 1
    print(f"Counted to {value}:{count} for you")


if __name__ == '__main__':
    count_to(sys.argv[1])

