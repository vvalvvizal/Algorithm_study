#include <deque>
#include <iostream>

using namespace std;

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);

    int t;

    cin >> t;

    for (int i = 0; i < t; i++) {

        // vector <int> number;
        deque<int> q1;
        deque<int> q2;

        int tmp = 0;
        int n, m;
        cin >> n >> m;

        for (int j = 0; j < n; j++) {
            cin >> tmp;
            q1.push_back(tmp);
            if (j == m)
                q2.push_back(1);
            else
                q2.push_back(0);
        }
        /*
        for (int j = 0; j < q1.size(); j++) {
                cout << q1[j] << " " << q2[j] << endl;
        }*/

        int result = 0;
        while (1) {
            int tmp1;
            int tmp2;
            int max = 0;

            for (int k = 0; k < q1.size(); k++) {
                // cout << q1[k] << endl;
                if (q1[k] > max) {
                    max = q1[k];
                }
            }

            tmp1 = q1.front();
            q1.pop_front();
            tmp2 = q2.front();
            q2.pop_front();
            // cout << "tmp1: " << tmp1 << "\ttmp2: " << tmp2 << endl;
            // cout << q1.size() << endl;

            // cout << "max: " << max << endl;

            if ((tmp1 == max) && (tmp2 == 1)) {
                cout << ++result << endl;
                break;
            } else if (tmp1 == max) {
                ++result;
            } else {
                q1.push_back(tmp1);
                q2.push_back(tmp2);
            }
            // cout << "result = " << result << endl;
        }
    }
}
