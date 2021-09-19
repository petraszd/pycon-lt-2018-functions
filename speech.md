# Functions: What a Concept

Hello.

My name is Petras Zdanavičius and today I am going to give a talk about
functions.

It is my first talk in English. So... Good luck to you all my dear audience.


# About me

Who am I. I am a Python programmer.

I earn my Euros to buy bread and games by doing Web developing. Of course,
nowadays I am calling it full stack engineering. It is a marketing trick and it
gives me more Euros. But it is the same old web development.


# About this talk

About this talk. What it is going to be.

I will start with basics.

I will start really easy and slow and than I will dive deep. After diving deep
I will give a shotgun which is really good and shooting both legs out.


# A Function (Math) #1

So. Basics.

What is a function. Wikipedia gives us this.

[Read it out loud]

Which sounds a little bit confusing. But what it says is this.


# A Function (Math) #2

Function input goes in. And output goes out.

It would be really good definition if we would be here at functional
programming conference. But we are not.

We are at Python conference. And Python is much more better language than
functional languages. It let's you just print "Hello World" on the screen
without feeling shame and than calling it a side effect.


# A Function (Programming) #1

What is a Python function? Or what is a function in any imperative programming
language?

[Read it out loud]


# Memory

OK. A side topic.

I remember when first time I've learned about functions. I was around 16 or 17
then. And we were learning about programming in our school. We were using
Turbo Pascal back then.

I was way better than my computer science teacher. Don't get me wrong. I was
horrible programmer. But... I was just better than my teacher. So I was
reading and learning on my own.

And I remember I've read about functions in Pascal. I've tried them out. Write
some code with functions.

Gave it a really good thought. And decided that. Nah! I do not like them.
Functions are stupid. It much more easy to copy paste and tweak code manually
where function parameters are suppose to be injected).

I think I was just a little bit wrong.


# A Function (Programming) #2

Advantages.

Reducing duplication. Right. Don't repeat yourself. Really good quality of any
function.

It also let's you decomposition complex problem into small simple ones and
solve them one by one.

Another advantage is encapsulation. It allows you to hide complex computations
under some nice simple interface.


# A Function (Python) #1

[Read it out loud]

So it is a object. A callable object. That does something and may return
something.


# A Function (Python) #2

This is it. A function. A Python function.


# CPython Object

And let's look how function is represented inside CPython code.

First of all, function is a object. Now let's look into how CPython represents
a object.

As you can see it is quite simple. First two items are Memory + GC related
items.

Last one is a pointer to type object. Nothing special here.


# CPython Function

Every concrete build-in Python type has it's own struct inside CPython C code.
This is a function struct definition.

* `PyObject_HEAD`: It is a macro to inject `ob_base`.
* `func_code`: It is a function's code
* `func_globals`: It is a reference to globals dict
* `func_defaults`: It is a reference to default arguments
* `func_kwdefaults`: And default keyword arguments
* `func_closure`: Tuple of cell objects. We will talk about those later
* `func_doc`: Documentation
* `func_name`: Name
* `func_dict`: Dictionary
* `func_weakreflist`: It is a weak reference list. It is about memory
* `func_module`: It is a module where this function is defined
* `func_annotations`: Function annotations
* `func_qualname`: A name with additional information


# CPython: Code Object

We will not go through each of these items. But for example:
* `co_argcount`: holds number of function's arguments
* `co_nlocals`: holds number of local variables
* `co_code`: is the most interesting one. It holds bytecode. Python is
  compiled language. And compiled bytecode of each function is stored within
  this variable.


# Demo: Functions

I think it is time for a demo. So we have a function. It has two arguments.
One with default parameter. It uses one global variable and one local
variable. And what it does. It adds all four of them together.

Let's explore.

```python
ipdb> a_function
ipdb> type(a_function)
ipdb> for x in dir(a_function): print(x)
ipdb> a_function.__defaults__
(3,)
ipdb> a_function.__code__.co_argcount
2
ipdb> a_function.__code__.co_code
b'd\x01}\x02t\x00|\x00\x17\x00|\x01\x17\x00|\x02\x17\x00S\x00'
ipdb> a_function.__code__.co_names
('a',)
ipdb> a_function.__code__.co_nlocals
3
ipdb> a_function.__code__.co_varnames
('b', 'c', 'd')
ipdb> a_function.__code__.co_consts
(None, 4)
ipdb> import dis
ipdb> dis.dis(a_function)
  5           0 LOAD_CONST               1 (4)
              2 STORE_FAST               2 (d)

  6           4 LOAD_GLOBAL              0 (a)
              6 LOAD_FAST                0 (b)
              8 BINARY_ADD
             10 LOAD_FAST                1 (c)
             12 BINARY_ADD
             14 LOAD_FAST                2 (d)
             16 BINARY_ADD
             18 RETURN_VALUE
```

OK. So we have `a_function` object. What it's type is? OK. It is a function.
Cool. Now it has defaults tuple. But for us the most interesting part is
`__code__` object.

`co_argcount` -- accepts two arguments
`co_code` -- it is compiled bytecode. So python is compiled language. It is
binary
`co_names` -- stores names accessed from global scope. Our uses `a` and we see
it here.
`co_nlocals` -- it has 3 local variables. Two function parameters and 1
defined locally.
`co_varnames` -- as you can see from variable names parameter.
`co_consts` -- it stores two constants. Function always stores pointer to None
cause every Python function returns None by default. And our function also
stores pointer to `4`. Cause it is used by our local variable `d`.

There is also cool Python module `dis`. And using `dis.dis` we can see human
readable byte code representation.


# CPython Bound Method

Very shortly about bound methods. Each method defined inside a class is a
function. But when you create a object then object has bound methods attached
to itself.

This is how it looks in C code. Very simple structure. It just has pointer to
self and pointer to function itself.


# Demo: Bound Method

It is interesting that Python exposes method type within itself. You can
import it from `types` module.

You can see that we have a simple function. Than we have a class. And inside
constructor we assign `a_attribute` to 2.

Then using `MethodType` we construct bound method.

And let's run it. It suppose to print 5. Yep. It prints five.

So bound method is not the same thing as function. It is object which has a
reference to function.


# Demo: Closures

Let's go back to functions. This time it is going to be demo about closures.

What is a closure. It is a technique to bind a function to local variables. It
is only possible if a function is first class citizen. Which it is in Python.

We have a closure factory `make_closure`. It creates function which has access
and uses two local variables. One is immutable and other is mutable.

```python
ipdb> a_closure.__closure__
(<cell at 0x109b57048: int object at 0x1097faa90>, <cell at 0x109b57078: dict object at 0x1099998b8>)
ipdb> a_closure.__closure__[0].cell_contents
2
ipdb> a_closure.__closure__[1].cell_contents
{'foo': 1}
ipdb> a_closure()
3
ipdb> a_closure.__closure__[1].cell_contents['foo'] = 100
ipdb> a_closure()
4
ipdb> a_closure.__closure__[0].cell_contents
2
ipdb> a_closure.__closure__[0].cell_contents += 1
*** AttributeError: attribute 'cell_contents' of 'cell' objects is not writable
```

First let's call `a_closure()`. OK. It returns 3. Cause dictionary's foo is 1
immutable is 2. And we adding them.

Let's see what `__closure__` holds. It is not empty. It holds two cell
objects.

First points to immutable. Second to mutable dictionary. Let's change it.
Let's set 'foo' to 100. It works.

Call `a_closure()` again. 102. We have just changed hidden variables.
That is nice. And dangerous.

The problem. We can't update immutable as easy. If we try it then it throws an
error. Cause it is immutable.


# Before Shooting My Foot Out: Function

But I will show you haw to change it.

First. Let's remember repeat how C stores Python function.

So there is `PyFunctionObject`. For now we only care about `func_code` and
`func_closure`.

* `func_closure` will point to a tuple with content of closure.
* `func_code` will point to `PyCodeObject`.


# Before Shooting My Foot Out: Code

And we care about those two attributes of code objects.

* `co_code` it is byte code
* `co_freevars` it is a tuple of names used by `func_closure`.


# Demo: Warm Up With Closures

`ctypes` it is foreign function library in Python. It allows to access
functions in dynamic linked libraries. `*.dll` files in windows `*.dynlib`.
And `*.o` files in Unix.

And it also exposes CPython functions inside a Python. So you can start
calling CPython code inside your Python code. What can go wrong?

Everything. When the last time anyone got segmentation fault while using
Python. Almost never. Right? Not when you try to use `ctypes`. Then you will
get segmentation faults all the time.

But we are going to use `ctypes` to replace closure immutable variables.


# Demo: Injecting Variables

[Free styling]


# Thank You

That is end of my talk. I hope that was interesting. If it does. My code
samples are here.

Also I've already uploaded my slides.

If you have any question I am happy to answer them.
