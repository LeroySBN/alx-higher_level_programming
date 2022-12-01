#!/usr/bin/python3
from sys import argv

argc = len(argv) - 1

if argc == 0:
    print("{0} arguments.".format(argc))
else:
    if argc > 1:
        print("{0} arguments:".format(argc))
    elif argc == 1:
        print("{0} argument:".format(argc))
    for i in range(argc):
        print("{0}: {1}".format(i + 1, argv[i + 1]))
