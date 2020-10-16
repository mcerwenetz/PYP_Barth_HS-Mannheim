#!/usr/bin/env python3

import sys

def calc(a, op, b):
    zahl1 = float(a)
    zahl2 = float(b)
    if op == "+":
        return zahl1+zahl2
    elif op == "-":
        return zahl1-zahl2
    elif op == "*":
        return zahl1*zahl2
    elif  op == "/":
        return zahl1 /zahl2
    else:
        return "Error"
