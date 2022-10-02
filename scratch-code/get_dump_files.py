#!/usr/bin/python

import sys
import os

f = open(sys.argv[1], 'r')
lines = f.readlines()
f.close()

for line in lines:
  if line.find("debug") != -1:
    line_list = line.split()
    filename =line_list[2]
    f = open(filename, 'r')
    flines = f.readlines()
    print (flines)
    f.close()

