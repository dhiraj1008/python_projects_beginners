"""
# format method (builtin method)
    ->adds specified argument in the placeholders
   str = "{} how are {}".format("dhiraj","how")
       or 
   str = "{name} how are {pronoun}".format(name="dhiraj",pronoun="how")
       or 
  str = "{1} how are {2}".format("dhiraj","how") # by using number
# time is the library in python for time related concepts
a, b = divmod(7, 3)  # Return the tuple (x//y, x%y). Invariant: div*y + mod == x.
print(a, b)
"""
"""
:d ->formate specifiers for integer
"""
"""
str = "{:02d} : {:02d}".format(2, 3)
print(str)
print(70 // 60, 70 % 60)  # technique to format output like stopwatch
"""
import time as td


def countdown(t):
    while t:
        min, sec = divmod(t, 60)
        timer = "{:02d}:{:02d} ".format(min, sec)
        print("\r" + timer, end="")
        td.sleep(1)
        t -= 11
    print("\nyour time start know")


time = input("enter the time ")
countdown(int(time))
