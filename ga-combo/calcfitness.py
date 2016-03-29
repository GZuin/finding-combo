#import evaluate as ev
import os
import subprocess
import shutil
import time
import re
import math


def calcFit(path, gamepath):
    vet = os.listdir(path)
    #print os.path.splitext(vet[0])
    index = 0
    for i in range(0, len(vet)):
        if(os.path.splitext(vet[i])[1] != ".ind"):
            continue
        if(os.path.exists(path + "/" + os.path.splitext(vet[i])[0] + ".fit")):
            continue
        inp = path + "/" + vet[i]
        out = open(path + "/" + os.path.splitext(vet[i])[0] + ".fit", 'w')

        lionpath = gamepath
        shutil.copyfile(inp, os.path.join(lionpath, '0.txt'))
        #print "copy to input"
        #time.sleep(5)
        lock = os.path.join(lionpath, 'inputlock.txt')
        unlock = os.path.join(lionpath, 'outputlock.txt')

        open(lock, 'a').close()
        done=0
        while(done==0):
            try:
                if(os.path.exists(unlock)):
                   os.remove(unlock)
                done=1
            except:
			    done=0
            #print "Delete unlock"
        #open(lock, 'a').close()


        
        #print "Create lockfile"
        #Wait for outputlock.txt file
        while(not os.path.exists(unlock)):
            time.sleep(0.05)
        #print "Recieved unlock"

        #time.sleep(0.5)

        fgpath = os.path.join(lionpath, 'fg_output.txt')
        fg = open(fgpath)
        #print "Opened fg_output"



        h2 = [m.group(0) for m in re.finditer(r"(\d)\1*", fg.read())]

        bigger=0
        for i in range(0,len(h2)):
            if(len(h2[i]) > len(h2[bigger]) and h2[i][0]=='1'):
               bigger = i

        ffit = 0.0
        for i in range(0,len(h2)):
            if(i==bigger and h2[i][0]=='1'):
                ffit+=len(h2[i])
            elif(i<bigger and h2[i][0]=='1'):
                ffit+= len(h2[i]) / math.pow(1+len(h2[i+1]),2) 
            elif(i>bigger and h2[i][0]=='1'):
                ffit+= len(h2[i]) / math.pow(1+len(h2[i-1]),2)

        fg.close()
        out.write(str(int(ffit*10000)))
        out.close()
        #shutil.copyfile(fgpath, os.path.join(path, str(index) + '.out'))

        os.remove(os.path.join(lionpath, '0.txt'))
        #print "Delete 0.txt"

        #os.remove(fgpath)
        index = index + 1


        #print("Simulation Ended")

        #out.write(str(err))
        #out.close()

if __name__ == "__main__":
    calcFit("test","Game")
