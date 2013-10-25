
import sys


def get_func_name(frame=1):
    """Get function name in stack frame=frame"""
    # By calling sys._getframe(1), you can get this information
    # for the *caller* of the current function.
    return sys._getframe(frame).f_code.co_name

get_current_func_name = get_func_name


def get_caller_func_name():
    """Get function name of the caller of the caller of this function"""
    return get_func_name(frame=3)

get_last_func_name = get_caller_func_name
