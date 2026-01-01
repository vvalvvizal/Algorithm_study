#include <iostream>
#include <queue>
using namespace std;

int main() {
    int n;
    int m[50];
    cin >> n;

    int dasom;
    cin >> dasom;

    priority_queue<int> pq;
    //heap O(nlogn)
    for (int i = 1; i < n; i++) {
       int x;
       cin >> x;
       pq.push(x);
    }

    int count  = 0;

    while (!pq.empty() && pq.top() >= dasom) {
        int top = pq.top();
        pq.pop();

        top--;
        dasom++;
        count++;

        pq.push(top);
    }

    cout << count << endl;
    return 0;
}
