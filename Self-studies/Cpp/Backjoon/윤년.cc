#include <iostream>

using namespace std;

int main() {
    int year, leap;
    cin >> year;
    leap = 0;

    if (year%4 == 0) {
        if (year%100 != 0) {
            leap = 1;
            }
        else {
            if (year%400 == 0) {
            leap = 1;
            }
        }
    }
    
    cout << leap << endl;
    return 0;
}