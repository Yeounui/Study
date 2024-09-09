#include <iostream>
#include <string>

using namespace std;

int main() {
    int T, R;
    string S, P;

    cin >> T;

    for(int i=0; i<T; i++) {
        cin >> R;
        cin.get(); //remove front spacing.
        getline(cin, S);
        for (char chr : S) {
            P += string(R, chr);
        }
    cout << P << endl;
    P.erase(); //remove all chars in a string variable.
    }
    return 0;
}