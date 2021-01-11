#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int s;

/* cada dígito possui um código que diz quais segmentos devem ser 'acesos'
 * para representá-lo
 * 
 *   0
 *   -
 * 1| |2
 *  3- 
 * 4| |5
 *  6-
 */
 
int digits[10][7] = {{1, 1, 1, 0, 1, 1, 1}, //0
					 {0, 0, 1, 0, 0, 1, 0}, //1
					 {1, 0, 1, 1, 1, 0, 1}, //2
					 {1, 0, 1, 1, 0, 1, 1}, //3
					 {0, 1, 1, 1, 0, 1, 0}, //4
					 {1, 1, 0, 1, 0, 1, 1}, //5
					 {1, 1, 0, 1, 1, 1, 1}, //6
					 {1, 0, 1, 0, 0, 1, 0}, //7
					 {1, 1, 1, 1, 1, 1, 1}, //8
					 {1, 1, 1, 1, 0, 1, 1}}; //9

//'desenharemos' os dígitos nessa matriz e depois na tela
int matrix[100][100];

void matrix_of_digits(string n){
	//dígito por dígito
	for(int i = 0; i < n.size(); i++){
		int d = (int)n[i] - 48;
		//linha por linha
		for(int j = 0; j < s; j++){
			matrix[0][(s+3)*i+1+j] = digits[d][0];
			matrix[1+j][(s+3)*i] = digits[d][1];
			matrix[1+j][(s+3)*i+s+1] = digits[d][2];
			matrix[s+1][(s+3)*i + 1 + j] = digits[d][3];
			matrix[s+2+j][(s+3)*i] = digits[d][4];
			matrix[s+2+j][(s+3)*i+s+1] = digits[d][5];
			matrix[2*s+2][(s+3)*i+1+j] = digits[d][6];
		}
	}
}

//imprimimos os caracteres na tela
void print_number(string n){
	for(int i = 0; i < 2*s+3; i++){
		for(int j = 0; j < (s+3)*n.size()-1; j++){
			if((i == 0) || (i == s+1) || (i == 2*s + 2)){
				if(matrix[i][j] == 1) cout << '-';
				else cout << ' ';
			}else{
				if(matrix[i][j] == 1) cout << '|';
				else cout << ' ';
			}
		}
		cout << endl;
	}
}

	
int main(){
	while(true){
		string n;
		cin >> s >> n;
		if(s == 0 && n.compare("0") == 0) break;
		
		memset(matrix, 0, sizeof(matrix));
		matrix_of_digits(n);
		print_number(n);
		
		cout << endl;
	}
	
	return 0;
}
