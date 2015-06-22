import os
import sys
import random

array = ["1l", "1m", "1h","1-",
         "2l", "2m", "2h","2-",
         "3l", "3m", "3h","3-",
         "4l", "4m", "4h","4-",
         "5l", "5m", "5h","5-",
         "6l", "6m", "6h","6-",
         "7l", "7m", "7h","7-",
         "8l", "8m", "8h","8-",
         "9l", "9m", "9h","9-"]

endinputs = sys.argv[1]
outfile = sys.argv[2]
word=""

output = open(outfile, 'w')

for i in range (0, int(endinputs)):
    inputfile = str(i) + ".txt"
    with open(inputfile) as f:
        for line in f:
            for char in line:
                if(char != '\n' and char!=' '):
                    word = word + char
                else:
                    if(word=="--"):
                        word = array[random.randint(0,35)]    
                    output.write(word + ' ')
                    word=""
    output.write('\n')
output.close()
           
