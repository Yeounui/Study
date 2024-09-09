#include <iostream>

using namespace std;

int main() {
    int A, B;
    
    cin >> A >> B;
    do {
        if (A > B) {
            cout << "Yes" << endl;
        }
        else {
            cout << "No" << endl;
        }
        cin >> A >> B;
    } while (A != 0 || B != 0);
    
    return 0;
}