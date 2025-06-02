#include <iostream>

int main() {
    int x;
    int& y = x; // x에 대한 참조자 y
    int& z = y; // 이 또한 x에 대한 참조자 z; 참조자의 참조자(int&&) 혹은 포인터(int*&)는 허용 안됨.
    // 참조자를 사용 시 포인터의 & 와 * 가 필요 없기에, 깔끔한 코드 작성 가능.
    x = 1;
    std::cout << "x : " << x << " y : " << y << " z : " << z << std::endl;
    y = 2;
    std::cout << "x : " << x << " y : " << y << " z : " << z << std::endl;
    z = 3;
    std::cout << "x : " << x << " y : " << y << " z : " << z << std::endl;
}