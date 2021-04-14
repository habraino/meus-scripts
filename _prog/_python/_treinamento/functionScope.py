a = 'global'

class Test:
    a = 'class'
    b = (a for i in range(10)) # function scope
    c = [a for i in range(10)] # function scope
    d = a # class scope
    e = lambda : a # function scope
    f = lambda a = a : a # default argument use class scope

    @staticmethod # or @classmethod, or regular instance method
    def g(): # function scope
        return a

print(Test.a) # class
print(next(Test.b)) # global
print(Test.c[0]) # class in Python 2, global in Python 3
print(Test.d) # class
print(Test.e) # global
print(Test.f) # class
print(Test.g()) # global

