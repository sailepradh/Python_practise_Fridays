#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def Main():
    line = "I think I understand regular expression"

    match_line = re.match ("think", line, re.M|re.I)

    if match_line:
        print ("Match found: "+match_line.group())
    else:
        print("No match found")

    search_line = re.search ("think", line, re.M|re.I)
    if search_line:
        print ("Search Found: "+search_line.group())
    else:
        print ("No search found")

if __name__ == "__main__":
    Main() 
