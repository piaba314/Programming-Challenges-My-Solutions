#include <iostream>
#include <map>

using namespace std;

map<int, int> memo;

int cycle_length(int n){
	if(memo.find(n) != memo.end()) return memo[n];
	if(n == 1) return 1;
	if(n%2 == 0) return memo[n] = 1 + cycle_length(n/2);
	return memo[n] = 1 + cycle_length(3*n + 1);
}

int max_cycle_length(int i, int j){
	int m = 0;
	for(int k = i; k <= j; k++){
		int cl = cycle_length(k);
		if(cl > m) m = cl;
	}
	return m;
}

int main(){
	int x, y;
	
	while(cin >> x >> y){
		int i = min(x, y);
		int j = max(x, y);
		cout << x << " " << y << " " << max_cycle_length(i, j) << endl;
	}
	
	return 0;
}
