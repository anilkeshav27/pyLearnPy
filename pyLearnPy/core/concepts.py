from pynput.keyboard import Key, Controller
import time
import re
from ctypes import wintypes, windll, create_unicode_buffer
import os
import platform

keyboard = Controller()

__all__ = ["learn"]


def _core_printer(concept, **kwargs):
    if platform.system() == "Windows":
        isTypeFast = True
        if "speed" in kwargs:
            if not kwargs["speed"]:
                isTypeFast = False
        output = concept()
        if _get_foreground_window_title().find("Visual Studio Code"):
            with keyboard.pressed(Key.ctrl): 
               keyboard.press("1")
               keyboard.release("1")
            _jump_end_of_file()
            for char in output:
                if _get_foreground_window_title().find("Visual Studio Code"):
                    if char == ";":
                        keyboard.press(Key.enter)
                        keyboard.release(Key.enter)
                    elif char == "<":
                        keyboard.press(Key.home)
                        keyboard.release(Key.home)
                    else:
                        keyboard.press(char)
                        keyboard.release(char)
                    if isTypeFast:
                        time.sleep(0.05)
                    else:
                        time.sleep(0.13)
                else:
                    print("VSS Code not found: pyLearnPy only supports VSS code")
                    exit()
            keyboard.press(Key.end)
        else:
            print("VSS Code not found: pyLearnPy only supports VSS code")
            exit()
    else:
        print("pyLearnPy only supports Windows")
        exit()


def _get_foreground_window_title():
    hWnd = windll.user32.GetForegroundWindow()
    length = windll.user32.GetWindowTextLengthW(hWnd)
    buf = create_unicode_buffer(length + 1)
    windll.user32.GetWindowTextW(hWnd, buf, length + 1)

    # 1-liner alternative: return buf.value if buf.value else None
    if buf.value:
        return buf.value
    else:
        return None


def _jump_end_of_file():
    keyboard.press(Key.end)
    keyboard.release(Key.end)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    keyboard.press(Key.home)
    keyboard.press(Key.enter)
    """ with keyboard.pressed(Key.ctrl):
        keyboard.press(Key.end)
        keyboard.release(Key.end)
    keyboard.press(Key.home) """


def _learn_function():
    return r"""def my_function():; 
return 'a';;
<tmp = my_function();
print(tmp)"""


def _learn_classes():
    return r"""class My_Class:; 
def __init__(self,initialValue):;
self.value=initialValue ;;
<obj = My_Class(1);
print(obj.value)"""


def _learn_contextManager_as_function():
    return r"""# PLEASE IMPORT : from contextlib import contextmanager;
@contextmanager;def context_manager_name(name,mode):
;#insert your code to be called when the context is opened;
yield f;
# insert your code when the context is closed;;
<# When the context is opended using with statement, everything till yield is executed and after the context scope is completed statements after yield are executed;
<with context_manager_name() as f:;
None"""


def _learn_threading_basic():
    return r"""#PLEASE IMPORT : import threading;
def worker_thread(num):;
print('Worker: %s' % num);
# Code for the task that needs to be parallely executed;
return ;;
<# to begin 2 threads in parallel;
<for i in range(2):;
t = threading.Thread(target=worker_thread, args=(i,));
t.start()"""


def learn_regex_patterns():
    return r"""# .(dot) - Match any single character (except a line break);
# \d - Digit(0-9);# \D - Not a Digit(0-9);
# \w - word character (a-z,A-Z,0-9,_);
# \W - not a word character;# \s - whitespace(space,tab,newline);
# \S - not a whitespace;;#\b - Word Boundary;#\B - not a boundary;
# ^ - Start of String;# $ End of String;;# [] - Match characters in brackets;
# [^] - Match character not in brackets;
# | Either or;# () Group;;# Quantifiers;
# * - 0 or more;# + - 1 or More;# ? - 0 or One;# {3} - Extact Number;
# {3,4} - Range of Numbers(Minimum,Maximum);;
# Charaters to escape;# .[{()\^$|?*+ """


def constant(f):
    def fset(self, value):
        raise TypeError

    def fget(self):
        return f()

    return property(fget, fset)


class _Grammar(object):
    @constant
    def return_grammar():
        return {
            "class": _learn_classes,
            "classes": _learn_classes,
            "function": _learn_function,
            "method": _learn_function,
            "methods": _learn_function,
            "functions": _learn_function,
            "context_manager": _learn_contextManager_as_function,
            "context manager": _learn_contextManager_as_function,
            "regular expression": learn_regex_patterns,
            "regular_expression": learn_regex_patterns,
            "regex": learn_regex_patterns,
            "threading": _learn_threading_basic,
            "thread": _learn_threading_basic,
        }


def learn(input, **kwargs):
    pattern = re.compile(
        r"(classe?s?|functions?|methods?|context_?\s?manager|regular\s?_?expression|regex|thread(ing)?)",
        re.IGNORECASE,
    )
    match = pattern.search(input)
    matchedInput = None

    GRAMMAR = _Grammar().return_grammar
    if match:
        matchedInput = match.group().lower()
    if matchedInput in GRAMMAR:
        _core_printer(GRAMMAR[matchedInput])
    else:
        print(
            "Sorry, learning word not found .Try calling function learn_list() to get a list of learning words "
        )


def learn_list():
    print(
        r"""class OR classes
function OR functions
method OR methods
context_manager OR context manager
regular_expression OR regular epxression OR regex"""
    )
