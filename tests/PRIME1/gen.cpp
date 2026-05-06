#include <bits/stdc++.h>

using namespace std;

mt19937_64 rng(chrono::steady_clock::now().time_since_epoch().count());

long long ran(long long l, long long r) {
    return l + (rng() % (r - l + 1));
}

signed main() {
    int t = ran(1, 5);
    cout << t << "\n";
    for(int loop0 = 0; loop0 < t; loop0++) {
        int n = ran(1, 100000);
        cout << n << "\n";
        vector<long long> a(n);
        for(int i = 0; i < n; i++) a[i] = ran(1, 1000000000);
        for (int i = 0; i < a.size(); i++) {cout << a[i] << (i == a.size() - 1 ? "" : " "); }
        cout << "\n";
    }
    return 0;
}