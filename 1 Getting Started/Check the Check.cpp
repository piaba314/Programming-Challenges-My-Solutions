#include <iostream>
#include <cstring>
#include <map>
#include <vector>
#include <cctype>

using namespace std;

char board[8][8];
char legal_moves[8][8];
int white_king_pos[2], black_king_pos[2];

map<char, vector<vector<int>>> directions;

bool read_board(){
	bool is_empty = true;
	for(int i = 0; i < 8; i++){
		for(int j = 0; j < 8; j++){
			cin >> board[i][j];
			if(board[i][j] == 'K'){
				white_king_pos[0] = i;
				white_king_pos[1] = j;
				is_empty = false;
			}
			if(board[i][j] == 'k'){
				black_king_pos[0] = i;
				black_king_pos[1] = j;
				is_empty = false;
			}
		}
	}
	return is_empty;
}

bool is_in_board(int i, int j){
	return i >= 0 and i < 8 and j >= 0 and j < 8;
}

bool is_oposite(char p1, char p2){
	 return (islower(p1) and isupper(p2)) or (isupper(p1) and islower(p2));
}

void calc_legal_moves(int i, int j){
	memset(legal_moves, '.', sizeof(legal_moves));
	char peace = board[i][j];
	char pl = tolower(board[i][j]);
	if(peace == 'P') pl = peace;
	//peças que se movem uma casa
	if(pl == 'p' or pl == 'P' or pl == 'k' or pl == 'n'){
		for(int k = 0; k < directions[pl].size(); k++){
			int x = directions[pl][k][0];
			int y = directions[pl][k][1];
			if(is_in_board(i+x, j+y))
				if(board[i+x][j+y] == '.' or is_oposite(peace, board[i+x][j+y]))
					legal_moves[i+x][j+y] = '*';
		}
	}
	//peças que podem se mover mais de uma casa
	else if(peace != '.'){
		for(int k = 0; k < directions[pl].size(); k++){
			int x = directions[pl][k][0];
			int y = directions[pl][k][1];
			int a = i+x, b = j+y;
			while(is_in_board(a, b) and board[a][b] == '.'){
				legal_moves[a][b] = '*';
				a += x;
				b += y;
			}
			if(is_in_board(a, b) and is_oposite(peace, board[a][b]))
				legal_moves[a][b] = '*';
			
		}
	}
}

int check_the_check(){
	for(int i = 0; i < 8; i++){
		for(int j = 0; j < 8; j++){
			calc_legal_moves(i, j);
			if(legal_moves[white_king_pos[0]][white_king_pos[1]] == '*')
				return 1;
			if(legal_moves[black_king_pos[0]][black_king_pos[1]] == '*')
				return 2;
		}
	}
	return 0;
}

int main(){
	
	directions['p'] = {{1, -1}, {1, 1}};
	directions['P'] = {{-1, -1}, {-1, 1}};
	directions['r'] = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};
	directions['n'] = {{2, 1}, {2, -1}, {-2, 1}, {-2, -1}, {1, 2}, {1, -2}, {-1, -2}, {-1, 2}};
	directions['b'] = {{1, -1}, {1, 1}, {-1, -1}, {-1, 1}};
	directions['q'] = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}, {1, -1}, {1, 1}, {-1, -1}, {-1, 1}};
	directions['k'] = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}, {1, -1}, {1, 1}, {-1, -1}, {-1, 1}};

	int game = 1;
	while(!read_board()){
		int resp = check_the_check();
		if(resp == 1) cout << "Game #"<< game << ": white king is in check." << endl;
		if(resp == 2) cout << "Game #"<< game << ": black king is in check." << endl;
		if(resp == 0) cout << "Game #"<< game << ": no king is in check." << endl;
		game++;
	}
	
	return 0;
}
