#include <iostream>

using namespace std;

int main() {
    int testCase;
    int tmp[2], currentScore, currentNum;
    int diceNums[3];
    int highScore = 0;
    int idNum = 0;

    cin >> testCase;

    for(int i=0; i<testCase; i++) {
        cin >> diceNums[0] >> diceNums[1] >> diceNums[2];
        

        if  (diceNums[2] == diceNums[1] || diceNums[2] == diceNums[0]) {
            idNum++;
            currentNum = diceNums[2];
        }

        if (diceNums[0] == diceNums[1]) {
            idNum++;
            currentNum = diceNums[0];
        }

        if (idNum == 0) {
            if (diceNums[0] > diceNums[1]) {
                    currentNum = diceNums[0];
                }
                else {
                    currentNum = diceNums[1];
                }
            
                if (diceNums[2] > currentNum) {
                    currentNum = diceNums[2];
                }
        }

        if (idNum == 2) {
            currentScore = 10000 + (currentNum * 1000);
        }
        else if (idNum == 1) {
            currentScore = 1000 + (currentNum * 100);
        }
        else {
            currentScore = (100 * currentNum);
        }

        idNum = 0;
        if (highScore < currentScore) {
            highScore = currentScore;
        }
    }
    cout << highScore;
    return 0;
}