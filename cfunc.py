import ctypes


class C_function:
    """This class wraps a Python function into its C equivalent in the given library"""

    types = ctypes.__dict__

    @classmethod
    def register_type(cls, typename, obj):
        """Add an acceptable argument or retval type to this."""
        cls.types[typename] = obj

    def __init__(self, dll, error_check=None):
        """Set the library to reference the function name against."""
        self.library = isinstance(dll, ctypes.CDLL) and dll or ctypes.CDLL(dll)
        self.error_check = error_check

    def __call__(self, f):
        """Performs the actual function wrapping.

        This extracts function details from annotations and signature.
        For example, to wrap puts, the following suffices (on Linux):

            >>> @C_function("libc.so.6")
            ... def puts(my_string: "c_char_p") -> "c_int":
            ...     return puts.c_function(my_string)
            ...
            >>> x = puts("hello, world!")
            hello, world!
            >>> x
            14

        Note that to call the actual C function, you just reference
        it by asking for the local function's .c_function attribute.
        """

        # get the function's name, arguments, and arg types
        name = f.__name__
        args = f.__code__.co_varnames
        annotations = f.__annotations__

        # get the function itself
        function = self.library[name]

        # set the function's call signature
        argtypes = []
        for arg in args:
            annotation = annotations[arg]
            if isinstance(annotation, basestring):
                # if its a pointer
                if annotation.startswith("*"):
                    argtypes.append(ctypes.POINTER(self.types[annotation[1:]]))
                # Kinda hackish ~treannotationorj
                #elif '*' in annotation and not annotation.endswith('*'):
                #    annotation, count = annotation.split('*', 1)
                #    count = int(count)
                #    field_type = self.types[annotation] * count
                else:
                    argtypes.append(self.types[annotation])
            elif isinstance(annotation, object):
                argtypes.append(annotation)
            else:
                raise Exception("Bad annotation '%s'" % annotation)

        function.argtypes = argtypes

        # and its return value
        restype = annotations['return']
        if isinstance(restype, basestring):
            if restype.startswith("*"):
                function.restype = ctypes.POINTER(self.types[restype[1:]])
            else:
                function.restype = self.types[restype]
        elif isinstance(restype, object):
            function.restype = restype
        else:
            raise Exception("Bad restype '%s'" % annotation)

        # set its error handler
        if self.error_check:
            function.errcheck = self.error_check

        # set the c_function as an attribute of f
        f.c_function = function

        return f

"""

How To Use It
Let's say I want to wrap a C function with the following signature

int process_foo(int bar);

from libfoo.so. Using this decorator, I could simply write the following Python:

>>> @C_function("libfoo.so")
... def process_foo(bar: "int") -> "int" :
...     return process_foo.c_function(bar)
...
I could then call that just as I would any other Python function:

>>> process_foo(5)
7
It also works with pointers- simply prefix the type with a *- and allows you to add types via C_function.register_type.

"""
