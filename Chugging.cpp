#include <bits/stdc++.h>
using namespace std;

int main() {
    int ta; 
    int da;
    int tb;
    int db;
    int n;
    int atot = 0; 
    int btot = 0;

    cin >> n;
    cin >> ta;
    cin >> da;
    cin >> tb;
    cin >> db;

    for (int i = 0; i < n; i++) {
        atot += (ta + i * da);
        btot += (tb + i * db);
    }

    if (atot == btot) {
        cout << "=" << endl;
    }
    else if (atot < btot) {
        cout << "Alice" << endl;
    }
    else if (btot < atot) {
        cout << "Bob" << endl;
    }
}