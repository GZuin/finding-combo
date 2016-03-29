import random
#import gentree as gt
import os


moves  = [
        '1l', '1m', '1h', '1-',
        '2l', '2m', '2h', '2-',
        '3l', '3m', '3h', '3-',
        '4l', '4m', '4h', '4-',
        '5l', '5m', '5h', '5-',
        '6l', '6m', '6h', '6-',
        '7l', '7m', '7h', '7-',
        '8l', '8m', '8h', '8-',
        '9l', '9m', '9h', '9-'
        ]

def regnextGen(basepath, gennum, startindex,regval, indsize):
    path = basepath + str(gennum)
    for index in range(startindex,regval+startindex):
        ofile = open(path + "/" + str(index)+".ind",'w')
        for i in range (0,indsize):
            if(i<3):
                ofile.write('5- ')
            else:
                ofile.write(random.choice(moves))
                ofile.write(' ')
        ofile.close()
        index = index + 1

		
def genPopulation(path,popsize,indsize):
    if(not os.path.exists(path)):
        os.makedirs(path)

    for index in range(0,popsize):
        ofile = open(path + "/" + str(index)+".ind",'w')
        for i in range (0,indsize):
            if(i<3):
                ofile.write('5- ')
            else:
                ofile.write(random.choice(moves))
                ofile.write(' ')
        ofile.close()
        index = index + 1
    

def premadegenPopulation(path, popsize, indsize):
    print "\rPopulation generated from premade combos"
    if(not os.path.exists(path)):
        os.makedirs(path)

    for index in range(0,popsize):
        s = []
        while len(s)<indsize:
            r = random.randint(0,45)
            s.extend(open('premade//'+str(r)+'.txt','r').read().split())
        ofile = open(path + "/" + str(index)+".ind",'w')
        for i in range(0,len(s)):
            if(i<indsize):
                ofile.write(s[i]+' ')
            else:
                break
        ofile.close()
        index = index + 1

if __name__ == "__main__":
    genPopulation("test",3,30)
