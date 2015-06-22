#include "_combodef.h"

//Combo grammar. 9 directionals and 3 types of attack
static char grammar[11] = {'1','2','3','4','5','6','8','-','l','m','h'};


Move::Move() { //Move creator. A random directional and a random attack
	dir = grammar[rand()%7];
	atk = grammar[rand()%4+7];

	str_move.push_back(dir);
	str_move.push_back(atk);
}

Move::Move(char a, char b) { //Move creator. A specific directional and a specific attack
	dir = a;
	atk = b;

	str_move.push_back(dir);
	str_move.push_back(atk);
}

Moveset::Moveset(unsigned int numMoves) { //Moveset creator. Contains 'numMoves' random moves
	for (unsigned int i=0; i<numMoves; i++)
	{	Move m;
		combo.push_back(m);
	}
}

Moveset::Moveset(string s) { //Moveset creator. Contains specific moves

	for (unsigned int i=0; i<s.size(); i+=2)
	{	Move m(s[i], s[i+1]);
		combo.push_back(m);
	}
}

void Moveset::print() { //Prints the moveset for easy debug
	for (unsigned int i=0; i< combo.size(); i++) {
		cout << combo[i].toStr() << " ";
	}
	cout << "\n";
}

InputSet::InputSet(Moveset ms, unsigned int weakDelay, unsigned int medDelay, unsigned int strgDelay) {
	//Fills the inputs between each move in a combo to suit the number of frames between each move

	inputList = "";
	for(unsigned int i=0; i<ms.getComboSize(); i++) {
		inputList += ms.getMove(i).toStr() + " ";
		int delay=0;

		switch(ms.getMove(i).getMoveType()) {
			case 'l':
				delay = weakDelay;
				break;
			case 'm':
				delay = medDelay;
				break;
			case 'h':
				delay = strgDelay;
				break;
		}


		for(unsigned int i=0; i<delay; i++){
			Move m_temp;
			inputList+=m_temp.toStr() + " ";
		}
	}
}
