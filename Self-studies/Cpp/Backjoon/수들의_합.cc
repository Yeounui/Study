#include <iostream>

using namespace std;

int main() {
    long S;
    long T = 0;
    int i = 0;
    cin >> S;

    while (T <= S) {
        i++;
        T += i;
    }
    
    cout << i-1 << endl;
    return 0;
}