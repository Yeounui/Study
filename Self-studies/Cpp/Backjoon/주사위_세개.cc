#include <iostream>

using namespace std;

void _diff(int num) {
    cout << num*100 << endl;
}

void _pair(int num) {
    cout << 1000 + (num*100) << endl;
}

int main() {
    int A, B, C;
    
    cin >> A >> B >> C;

    if (A == B) {
        if (B == C) {
            cout << 10000 + (A*1000) << endl;
        }
        else {
            _pair(A);
        }
    }
    else if (B == C) {
            _pair(B);
    }
    else if (A == C) {
            _pair(A);
    }
    else {
        if (A > B) {
            if (A > C) {
                _diff(A);
            }
            else {
                _diff(C);
            }
        }
        else {
            if (B > C) {
                _diff(B);
            }
            else {
                _diff(C);
            }
        }
    }
    return 0;
}