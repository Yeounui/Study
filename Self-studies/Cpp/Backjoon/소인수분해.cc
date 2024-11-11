#include <iostream>

using namespace std;

void _divide(int subject, int& denominator){
    if (subject != 1) {
        if (subject%denominator == 0) {
            cout << denominator << endl;
            subject /= denominator;
        }
        else {
            denominator++;
        }
        _divide(subject, denominator);
    }
}

int main() {
    int N;
    int denominator = 2;
    cin >> N;

    _divide(N, denominator);
    
    return 0;
}