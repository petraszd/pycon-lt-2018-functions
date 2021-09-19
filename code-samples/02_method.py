from types import MethodType


def a_function(self, a_param):
    return self.a_attribute + a_param


class A_Class:
    def __init__(self):
        self.a_attribute = 2


a_object = A_Class()
a_method = MethodType(a_function, a_object)
print(a_method)
print(a_method(3))
