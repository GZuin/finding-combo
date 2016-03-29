// Definition of a move, a moveset and a inputset.

#include <iostream>
#include <ctime>
#include <cstdlib>
#include <vector>
#include <string>

using namespace std;

class Move{ //Single possible input action. A directional + attack
	
	public:
		Move(); 							//Creates a random move
		Move(char a, char b);				//Creates a prefixed move
		string toStr() {return (str_move);}	//Returns the move (string)
		char getMoveType() { return atk;}
	private:
		char dir;
		char atk;
		string str_move;
};

class Moveset{ //A set of moves (a possible combo)
	
	public:
		Moveset(unsigned int numMoves);							//Creates a random moveset with n moves
		Moveset(string s);										//Creates a prefixed moveset
		Move getMove(unsigned int pos) { return combo[pos];}	//Returns the 'pos' move in a moveset
		unsigned int getComboSize() { return combo.size();}		//Returns the size of the moveset
		void print();									//Prints on screen the moveset
	private:
		vector<Move> combo;
		
};

class InputSet{ //A list of possible inputs of a player

	public:	
		InputSet(Moveset ms, unsigned int weakDelay, unsigned int medDelay, unsigned int strgDelay);	//Creates a random imputset from a moveset
		string getInput() {return inputList;}
	private:
		string inputList;
};
