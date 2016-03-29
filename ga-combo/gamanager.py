import sys
import os
import random
import genpop as gp
import calcfitness as cf
import elitism as elit
import genoperands as go
import tournament as tour
import time

def shouldSmartMutate(fitbygen,waitgen):
    if(waitgen>len(fitbygen)):
       return False
    vet = list(fitbygen[::-1])
    equal=0
    for i in range(0, len(fitbygen)-1):
        if (vet[i] == vet[i+1]):
            equal=equal+1
        else:
            return False
        if(equal>=waitgen):
            return True
    

def gaManager(experimentPath, seed, numGen, popSize, indSize, numElit, numRegen,
	      tourSize, mutationProb, crossProb, maxMutations, repetitions,
              segsize,waitgen, popmode):

    stime = time.time()
	
    #lastrep=0
	#Find last evaluated generation
    #for lastrep in range(0,repetitions):
		#if(not os.path.exists(experimentPath + "/rep" + str(lastrep+1))): 
		#	break
		
    for rep in range(0, repetitions):
        random.seed(seed+rep)
        path = experimentPath + "/rep" + str(rep+1) + "/" + experimentPath + "_gen"
        sys.stdout.write("\r................................................")
        sys.stdout.write("\rEvaluating " + experimentPath + " rep " + str(rep))
        #Generate Initial Population
        if popmode:
            gp.premadegenPopulation(path+"0",popSize, indSize)
        else:
            gp.genPopulation(path+"0",popSize, indSize)
        #Repeat for a number of generations
        fitbygen = []
        for i in range(0, numGen):
            sys.stdout.write("\rEvaluating " + experimentPath + " repetition " + str(rep) +
                            " generation " + str(i+1))

            #If it exists, this generatios was already evaluated and the next one created, The program most lilely crashed
            if(os.path.exists(path+str(i+2))): 
                continue
            
            #Evaluate Population
            cf.calcFit(path+str(i), 'Game')
            fitbygen.append(open(os.path.join(path+str(i),'0.fit'),'r').read())
            #Carryover to next generation the best individuals    
            best = elit.nextGen(path, i, numElit)
            k = numElit #size of next generation population
            if (segsize>0 and shouldSmartMutate(fitbygen,waitgen)):
                go.smartmutation(best,path,'Game',i,segsize,k)
                k = k+2
			
	    #Insert random individuals back into population
            gp.regnextGen(path, i+1, k,numRegen, indSize)
            #cf.calcFit(path+str(i+1), 'Game')
            k = k + numRegen #size of next generation population
			
            while k<popSize:
                #Select good invidual in current population
                father1 = tour.tournament(path+str(i),tourSize, popSize)
                father2 = tour.tournament(path+str(i),tourSize, popSize)
                            
                #Generate new individuals through crossover and mutation
                #and evaluate them
                go.reproduce(father1, father2, path, i, k, indSize, mutationProb, crossProb, maxMutations)
                k=k+2
		#lastgen=0 #sets last evaluated generation to be 0 again
        
    sys.stdout.write("\r................................................")
    sys.stdout.write("\rExperiment " + experimentPath + " done!")
    sys.stdout.write("\n Elapsed time: " + str(time.time() - stime))
    o = open(os.path.join(experimentPath,'param.txt'),'w')
    o.write(experimentPath + ' ' + str(seed) + ' ' + str(numGen) + ' ' + str(popSize) + ' ' + str(indSize) + ' ' + 
			str(numElit) + ' ' + str(numRegen) + ' ' + str(tourSize) + ' ' + str(mutationProb) + ' ' + str(crossProb) + ' ' + 
			str(maxMutations) + ' ' + str(repetitions) + "\n Elapsed time: " + str(time.time() - stime))
    o.close()

if __name__=="__main__":
    experimentPath = sys.argv[1]
    seed = int(sys.argv[2])                 #random seed
    numGen = int(sys.argv[3])               #number of generations
    numInd = int(sys.argv[4])               #size of population
    sizInd = int(sys.argv[5])               #size of each individual
    numElit = int(sys.argv[6])              #how many individuals are preserved (elitism)
    numRegen = int(sys.argv[7])             #how many individuals are generated randomly in each gen
    tourSize = int(sys.argv[8])             #size of tournament
    
    mutationProb = float(sys.argv[9])       #mutation probability
    crossProb = float(sys.argv[10])         #crossover probability
    maxMutations = int(sys.argv[11])        #max genes mutaded

    repetitions = int(sys.argv[12])         #repetitions of each experiment

    if(len(sys.argv)>13):
        segsize = int(sys.argv[13])             #size of segment used for smartmutation
        waitgen = int(sys.argv[14])             #number of generations to w8 b4 using smartmutation
    else:
        segsize = 0
        waitgen = 0


    if(len(sys.argv)>14):
        popmode = sys.argv[14]
    else:
        popmode = 0

    
    gaManager(experimentPath, seed, numGen, numInd, sizInd, numElit, numRegen,
              tourSize, mutationProb, crossProb, maxMutations, repetitions,
              segsize, waitgen, popmode)
    
