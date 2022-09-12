#include <iostream>
#include <deque>

using namespace std;

int main() {
    int n, k;
    cin >> n >> k;

    deque<int> q;

    for (int i = 1; i <= n; i++) {
        q.push_back(i);
    }

    cout << "<";
    while (1) {
        int tmp = 0;
        for (int j = 0; j < k - 1; j++) { 
            tmp = q.front();
            q.pop_front();
            q.push_back(tmp);
        }
        cout << q.front();
        q.pop_front();

        if (q.size() >= 1) {
            cout << ", ";
        }
        if (q.empty())
            break;
    }

    cout << ">";
}
