from __future__ import print_function
from stack import Stack

def convert(dec):
    s = Stack()
    while dec > 1 :
        quo = dec // 2
        rem = dec % 2
        s.push(rem)
        dec = quo

    s.push(dec)

    while not s.isEmpty():
        print(s.pop(), end="")


convert(233)
