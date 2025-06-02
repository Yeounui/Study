#include <iostream>
int main() {
    int a = 3;
    int& another_a = a; // Reference: $another_a의 주소값은 a와 같다.
    //another_a 는 a 의 또다른 이름 이라고 컴파일러에게 알려주는 것
    //포인터와의 차이점.
    //1. 레퍼런스는 반드시 처음에 어느 변수의 별명이 될 것인지 지정되어야 함. (불가: int& another_a;)
    //2. 레퍼런스가 한 번 정의되면 절대로 다른 변수로 지정될 수 없음. (모순[주소값 = 원소값]: &another_a = b;)
    //3. 레퍼런스는 메모리 상에 존재하지 않을 수 있음. (컴파일러에겐 a나 another_a나 동일 변수.)
    another_a = 5; // another_a는 5다. 따라서 주소값이 같은 a 또한 5다.

    std::cout << "a : " << a << std::endl;
    std::cout << "another_a : " << another_a << std::endl;
    return 0;
}