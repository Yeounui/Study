#include <iostream>

using namespace std;

int main() {
    int i, A, B;
    
    cin >> i;
    
    for (int j = 0; j < i; j++) {
        int lcm = 1;
        int denominator = 2;
        cin >> A >> B;
        
        while (A != 1 || B != 1) {
            if (A%denominator == 0 || B%denominator == 0) {
                if (A%denominator == 0) {
                    A /= denominator;
                }
                if (B%denominator == 0) {
                    B /= denominator;
                }
                lcm *= denominator;
            }
            else {
                denominator++;
            }
        }
        cout << lcm << endl;
    }
    return 0;
}