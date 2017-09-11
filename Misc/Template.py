#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from string import Template

def Main():
    cart = []
    cart.append(dict(item = "coke", price = 30, qty = 2))
    cart.append(dict(item = "maps", price = 15, qty = 5))
    cart.append(dict(item = "grocery", price = 400, qty = 7))

    print (cart)
    t = Template("$qty x $item = $price")
    total = 0
    print ("Cart: ")
    for data in cart:
        print (t.substitute(data))
        total += data["price"]
    print ("Total "+str(total))

if  __name__ == '__main__':
        Main()
