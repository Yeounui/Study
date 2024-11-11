#include <iostream>

using namespace std;

int main() {
    int score;
    int sum = 0;

    for(int i=0; i<5; i++) {
        cin >> score;
        if (score >= 40) {
            sum += score;
        }
        else {
            sum += 40;
        }
    }
    cout << sum/5 << endl;
    return 0;
}