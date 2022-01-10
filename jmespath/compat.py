import inspect


def with_metaclass(meta, *bases):
    # Taken from flask/six.
    class metaclass(meta):
        def __new__(cls, name, this_bases, d):
            return meta(name, bases, d)
    return type.__new__(metaclass, 'temporary_class', (), {})


def get_methods(cls):
    yield from inspect.getmembers(cls,
                                           predicate=inspect.isfunction)
