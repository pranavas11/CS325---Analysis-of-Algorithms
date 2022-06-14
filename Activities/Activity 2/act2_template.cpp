/******************************************************************************
CS 325 Activity 2
*******************************************************************************/

#include <iostream>
using namespace std;

int main() {
   int A[1000];  	// array of elements <= 1000
   int num;		// number of elements in the array
	int mode;
	int mfreq;
   
   cin >> num;		// read in number of elements
	cin >> A[0];	// the list will have at least one element
   
   for (int j = 1; j < num; j++) cin >> A[j];
	
   // add your code
	
	// the mode and frequency
	cout << mode << " " << mfreq;
   
   return 1;
}