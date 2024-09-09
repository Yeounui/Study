#include <iostream>

using namespace std;

int main() {
    int testCase;
    char marsMath;
    float number;

    cout << fixed; //소수점 부동
    cout.precision(2); // 소수점 2번 째 자리까지 표현

    cin >> testCase;

    for(int i=0; i<testCase; i++) {
        cin >> number;
        while (1) {
            cin.get(marsMath); // cin << 와 비교하여 공백, 개행 포함하여 한글자씩만 입력받음.
            if (marsMath == '\n') {
                cout << number << endl;
                break;
            }
            else if (marsMath == '@') {
                number *= 3;
            }
            else if (marsMath == '%') {
                number += 5;
            }
            else if (marsMath == '#') {
                number -= 7;
            }
        }
    }
    
    return 0;
}