import os
import sys
import random

array = ["1-","2-","3-","4-","5-","6-","7-","8-","9-"]

endinputs = sys.argv[1]
outfile = sys.argv[2]
word=""

output = open(outfile, 'w')

for i in range (0, int(endinputs)):
    inputfile = "preset_combos\\" + str(i) + ".txt"
    with open(inputfile) as f:
        for line in f:
            for char in line:
                word = word + char
                if(word=="--"):
                    word = array[random.randint(0,8)] 
                if(char=='\n' or char==' '):
                    output.write(word)
                    word=""
    word=""
    output.write('\n')
output.close()
           
