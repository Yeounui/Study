#include <iostream>
#include <string>

using namespace std;

string _plusBigSmall(int dgtBig, int dgtSmall) {
    string result;
    
    if (dgtBig != dgtSmall) {
        result.reserve(dgtBig);
        result.append(1, '1');
        result.append(dgtBig-dgtSmall-1, '0');
        result.append(1, '1');
        result.append(dgtSmall-1, '0');
        return result;
    }
    else {
        result.reserve(dgtBig);
        result.append(1, '2');
        result.append(dgtBig-1, '0');
        return result;
    }
}
    
string _multBigSmall(int dgtBig, int dgtSmall) {
    string result;

    result.reserve(dgtBig+dgtSmall-1);
    result.append(1, '1');
    result.append(dgtBig+dgtSmall-2, '0');
    return result;
}

int main() {
    string a, b, result;
    char oper;

    cin >> a >> oper >> b;

    switch (oper) {
        case '+':
            if (a.size() >= b.size()) {
                cout << _plusBigSmall(a.size(), b.size()) << endl;
            }
            else if (a.size() < b.size()) {
                cout << _plusBigSmall(b.size(), a.size()) << endl;
            }  
            else {
                return 1;
            }
            break;
        case '*':
            cout << _multBigSmall(a.size(), b.size()) << endl;
            break;
    }
    cout << result;
    return 0;
}