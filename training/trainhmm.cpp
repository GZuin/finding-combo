#include <fstream>
#include <iostream>
#include <cstdlib>
using namespace std;

#include "hmm.h"

int main(int argc, char* argv[])
{
  Hmm hmm;
  if (argc<3) {
    cerr << "USAGE: trainhmm INIT-HMM RESULT-HMM DATA [MAX-ITERATIONS]" << endl;
    exit(1);
  }

  const char* output = argv[1];
  ifstream sstrm(argv[2]);
  ifstream istrm(argv[3]);
  int maxIterations = 10;
  if (argc>4)
    maxIterations = atoi(argv[4]);

  vector<vector<unsigned long>*> trainingSequences;
  vector<vector<unsigned long>*> trainingStates;

  hmm.readSeqs(istrm, trainingSequences);
  hmm.readSeqs(sstrm, trainingStates);

  hmm.supervisedLearning(trainingSequences, trainingStates);
  //hmm.saveProbs(output);
}

