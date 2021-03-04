"""Read and write from files with python.

Methods:
    .read/write(file.name, mode='w|rt|b', encoding)
    .readline/writeline(must specify newlines)
    .seek(move to beginning with 0)

Files are iterable objects when opened. Iterated by newlines.
"""

import sys

f = open(sys.argv[1], mode='rt', encoding='utf-8')

for line in f:
    # print(line) Adds extra newlines from what's in the file
    sys.stdout.write(line)
f.close()
