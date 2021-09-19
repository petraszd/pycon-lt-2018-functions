import ctypes


py_cell_new = ctypes.pythonapi.PyCell_New
py_cell_new.restype = ctypes.py_object

py_set_closure = ctypes.pythonapi.PyFunction_SetClosure


def make_closure():
    a = 1
    b = 2

    def result():
        return a + b

    return result


a_closure = make_closure()
print(a_closure())

a_tuple = tuple([
    py_cell_new(ctypes.py_object(222)),
    py_cell_new(ctypes.py_object(444)),
])
py_set_closure(
    ctypes.py_object(a_closure),
    ctypes.py_object(a_tuple),
)

print(a_closure())
