import random

def tournament(path, tournamentSize, popSize):
	fit = -1.0
	best = None
	for i in range(0, tournamentSize):
		index = str(random.randint(0, popSize-1))
		inp = open(path + "/" + index + ".fit")
		temp = float(inp.read())
		inp.close()
		if (fit > 0):
			if (temp > fit):
				fit = temp
				best = index
		else:
			fit = temp
			best = index
	return best+".ind"


if __name__=="__main__":
	print (tournament("test", 4,4))
