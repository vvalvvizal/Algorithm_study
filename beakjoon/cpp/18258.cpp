#include <iostream>
#include <queue>
#define ERROR -1
using namespace std;

int main() {
    queue<int> q;
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;

    std::cin >> n;
    for (int i = 0; i < n; i++) {
        int num;
        string str;
        cin >> str;
        if (str == "push") {
            cin >> num;
            q.push(num);

        } else if (str == "pop") {
            if (q.empty())
                cout << ERROR << "\n";
            else {
                cout << q.front() << "\n";
                q.pop();
            }

        } else if (str == "size") {
            if (q.empty())
                cout << 0 << "\n";
            else
                cout << q.size() << "\n";

        } else if (str == "empty") {
            if (q.empty())
                cout << 1 << "\n";
            else
                cout << 0 << "\n";

        } else if (str == "back") {
            if (q.empty())
                cout << ERROR << "\n";
            else
                cout << q.back() << "\n";
        } else if (str == "front") {
            if (q.empty())
                cout << ERROR << "\n";
            else
                cout << q.front() << "\n";
        }
    }

    return 0;
}
