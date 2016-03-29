import os
import sys

inputfile = sys.argv[1]
outputfile = sys.argv[2]
outprefix = 0

out = open(outputfile, 'w')

with open(inputfile) as f:
    for line in f:
        i = 0;
        for char in line:
            i=i+1
            if (i==15):
                out.write("5- 5- 5- 5- 5- ")
            if (i>15):
                out.write(char)
out.close()
