import functools


class Cache:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.__func = func
        self.__cache = {}

    def __call__(self, *args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in self.__cache:
            self.__cache[cache_key] = self.__func(*args, **kwargs)
        return self.__cache[cache_key]
