import os
import sys
#from itertools import zip

combofile = sys.argv[1]
statefile = sys.argv[2]

outcombofile = sys.argv[3]
outstatefile = sys.argv[4]


combos = open (combofile)
states = open (statefile)
outcombos = open (outcombofile, 'w')
outstates = open (outstatefile, 'w')


for linecombo, linestate in zip(combos, states):
    statearray = []
    comboarray = []
    word = ""
    for char in linestate:
        if(char!=' ' and char !='\n'):
            statearray.append(char)
    for char in linecombo:
        if (char==' ' or char == '\n'):
            if(len(word)==2):
                comboarray.append(word)
            word=""
        else:
            word+=char
    statedif = len(statearray) - len(comboarray)
    combodif = len(comboarray) - len(statearray)

    if(statedif>0):
        for i in range(0,statedif):
            statearray.pop()
    if(combodif>0):
        for i in range(0,combodif):
            comboarray.pop()
    for i in range(0, len(statearray)):
        outcombos.write(comboarray[i])
        outcombos.write(' ')
        outstates.write(statearray[i])
    outcombos.write('\n')
    outstates.write('\n')

        
