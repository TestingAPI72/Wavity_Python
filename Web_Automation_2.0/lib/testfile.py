# creating class A
class A:
    def getter(func):
        def inner(self):
            print('Started')
            func(self)
        return inner

    @getter
    def get_age(self):
        print('Yes')

ob = A()
ob.get_age()