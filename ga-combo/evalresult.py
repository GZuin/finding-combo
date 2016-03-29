import os
import sys
import math

if __name__=="__main__":
        exp = sys.argv[1]
        inp = sys.argv[2]
        numRep = int(sys.argv[3])
        numGen = int(sys.argv[4])
        print ("Evaluating " + inp + " of " + exp)

        matrix = [[0 for x in range(numRep)] for x in range(numGen)] 
        med=[0.0]*numGen
        variance =[0.0]*numGen

        for r in range(0,numRep):
                #ofile = open("results/"+exp+"_rep"+str(r+1)+inp,'w')
                for g in range(0, numGen):
                        ifile = open(exp+"/rep"+str(r+1)+"/"+exp+"_gen"+str(g)+"/"+inp)
                        temp = ifile.read()
                        matrix[g][r]=float(temp)
                        med[g]=med[g]+float(temp)
                        #ofile.write(temp+"\t")
                        ifile.close()
                #ofile.close()


        for m in range(0,len(med)):
                med[m]=med[m]/numRep
        for r in range(0,numRep):
                for g in range(0,numGen):
                        temp = matrix[g][r] - med[g]
                        temp = temp*temp
                        variance[g] = variance[g]+temp

        out = open("results/"+exp+"_stdvar"+inp,'w')
        for v in range(0,len(variance)):
                variance[v] = math.sqrt(variance[v]/max(1,(numRep-1)))
                out.write(str(variance[v])+"\t")
        out.close()

        outmed = open("results/"+exp+"_med"+inp,'w')
        for m in range(0,len(med)):
                outmed.write(str(med[m])+"\t")
        outmed.close()
        


        
