#! /usr/bin/env python3

import argparse
from basicds.linkedlist import linkedlist
from collections_intro import *
from lambdas import *
import sys

"""
Argument specifiers:

%s - String (or any object with a string representation, like numbers)

%d - Integers

%f - Floating point numbers

%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

%x/%X - Integers in hex representation (lowercase/uppercase)

"""


def get_args():
    parser = argparse.ArgumentParser(
        description="A simple argument parser",
        epilog="-h for help"
    )

    parser.add_argument('-x', action="store", required=True,
                        help='Help text for option x')
    parser.add_argument('-y', action="store", default=False,
                        help='Help text for option y')
    args = parser.parse_args()
    print("passed argument is ", args.x)


def main():
    # get_args()
    astring = "Hello World people"
    print(">>> refcount is ", sys.getrefcount(astring))

    print(astring)
    print(astring[::-1])
    print(astring.startswith("Hel"))
    print(astring.endswith("ld"))
    print(astring.upper())

    mylist = [1, 2, 3]
    print("list is %s" % mylist)

    for x in range(5):
        print(x)
    for x in range(3, 6):
        print(x)
    for x in range(3, 7, 2):
        print(x)
    else:  # else clause for false condition in loops
        print("x value exceeds boundary 6")

    # insert in linked list
    ll = linkedlist.New()
    ll.push_front(10)
    ll.push_front(20)
    ll.push_front(30)
    ll.push_front(40)
    print(ll)

    run_lambdas()
    check_collections()

if __name__ == "__main__":
    main()
