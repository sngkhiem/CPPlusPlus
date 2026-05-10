#include <bits/stdc++.h>

using namespace std;

mt19937_64 rng(chrono::steady_clock::now().time_since_epoch().count());

long long ran(long long l, long long r) {
    return l + (rng() % (r - l + 1));
}

string randString(long long len) {
    string s;
    for(long long i = 0; i < len; i++) s += char('a' + ran(0, 25));
    return s;
}

signed main() {
    int t = ran(1, 5);
    cout << t << "\n";
    for(int loop0 = 0; loop0 < t; loop0++) {
        long long n = ran(10000000000, 1000000000000000000);
        cout << n << "\n";
    }
    return 0;
}