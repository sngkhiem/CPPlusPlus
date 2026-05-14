#include <bits/stdc++.h>
using namespace std;

int main() {
    this_thread::sleep_for(chrono::seconds(2));

    int t;
    cin >> t;

    long long sum = 0;

    while (t--) {
        long long n;
        cin >> n;
        sum += n;
        cout << sum << '\n';
    }

    return 0;
}
