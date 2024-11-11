#include <iostream>

using namespace std;

int main() {
    char gpa[3]; // \0이 맨 마지막에 들어감 그렇기에 2 + 1
    float score = 0.0; 
    cin >> gpa[0];
    if (gpa[0] != 'F') {cin >> gpa[1];}

    if (gpa[1] == '+') {score = 0.3;}
    else if (gpa[1] == '-') {score = -0.3;}
    
    if (gpa[0] == 'A') {score += 4.0;}
    else if (gpa[0] == 'B') {score += 3.0;}
    else if (gpa[0] == 'C') {score += 2.0;}
    else if (gpa[0] == 'D') {score += 1.0;}

    cout << fixed;
    cout.precision(1);
    cout << score;

	return 0;
}