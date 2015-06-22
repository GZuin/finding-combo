import os
import sys

inputfile = sys.argv[1]
outprefix = 0


with open(inputfile) as f:
    for line in f:
        path = str(outprefix) + ".txt"
        print path
        output = open(path, 'w');
        output.write(line)
        output.close()
        outprefix = outprefix + 1
