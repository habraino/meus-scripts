class Decorator(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Before the function call.')
        res = self.func(*args, **kwargs)
        print('After the function call.')

        return res

import types

@Decorator
def testfunc():
    print('Inside the function.')

a = isinstance(testfunc, types.FunctionType)
print(a)
print(type(testfunc))

#------------------------------------------
def decoratorfatory(mesage):
    def decorator(func):
        def wrapped_func(*args, **kwargs):
            print('The decorator want to tell you: {}'.format(mesage))
            return func(*args, **kwargs)
        return wrapped_func
    return decorator


@decoratorfatory("Hello Brayen")
def test():
    pass

test()
