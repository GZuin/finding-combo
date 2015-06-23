import sys
import hmm_tables as table
import viterbi

states = ["Combo","Free"]
obs = []
obsarray = [["Combo"], ["Free"]]

finds = []
params = []


def iscombosize(vet,size):
    streak = 0
    maxstreak = 0
    for i in range(0, len(vet)):
        if(vet[i] == "Combo"):
            streak = streak + 1
            if (streak > maxstreak):
                maxstreak = streak
        else:
            streak = 0

    if(maxstreak >= size):
        return True
    else:
        return False


if __name__ == '__main__':
    inputsize = int(sys.argv[1])
    combosize = int(sys.argv[2])


    #Generate all possible entries
    n=0
    while(len(obsarray[-1])<inputsize+1):
        obs = obsarray[n]
        #print obs
        t1 = ["Combo"] + obs
        t2=  ["Free"] + obs
        obsarray.append(t1)
        obsarray.append(t2)
        n = n+1
    obsarray.pop()
    obsarray.pop()

    for n in range(0, len(obsarray)):
        if(iscombosize(obsarray[n],combosize)):
            viterbi.fill_observations(obsarray[n])
            finds.append(viterbi.example())
            params.append(obsarray[n])

    for i in range(0, len(finds)):
        for h in range (i, len(finds)):
            if(finds[h][0] > finds[i][0]):
                tempf = finds[i]
                tempp = params[i]

                finds[i] = finds[h]
                params[i] = finds[h]

                finds[h] = tempf
                params[h] = tempp

    outfile = sys.argv[3]
    output = open(outfile, 'w')


    #print finds[0]
    #print finds[0][1]
    #print finds[0][1][0]

    for i in range(0,10):
        print params[i]
        print finds[i]
        print ' '
        for k in range(0, len(finds[i][1])):
            output.write(finds[i][1][k])
            output.write(' ')
        output.write('\n')
    output.close()
    
