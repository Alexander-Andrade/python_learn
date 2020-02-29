def func_signature(*args, **kwargs):
    args_repr = [repr(a) for a in args]
    kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
    return ", ".join(args_repr + kwargs_repr)


def log(func):
    def wrapper_log(*args, **kwargs):
        try:
            signature = func_signature(*args, **kwargs)
            print(f"Info: Calling {func.__name__!r}({signature})")
            result = func(*args, **kwargs)
        except Exception as e:
            print(f"Error: Method {func.__name__!r} raised an exception {e!r}")
            raise
        if result is None:
            print(f"Warning: Method {func.__name__!r} returned None")
        return result
    return wrapper_log


class Logger(type):
    def __new__(cls, name, bases, dct):
        for attr_name, attr_value in dct.items():
            if callable(attr_value):
                dct[attr_name] = log(attr_value)
        return super().__new__(cls, name, bases, dct)


class Bar(metaclass=Logger):
    def raise_exception(self):
        raise RuntimeError('Something has happened')

    def return_none(self):
        return None

    def hello_name(self, name):
        return f"Hello, {name}!"


if __name__ == "__main__":
    b = Bar()

    try:
        b.raise_exception()
    except:
        pass

    b.return_none()

    b.hello_name("Alex")
