#!/usr/bin/env python3

import sys

def calc(a, op, b):
    if op == "+":
        return a+b
    elif op == "-":
        return a-b
    elif op == "*":
        return a*b
    elif  op == "/":
        return a /b
    else:
        return "Error"


args = sys.argv[1:]
# print(args)
# args= args[1:]
zahl1=float(args[0])
op = args[1]
zahl2=float(args[2])
print(calc(zahl1, op, zahl2))