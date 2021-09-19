import ctypes
import dis
from types import CodeType


py_cell_new = ctypes.pythonapi.PyCell_New
py_cell_new.restype = ctypes.py_object

py_set_closure = ctypes.pythonapi.PyFunction_SetClosure


def simple_addition():
    return a + b


try:
    simple_addition()
except NameError:
    print("Can not call it")
    print()


dis.dis(simple_addition)
print()


code = simple_addition.__code__
co_code = code.co_code[:]
load_vars = bytes([
    dis.opmap['LOAD_DEREF'], 0,
    dis.opmap['LOAD_DEREF'], 1
])
co_code = load_vars + co_code[4:]
freevars = tuple(['a', 'b'])
new_code = CodeType(
    code.co_argcount,
    code.co_kwonlyargcount,
    code.co_nlocals,
    code.co_stacksize,
    code.co_flags,
    co_code,  # <-------------- CODE GOES HERE
    code.co_consts,
    code.co_names,
    code.co_varnames,
    code.co_filename,
    code.co_name,
    code.co_firstlineno,
    code.co_lnotab,
    freevars,  # <----------- FREEVARS GOES HERE
    code.co_cellvars,
)

cells = tuple([
    py_cell_new(ctypes.py_object(222)),
    py_cell_new(ctypes.py_object(444)),
])
py_set_closure(
    ctypes.py_object(simple_addition),
    ctypes.py_object(cells),
)
simple_addition.__code__ = new_code

print('---------------->', simple_addition())

print()
print()

dis.dis(simple_addition)
