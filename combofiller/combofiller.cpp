#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <ctime>
#include "_combodef.h"

using namespace std;


string run(Moveset *ms, int _weakDelay, int _medDelay, int _strgDelay, unsigned int _numInputs);
// Generates a file with multiple possible inputs of a player for a given combo

int main(int argc, char** argv) {
	srand(time(NULL));
	if(argc==4)	{
        unsigned int _numInputs = atoi(argv[1]);
        unsigned int _comboSize = atoi(argv[2]);
		string outFile = argv[3];
        ofstream output(outFile.c_str(), ofstream::out);

        for(unsigned int i=0; i<_numInputs; i++) {
            Moveset *ms;
            ms = new Moveset (_comboSize);
            for(unsigned int i=0; i<ms->getComboSize(); i++)
                output << ms->getMove(i).toStr() << " ";
            delete ms;
            output << "\n";
        }
	    output.close();
	    return 0;
	}
	else if(argc<8) {
		cout << "Incorrect number of arguments (presented " << argc << ")\n<wkDelay> <mdDelay> <stgDelay> <numInputs> <outFile> -size|-custom <comboSize | customCombo>\n";
		exit(-1);
	}

	int _weakDelay = atoi(argv[1]);
	int _medDelay =  atoi(argv[2]);
	int _strgDelay = atoi(argv[3]);
	unsigned int _numInputs = atoi(argv[4]);
	string outFile = argv[5];
    ofstream output(outFile.c_str(), ofstream::out);
	string mode = argv[6];


	if(mode=="-custom") //if a custom combo is being inserted
	{	string customMove = argv[7];
		Moveset *ms;
		ms = new Moveset(customMove);
		ms->print();
		output << run(ms,_weakDelay,_medDelay,_strgDelay, _numInputs);
		delete ms;
	}
	else //if program should create a random combo
	{	int _comboSize = atoi(argv[7]);
		Moveset *ms;
		ms = new Moveset(_comboSize);
		ms->print();
		output << run(ms,_weakDelay,_medDelay,_strgDelay, _numInputs);
		delete ms;
	}
    output.close();
	return 0;
}

string run(Moveset *ms, int _weakDelay, int _medDelay, int _strgDelay, unsigned int _numInputs)
{
	string output="";

	for(unsigned int i=1; i<=_numInputs; i++) { //Multiple possible inputs for the same combo
		InputSet is(*ms,_weakDelay,_medDelay, _strgDelay);
		output += is.getInput();
		if(i!=_numInputs) //if its not the last input possibility
			output += '\n';
	}
	return(output);
}
