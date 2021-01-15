#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int reverse_and_add(long &n){
	string sn, srn;
	long count=0;
	while(true){
		sn = to_string(n);
		srn = sn;
		reverse(srn.begin(), srn.end());
		if(sn.compare(srn) == 0) return count;
		n += stoi(srn);
		count++;
	}
}

int main(){
	
	int N;
	long n;
	cin >> N;
	for(int i=0; i < N; i++){
		cin >> n;
		cout << reverse_and_add(n) << " " << n << endl;
	}
	
	return 0;
}
