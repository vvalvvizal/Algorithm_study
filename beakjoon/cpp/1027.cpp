#include <iostream>
#include <algorithm>
using namespace std;
bool desc(int a, int b) {
	return a > b;
}

int main() {
	int a[60];
	int b[60];
	int c[60];
	int result = 0;
	int n;

	cin >> n;

	
	for (int i = 0; i < n; i++)
		cin >> a[i];
	for (int i = 0; i < n; i++)
		cin >> b[i];

	sort(a, a+n);//오름차
	sort(b, b + n, desc);//내림차


	//for (int i = 0; i < n; i++)
	//	cout << a[i];
	//cout << "\n";
	//for (int i = 0; i < n; i++)
	//	cout << b[i];


	//cout << "\n";
	for (int i = 0; i < n; i++) {
		c[i] = a[i] * b[i];

	}
	for (int i = 0; i < n; i++) {
		result += c[i];
	}
	cout << result;




}