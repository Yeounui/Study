#include <iostream>

using namespace std;

int main() {
    int price, snack, money;
    int supplement = 0;
    
    cin >> price >> snack >> money;
    
    supplement = price * snack;
    if (supplement > money) {
        supplement -= money;

    }
    else {
        supplement = 0;
    }
    cout << supplement << endl;
    return 0;
}