#include <iostream>

int function() {
    int a = 5;
    return a;
}
int main() {
    const int& c = function(); //정수에 대한 참조자는 에러 발생되지만 상수(const) 레퍼런스로 받으면 통과.
    std::cout << "c : " << c << std::endl; 
    return 0;
}

/*
int function() {
    int a = 5;
    return a;
}

int main() {
    int& c = function(); // function의 return, int 값에 대한 참조자 c가 정의되었지만 (int reference)
    // function이 종료 됨에 따라 a 또한 사라지기에 지정된 변수가 없는 참조자가 되어 에러 발생.
    c = 2;
    return 0;
}
*/
