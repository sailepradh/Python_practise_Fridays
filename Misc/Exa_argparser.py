#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import glob
import logging
import os
import random
import string
import subprocess

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return(a)

def Main():
    parser = argparse.ArgumentParser()
    groups = parser.add_mutually_exclusive_group()
    groups.add_argument("-v", "--verbose", action ="store_true")
    groups.add_argument("-q", "--quiet", action = "store_true")
    parser.add_argument("num", help = "The fibonacci number you wish to calculate", type = int)
    parser.add_argument("-o", "--output", help = "Outputs the result to some file", action = "store_true")

    args = parser.parse_args()
    result = fib(args.num)

    if args.verbose:
        print ("The "+str(args.num)+"the fibonaaci number is "+str(result))
    elif args.quiet:
        print(result)
    else:
        print ("Fib("+str(args.num)+") = "+str(result))

    if args.output:
        f = open ("fib.txt", "a")
        f.write (str(result)+"\n")

if __name__ == '__main__':
    Main()
