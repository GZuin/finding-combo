import os
import sys


endinputs = sys.argv[1]
outfile = sys.argv[2]

output = open(outfile, 'w')

for i in range (0, int(endinputs)):
    inputfile = str(i) + ".txt"
    with open(inputfile) as f:
        for char in f:
            if(char != '\n'):
                output.write(char)
    output.write('\n')
output.close()
           
