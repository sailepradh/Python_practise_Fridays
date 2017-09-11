#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import argparse

def Main():

    parser = argparse.ArgumentParser()
    parser.add_argument('word', help = "Search word in txt")
    parser.add_argument('file', help = "file where the word is searched")
    args = parser.parse_args()

    searchFile = open(args.file)
    linenum = 0

    for line in searchFile.readlines():
        line = line.strip("\r\n")
        linenum += 1
        searchstring = re.search(args.word, line , re.M|re.I)

        if searchstring:
            print (str(linenum)+': '+ line)


if __name__ == "__main__":
    Main()
