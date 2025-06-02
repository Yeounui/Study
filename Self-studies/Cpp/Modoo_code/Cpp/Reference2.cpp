#include <iostream>

int change_val(int &p) { //Reference를 인자로 받아들일 땐 지정하지 않아도 됨.
    p = 3;
    return 0;
}

int main() {
    int number = 5;
    std::cout << number << std::endl;
    change_val(number); //사실상, int &p = number이기에. 변수 그대로 사용 가능.
    std::cout << number << std::endl;
}