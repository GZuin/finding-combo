import os
import shutil
import time

#def fitnessDiretctory(path
#path="test"
#vet = os.listdir(path)
#print os.path.splitext(vet[0])

#for i in range(0, len(vet)):
#    inp = open(path + "/" + vet[i])
#    out = open(path + "/" + os.path.splitext(vet[i])[0] + ".fit", 'w')
#    ev.evalTree(inp,out,1,50)
#    inp.close()
#    out.close()

def bubble_sort(vetfiles, vetfitns):
    for i in range(0,len(vetfitns)):
        for j in range(0,len(vetfitns)-1-i):
            if vetfitns[j] < vetfitns[j+1]:
                vetfitns[j], vetfitns[j+1] = vetfitns[j+1], vetfitns[j]
                vetfiles[j], vetfiles[j+1] = vetfiles[j+1], vetfiles[j]   


def nextGen(basepath, gennum, elitval):
	path = basepath + str(gennum)
	files = os.listdir(path)
	total = 0.0
	vetfiles = []
	vetfitns = []
	for i in range (0, len(files)):
		if(os.path.splitext(files[i])[1]==".fit"):
			vetfiles.append(os.path.splitext(files[i])[0])
			inp = open(basepath + str(gennum) + "/" + files[i])
			vetfitns.append(float(inp.read()))
			total = total + vetfitns[len(vetfitns)-1]
			inp.close()
			
	bubble_sort(vetfiles, vetfitns)
	if(os.path.exists(basepath + str(gennum+1))):
		shutil.rmtree(basepath + str(gennum+1), ignore_errors=True)
    #time.sleep(1)
	os.makedirs(basepath + str(gennum+1))        
	for j in range(0,elitval):
		shutil.copyfile(basepath + str(gennum) + "/" + vetfiles[j]+".ind", basepath + str(gennum+1) + "/" + str(j)+".ind")
		shutil.copyfile(basepath + str(gennum) + "/" + vetfiles[j]+".fit", basepath + str(gennum+1) + "/" + str(j)+".fit")
		#shutil.copyfile(basepath + str(gennum) + "/" + vetfiles[j]+".out", basepath + str(gennum+1) + "/" + str(j)+".out")
	shutil.copyfile(basepath + str(gennum) + "/" + vetfiles[0]+".fit", basepath + str(gennum) + "/_bestfitness.txt")
	shutil.copyfile(basepath + str(gennum) + "/" + vetfiles[len(vetfiles)-1]+".fit", basepath + str(gennum) + "/_lastfitness.txt")
	total = total / len(vetfiles)
	out = open(basepath + str(gennum) + "/_medfitness.txt",'w')
	out.write(str(total))
	out.close()
	return vetfiles[0]
    


if __name__ == "__main__":
    nextGen("test",1,2)

