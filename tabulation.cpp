#include <iostream>
#include <vector>
#include <set>
#include <bitset>
#include <algorithm>

using namespace std;

class Util{
	/*
	A class that contains utility functions required in the program.
	*/
public:
	string intToBinString(int size, int val){
		string bin;
		bin = bitset<100>(val).to_string();
		bin = bin.substr(100-size);
		return bin;
	}

	int get1s(string x) {
		// returns the number of 1s in a binary string
		int count = 0;
		for (int i = 0; i < x.size(); ++i){
			if (x[i] == '1')
				count++;
		}
		return count;
	}

	bool compare(string a, string b) {
		// checks if two string differ at exactly one location or not
		int count = 0;
		for(int i = 0; i < a.length(); i++) {
			if (a[i]!=b[i])
				count++;
		}

		if(count == 1)
			return true;

		return false;
	}

	string getDiff(string a, string b) {
		// returs a string that replaces the differ location of two strings with '-'
		for(int i = 0; i < a.length(); i++) {
			if (a[i]!=b[i])
				a[i]='-';
		}

		return a;
	}

	bool checkEmpty(vector< vector< string> > table){
		for (int i = 0; i < table.size(); ++i){
			if (table[i].size()!=0) {
				return false;
			}
		}
		return true;
	}

	string binToString(string x){
		// converts binary string to alphabetic variables
		string out = "";
		for (int i = 0; i < x.size(); ++i){
			if (x[i]=='1') {
				char x = 97 + i;
				out += x;
			}
			else if (x[i]=='0') {
				char x = 97 + i;
				out += x;
				out += "'";
			}
		}
		return out;
	}

	bool primeIncludes(string imp, string minTerm){
		// check is a prime implicant satisfies a min term or not
		for (int i = 0; i < imp.size(); ++i){
			if (imp[i]!='-'){
				if(imp[i]!=minTerm[i]){
					return false;
				}
			}
		}
		return true;
	}

	int getVar(set<int> comb, vector<string> primeImp){
		// returns the number of variables in a petrick method combination
		int count = 0;
		set<int> :: iterator itr;
		for (itr = comb.begin(); itr != comb.end(); ++itr){
			int imp = *itr;
			for (int i = 0; i < primeImp[imp].size(); ++i){
				if (primeImp[imp][i]!='-')
					count ++;
			}
		}
		return count;

	}

};

class Tabulation{
private:
	Util util;
	vector< int > minInt; // min terms in decimal
 	vector< string > minBin; // min terms in binary
 	int nBits;
 	int nMin;  // no of variables
 	vector< vector< string> > table; 
 	vector< string > primeImp;
 	vector< set<int> > functions;
 	
 

public:
	void initialise() {
		cout << "Enter number of bits/variables:" << endl;
		cin >> nBits;

		cout << "Enter number of min terms:" << endl;
		cin >> nMin;

		cout << "Enter min terms:" << endl;
		for (int i = 0; i < nMin; ++i){
			int x;
			cin >> x;
			minInt.push_back(x);
			minBin.push_back(util.intToBinString(nBits, x));
		}

		cout << "\nBinary representation of provided min terms:" << endl;
		for (int i = 0; i < nMin; ++i){
			cout << i << ") " << minBin[i] << endl;
		}

		table = vector< vector< string> >(nBits+1);
	}

	void setPrimeImp() {
		set< string > primeImpTemp;
		createTable();
		cout << "\nGetting Prime Implicants.." << endl;

		// Combine consecutive terms in the table until its empty
		while (!util.checkEmpty(table)){
			table = combinePairs(table, primeImpTemp);
		}
		
		set<string > :: iterator itr;  // convert set to vector
		 for (itr = primeImpTemp.begin(); itr != primeImpTemp.end(); ++itr){
		 	string x = *itr;
        	primeImp.push_back(x);
    	}

    	cout << "\nThe Prime Implicants are:" << endl;
    	for (int i = 0; i < primeImp.size(); ++i){
    		cout  << i << ") "<< util.binToString(primeImp[i]) << endl;
    	}

	}

	void minimise() {
		// prepare primeImp chart
		bool primeImpChart[primeImp.size()][nMin] = {{false}};

		for (int i = 0; i < primeImp.size(); ++i){
			for (int j = 0; j < nMin; ++j){
				primeImpChart[i][j] = util.primeIncludes(primeImp[i], minBin[j]);
			}
		}

		cout << "\nPrime implicants chart (rows: prime implicant no., col: minterm no.):" << endl;
		for (int i = 0; i < primeImp.size(); ++i){
			for (int j = 0; j < nMin; ++j){
		 		if (primeImpChart[i][j] == true){
		 			cout << "1\t";
		 		}
		 		else {
		 			cout << "0\t";
		 		}
		 	}
		 	cout << endl;
		}

		// petric logic
		vector< set<int> > patLogic;
		for (int j = 0; j < nMin; ++j){ // column iteration
			set<int> x;
			for (int i = 0; i < primeImp.size(); ++i){ // row iteration
				if (primeImpChart[i][j] == true) {
					x.insert(i);
				}
			}
			patLogic.push_back(x);
		}
		cout << "\nPetric logic is (row: minterms no., col: prime implicants no.): " << endl;
		for (int i = 0; i < patLogic.size(); ++i){
			set<int > :: iterator itr;  // convert set to vector
			for (itr = patLogic[i].begin(); itr != patLogic[i].end(); ++itr){
				int x = *itr;
	        	cout << x << " ";
	    	}
	    	cout << endl;
		}

		// get all possible combinations
		set< set<int> > posComb;
		set<int> prod;
		getPosComb(patLogic, 0, prod, posComb); // recursively multiply set elements
		int min = 9999;

		cout << "\nPossible combinations that satisfy all minterms:" << endl;
		set< set<int> > :: iterator itr1;
		for (itr1 = posComb.begin(); itr1 != posComb.end(); ++itr1){
			set<int> comb = *itr1;
			if (comb.size() < min){
				min = comb.size();
			}
			set<int > :: iterator itr;  
			for (itr = comb.begin(); itr != comb.end(); ++itr){
				int x = *itr;
	        	cout << x << " ";
	    	}
	    	cout << endl;
		}

		cout << "\nGetting the combinations with min terms and min variables ..." << endl;
		//Combinations with minimum terms
		vector< set<int> > minComb;
		set< set<int> > :: iterator itr;
		for (itr = posComb.begin(); itr != posComb.end(); ++itr){
			set<int> comb = *itr;
			if (comb.size() == min) {
				minComb.push_back(comb);
			}
		}

		//Combinations with minimum variables
		min = 9999;
		for (int i = 0; i < minComb.size(); ++i){
			if(util.getVar(minComb[i], primeImp) < min){
				min = util.getVar(minComb[i], primeImp);
			}
		}

		for (int i = 0; i < minComb.size(); ++i){
			if(util.getVar(minComb[i], primeImp) == min){
				functions.push_back(minComb[i]);
			}
		}
	}

	void displayFunctions() {
		// prints output
		cout << "\n\nThe possible functions are-\n" << endl;
		for (int i = 0; i < functions.size(); ++i){
			set<int> function = functions[i]; 
			set<int> :: iterator itr;
			cout << "Function " << i+1 << ":"<< endl;
			for (itr = function.begin(); itr != function.end(); ++itr){
				int x = *itr;
				cout << util.binToString(primeImp[x]) << " + ";
			}
			cout << "\b\b  \n" << endl;
		}
	}

	void getPosComb(vector< set<int> > &patLogic, int level, set<int> prod, set< set<int> > &posComb) {
		// a recursive function to multiple elements of set patLogic and store it in set posComb
		if (level == patLogic.size()){
			set<int> x = prod;
			posComb.insert(x);
			return;
		}
		else{
			set<int > :: iterator itr;  
			for (itr = patLogic[level].begin(); itr != patLogic[level].end(); ++itr){

				int x = *itr;
	        	bool inserted = prod.insert(x).second;
	        	getPosComb(patLogic, level+1, prod, posComb);
	        	if (inserted){
	        		prod.erase(x);
	        	}
	    	}
		}
	}

	vector< vector< string> > combinePairs(vector< vector< string> > table, set<string>& primeImpTemp) {
		bool checked[table.size()][nMin] = {false};
		vector< vector< string> > newTable(table.size()-1);


		for (int i = 0; i < table.size() -1; ++i){
			for (int j = 0; j < table[i].size(); ++j){
				for (int k = 0; k < table[i+1].size(); k++){
					if (util.compare(table[i][j], table[i+1][k])){
						newTable[i].push_back(util.getDiff(table[i][j], table[i+1][k]));
						checked[i][j] = true;
						checked[i+1][k] = true;
					}
				}
			}
		}

		for (int i = 0; i < table.size(); ++i){
			for (int j = 0; j < table[i].size(); ++j){
				if (!checked[i][j]) {
					primeImpTemp.insert(table[i][j]);
				}
			}
		}

		return newTable;
	}

	void createTable() {
		for (int i = 0; i < nMin; ++i){
			int num1s = util.get1s(minBin[i]);
			table[num1s].push_back(minBin[i]);
		}
		
		cout << "\nTable:" << endl;
		for (int i = 0; i < nBits+1; ++i){
			cout << i << ")  ";
			for (int j = 0; j < table[i].size(); ++j){
				cout << table[i][j] << ", ";
			}
			cout << endl;
		}
	}

};

int main()  {
	Tabulation tab;
	tab.initialise();
	tab.setPrimeImp();
	tab.minimise();
	tab.displayFunctions();
	return 0;
}