from cache import Cache


@Cache
def fibonacci_numbers(n):
    assert n >= 0
    if n < 2:
        return n
    else:
        return fibonacci_numbers(n-1) + fibonacci_numbers(n-2)