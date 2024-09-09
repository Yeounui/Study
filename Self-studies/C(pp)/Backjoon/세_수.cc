#include <iostream>

using namespace std;

void _compare(int& first, int& second) { //int&는 "int형 변수에 대한 참조" 의미. main에 있는 A,B,C를 함수 안에서 변경 가능
        
    if (first < second) {
        int temp = first;
        first = second;
        second = temp;
    }
}

int main() {
    int A, B, C;
    cin >> A >> B >> C;
    _compare(A, B);
    _compare(B, C);
    _compare(A, B);
    cout << B << endl;
    return 0;
}