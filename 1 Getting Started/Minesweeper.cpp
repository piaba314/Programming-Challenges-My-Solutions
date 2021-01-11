#include <iostream>

using namespace std;

int x=1, n, m;
char board[100][100];

int how_many_mines(int i, int j){
	int count = 0;
	for(int di=-1; di < 2; di++){
		for(int dj=-1; dj < 2; dj++){
			if(i+di >= 0 && i+di < n && j+dj >= 0 && j+dj < m)
				if(board[i+di][j+dj] == '*') count++;
		}
	}
	return count;
}

int main(){
	
	while(true){
		cin >> n >> m;
		
		if(n == 0 && m == 0) break;
		
		if(x > 1) cout << endl;
		
		for(int i = 0; i < n; i++)
			for(int j = 0; j < m; j++)
				cin >> board[i][j];
		
		cout << "Field #" << x << ":\n";
		for(int i = 0; i < n; i++){
			for(int j = 0; j < m; j++){
				if(board[i][j] == '*') cout << '*';
				else cout << how_many_mines(i, j);
			}
			cout << endl;
		}
		
		x++;
	}
	
	return 0;
}
