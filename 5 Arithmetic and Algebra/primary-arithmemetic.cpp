#include <iostream>

using namespace std;

int number_of_carry(int a, int b){
	int count=0, carry=0, da, db;
	while(a != 0 || b  != 0){
		da = a%10;
		db = b%10;
		a = (a - da)/10;
		b = (b - db)/10;
		carry = (da + db + carry)/10;
		if(carry > 0) count += 1;
	}
	return count;
}

int main(){
	
	int a, b, n;
	
	while(true){
		cin >> a >> b;
		if(a == 0 and b == 0) break;
		n = number_of_carry(a, b);
		if(n == 0) cout << "No carry operation.\n";
		else if(n == 1) cout << "1 carry operation.\n";
		else cout << n << " carry operations.\n";
	}
	
	return 0;
}
