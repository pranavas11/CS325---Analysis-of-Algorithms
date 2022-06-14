/******************************************************************************
CS 325 Activity 7: Babyface & Heels

Sample Test Case
Input:
4       
4
1 2
1 3
4 2
4 3
Output: Possible
*******************************************************************************/

#include <iostream>
#include <fstream>
#include <queue>
using namespace std;

int G[100][100];        // if you want to use an adjacency matrix

bool babyfaceHeel(int G[][100],int n,int arr[]){
	arr[0]=1;
	queue <int> vertexes;
	vertexes.push(0);
   
	while (!vertexes.empty()){
		int u = vertexes.front();
		vertexes.pop();
		if(G[u][u]==1){
			return false;
		}
      
		for (int i = 0; i < n; i++){
			if (G[u][i] && arr[i]==-1) {
				arr[i] = 1-arr[u];
				vertexes.push(i);
			} else if (G[u][i] && arr[i] == arr[u]) {
				return false;
			}
		}
	}
   
	return true;
}

int main () {
   // create a graph given in the above diagram
	int n;         // number of wrestlers numbered 1..n 
	int m;		   // number of rivalries
	int w1, w2;
	int temp1,temp2;
   
	cin >> n;
	int arr[n];
	for (int i = 0; i < n; i++) {
      arr[i]=-1;
		for (int j = 0; j < n; j++) {
			G[i][j]=0;  
		}
	}

	cin >> m;
	for (int j = 0; j < m; j++) {
		cin >> w1;        // 1st wrestler
		cin >> w2;        // 2nd wrestler
      
		w1--;
		w2--;

		// add edges to adjacency matrix optional
		G[w1][w2] = 1;
		G[w2][w1] = 1; 
    }

	bool result = babyfaceHeel(G,n,arr);
 
	if (result) {
      cout << "Possible"<<endl;
	}  else {
      cout << "Impossible" << endl;
	}
   
	return 0;
}