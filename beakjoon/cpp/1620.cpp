#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    map<string, int> dogam;
    vector<string> pocketmon;
    int n, m;
    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        string name;
        cin >> name;
        dogam.insert({name, i + 1});
        pocketmon.push_back(name);
    }

    for (int i = 0; i < m; i++) {
        char value[21]; //문제
        cin >> value;
        if (atoi(value)) { //정수로 변환돼? -> 숫자
            cout << pocketmon[atoi(value) - 1] << '\n';
        } else { //->문자열
            cout << dogam[(string)value] << '\n';
        }
    }

    return 0;
}