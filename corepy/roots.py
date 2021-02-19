import sys


def sqrt(x):
    """Compute square root using the method of Heron Alexandria

    Args:
        x: the number for which to find the square root

    Returns:
        The square root of x
    """
    if x < 0:
        raise ValueError(f"Cannot compute the square root of negative number {x}")

    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess


def main():
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))
    #     Will terminate immediately when error is thrown
    except (ZeroDivisionError, ValueError) as e:
        print(e, file=sys.stderr)
        # We shouldn't handle ZeroDivision here, because the function knows what it can't work with.


if __name__ == '__main__':
    main()
